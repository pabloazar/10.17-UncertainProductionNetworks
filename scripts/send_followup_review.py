import os
import sys
from pathlib import Path

# Configuration for the specific models requested
MODELS = {
    "super_grok": {
        "provider": "xai",
        "model": "grok-4-1-fast-reasoning",
        "env_key": "XAI_API_KEY",
        "url": "https://api.x.ai/v1/chat/completions"
    },
    "claude_opus_deepthink": {
        "provider": "anthropic",
        "model": "claude-opus-4-5-20251101",
        "env_key": "ANTHROPIC_API_KEY",
        "thinking_budget": 10000
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
    ]
    
    for agent_file in agent_files:
        path = agent_framework_dir / agent_file
        content = load_file(path)
        if content:
            guidelines.append(f"### {agent_file.replace('/', ' - ').replace('.md', '')}\n{content}")
    
    return "\n\n".join(guidelines)

def main():
    print("Initializing Follow-up Review via LLMs...")
    print("Models: Super Grok, Claude Opus 4.5 Deep Think")
    
    # Load content
    root_dir = Path(__file__).parent.parent
    agent_framework_dir = root_dir / "agent_framework"
    paper_path = root_dir / "paper.tex"
    diff_path = root_dir / "paper_diff.tex"  # latexdiff output
    system_prompt_path = root_dir / "prompts/math_check_system_prompt.txt"
    user_prompt_path = root_dir / "prompts/followup_review_prompt.txt"

    # Load all content
    agent_guidelines = load_agent_guidelines(agent_framework_dir)
    paper_content = load_file(paper_path)
    diff_content = load_file(diff_path)
    
    if len(paper_content) < 100:
        print("Error: Paper content seems too short or empty.")
        return

    system_prompt_template = load_file(system_prompt_path)
    user_prompt_template = load_file(user_prompt_path)

    # Format prompts
    system_prompt = system_prompt_template.replace("{agent_guidelines}", agent_guidelines)
    user_prompt = user_prompt_template.replace("{paper_content}", paper_content).replace("{diff_content}", diff_content)

    print(f"Loaded paper ({len(paper_content)} bytes) and diff ({len(diff_content)} bytes).")
    print("Starting API calls...\n")

    import requests

    for name, config in MODELS.items():
        print(f"--- Sending to {name} ({config['model']}) ---")
        api_key = os.environ.get(config["env_key"])
        
        if not api_key:
            print(f"⚠️  Skipping {name}: {config['env_key']} not found.")
            continue

        try:
            output = ""
            
            if config["provider"] == "anthropic":
                import anthropic
                client = anthropic.Anthropic(api_key=api_key)
                
                request_params = {
                    "model": config["model"],
                    "max_tokens": 16000,
                    "messages": [{"role": "user", "content": user_prompt}]
                }
                
                if system_prompt:
                    request_params["system"] = system_prompt
                
                if "thinking_budget" in config:
                    request_params["thinking"] = {
                        "type": "enabled",
                        "budget_tokens": config["thinking_budget"]
                    }
                
                response = client.messages.create(**request_params)
                
                output = ""
                for block in response.content:
                    if block.type == "thinking":
                        output += f"\n### THINKING PROCESS ###\n{block.thinking}\n\n"
                    elif block.type == "text":
                        output += block.text

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
            out_filename = f"followup_review_{name}.md"
            with open(out_filename, "w") as f:
                f.write(output)
            print(f"✅ Success! Output saved to {out_filename}\n")

        except Exception as e:
            print(f"❌ FAILED to call {name}: {str(e)}\n")

    print("\n=== Follow-up Review Complete ===")

if __name__ == "__main__":
    main()
