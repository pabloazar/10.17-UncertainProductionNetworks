import os
import sys
import requests
import json
from pathlib import Path

# Configuration for the specific models requested
MODELS = {
    "super_grok": {
        "provider": "xai",
        "model": "grok-4-1-fast-reasoning",  # Super Grok
        "env_key": "XAI_API_KEY",
        "url": "https://api.x.ai/v1/chat/completions"
    },
    "chatgpt_5_pro": {
        "provider": "openai",
        "model": "gpt-5.1-2025-11-13",  # ChatGPT 5 Pro
        "env_key": "OPENAI_API_KEY"
    },
    "claude_opus_deepthink": {
        "provider": "anthropic",
        "model": "claude-opus-4-5-20251101",  # Claude Opus 4.5 with extended thinking
        "env_key": "ANTHROPIC_API_KEY",
        "thinking_budget": 10000
    },
    "gemini_3": {
        "provider": "google",
        "model": "gemini-3-pro-preview",  # Gemini 3 Pro Preview
        "env_key": "GOOGLE_API_KEY"
    }
}

def load_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""

def load_agent_guidelines(agent_framework_dir):
    """Load all agent .md files as reference guidelines"""
    guidelines = []
    agent_files = [
        "economists/model_agent.md",
        "economists/empirical_agent.md",
        "economists/research_log_agent.md",
        "writers/paper/paper_agent.md"
    ]
    
    for agent_file in agent_files:
        path = agent_framework_dir / agent_file
        content = load_file(path)
        if content:
            guidelines.append(f"### {agent_file.replace('/', ' - ').replace('.md', '')}\n{content}")
    
    return "\n\n".join(guidelines)

def main():
    print("Initializing Math Check via LLMs...")
    print("Models: Super Grok, ChatGPT 5 Pro, Claude Opus 4.5 Deep Think, Gemini 3")
    
    # Load content
    root_dir = Path(__file__).parent.parent
    agent_framework_dir = root_dir / "agent_framework"
    paper_path = root_dir / "new_draft_2.tex"
    system_prompt_path = root_dir / "prompts/math_check_system_prompt.txt"
    user_prompt_path = root_dir / "prompts/math_check_user_prompt.txt"

    # Load all agent guidelines
    agent_guidelines = load_agent_guidelines(agent_framework_dir)
    paper_content = load_file(paper_path)
    
    # Simple check to ensure we have content
    if len(paper_content) < 100:
        print("Error: Paper content seems too short or empty.")
        return

    system_prompt_template = load_file(system_prompt_path)
    user_prompt_template = load_file(user_prompt_path)

    # Format prompts with agent guidelines
    system_prompt = system_prompt_template.replace("{agent_guidelines}", agent_guidelines)
    user_prompt = user_prompt_template.replace("{paper_content}", paper_content)

    print(f"Loaded paper ({len(paper_content)} bytes) and {len(agent_guidelines)} bytes of agent guidelines.")
    print("Starting API calls...\n")

    for name, config in MODELS.items():
        print(f"--- Sending to {name} ({config['model']}) ---")
        api_key = os.environ.get(config["env_key"])
        
        if not api_key:
            print(f"⚠️  Skipping {name}: {config['env_key']} not found in environment variables.")
            print(f"   To enable, run: export {config['env_key']}='your-key-here'\n")
            continue

        try:
            output = ""
            
            if config["provider"] == "openai":
                import openai
                client = openai.OpenAI(api_key=api_key)
                
                # Check if o1 model (needs special handling)
                if "o1" in config["model"]:
                    combined_content = f"SYSTEM INSTRUCTIONS:\n{system_prompt}\n\nUSER REQUEST:\n{user_prompt}"
                    response = client.chat.completions.create(
                        model=config["model"],
                        messages=[{"role": "user", "content": combined_content}]
                    )
                else:
                    # Standard ChatGPT models support system messages
                    response = client.chat.completions.create(
                        model=config["model"],
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ]
                    )
                
                output = response.choices[0].message.content

            elif config["provider"] == "anthropic":
                import anthropic
                client = anthropic.Anthropic(api_key=api_key)
                
                # Build request with thinking enabled
                request_params = {
                    "model": config["model"],
                    "max_tokens": 16000,
                    "messages": [{"role": "user", "content": user_prompt}]
                }
                
                # Add system message if supported
                if system_prompt:
                    request_params["system"] = system_prompt
                
                # Enable extended thinking
                if "thinking_budget" in config:
                    request_params["thinking"] = {
                        "type": "enabled",
                        "budget_tokens": config["thinking_budget"]
                    }
                
                response = client.messages.create(**request_params)
                
                # Extract thinking and text from response
                output = ""
                for block in response.content:
                    if block.type == "thinking":
                        output += f"\n### THINKING PROCESS ###\n{block.thinking}\n\n"
                    elif block.type == "text":
                        output += block.text

            elif config["provider"] == "google":
                from google import genai
                from google.genai import types
                
                client = genai.Client()
                
                # Build the request with thinking enabled for deep reasoning
                response = client.models.generate_content(
                    model=config["model"],
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        thinking_config=types.ThinkingConfig(
                            thinking_level="high"  # Use "high" for deep thinking
                        )
                    )
                )
                
                output = response.text

            elif config["provider"] == "xai":
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
                
                data = {
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "model": config["model"],
                    "stream": False,
                    "temperature": 0
                }
                
                resp = requests.post(config["url"], headers=headers, json=data)
                resp.raise_for_status()
                output = resp.json()['choices'][0]['message']['content']

            # Save output
            out_filename = f"math_check_{name}.md"
            with open(out_filename, "w") as f:
                f.write(output)
            print(f"✅ Success! Output saved to {out_filename}\n")

        except Exception as e:
            print(f"❌ FAILED to call {name}: {str(e)}\n")

    print("\n=== Math Check Complete ===")
    print("Review the generated math_check_*.md files for detailed feedback.")

if __name__ == "__main__":
    main()
