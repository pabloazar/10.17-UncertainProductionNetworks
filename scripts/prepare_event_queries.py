#!/usr/bin/env python3
"""Utility to generate Flipside Crypto SQL for event windows.

Reads `data/market_events.json` and `data/mev_bot_complexity.csv` to
produce parameterized SQL queries that pull swap transactions for the
tracked bots around each event (+/- 24h buffer).  Queries are printed to
stdout by default but can also be written to disk.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
EVENT_PATH = BASE_DIR / "data" / "market_events.json"
COMPLEXITY_PATH = BASE_DIR / "data" / "mev_bot_complexity.csv"

DATE_FMT = "%Y-%m-%d"

SQL_TEMPLATE = """
-- {event_name}
SELECT
    block_timestamp,
    tx_hash,
    event_index,
    trader_address AS bot_address,
    platform,
    pool_address,
    token_in,
    token_out,
    amount_in_usd,
    amount_out_usd
FROM flipside_prod_db.ethereum.dex_swaps
WHERE block_timestamp BETWEEN TIMESTAMP '{window_start}' AND TIMESTAMP '{window_end}'
  AND trader_address IN ({address_list})
ORDER BY block_timestamp;
""".strip()

def load_bot_addresses() -> list[str]:
    df = pd.read_csv(COMPLEXITY_PATH, usecols=["SENDER"])
    addresses = sorted(set(df["SENDER"].str.lower()))
    return addresses

def load_events() -> list[dict]:
    with EVENT_PATH.open() as fh:
        events = json.load(fh)
    return events

def format_address_list(addresses: list[str]) -> str:
    return ",\n        ".join(f"'{addr}'" for addr in addresses)

def compute_window(start: str, end: str, buffer_hours: int) -> tuple[str, str]:
    start_dt = datetime.strptime(start, DATE_FMT) - timedelta(hours=buffer_hours)
    end_dt = datetime.strptime(end, DATE_FMT) + timedelta(hours=buffer_hours)
    return start_dt.strftime("%Y-%m-%d %H:%M:%S"), end_dt.strftime("%Y-%m-%d %H:%M:%S")

def main():
    parser = argparse.ArgumentParser(description="Generate Flipside SQL for event windows")
    parser.add_argument("--buffer-hours", type=int, default=24,
                        help="Hours to pad before/after each event window")
    parser.add_argument("--output", type=Path,
                        help="Optional file to write concatenated SQL queries")
    args = parser.parse_args()

    addresses = load_bot_addresses()
    events = load_events()
    address_list = format_address_list(addresses)

    queries = []
    for event in events:
        window_start, window_end = compute_window(event["start_date"], event["end_date"], args.buffer_hours)
        queries.append(SQL_TEMPLATE.format(
            event_name=event["event_name"],
            window_start=window_start,
            window_end=window_end,
            address_list=address_list,
        ))

    content = "\n\n".join(queries)
    if args.output:
        args.output.write_text(content)
        print(f"Saved {len(queries)} queries to {args.output}")
    else:
        print(content)

if __name__ == "__main__":
    main()
