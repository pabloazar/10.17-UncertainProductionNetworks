# Flipside Data Query: High-Frequency MEV Bot Trading Stats

## Objective
Rerun the crash, boom, and depeg queries to collect bot trading statistics at finer time granularities: **5 minutes, 15 minutes, 30 minutes, and 1 hour** windows around each event.

## Context
We're studying whether "deep" vs "shallow" MEV bots respond differently to real fundamental shocks vs noise. Current hourly data is too coarse to capture the initial reaction. We need to see bot behavior in the first 5-15 minutes of an event.

## Required Output Schema

For each event type (crash, boom, depeg), generate a table with:

| Column | Description |
|--------|-------------|
| `BOT_ADDRESS` | Bot wallet address |
| `TOKEN_ADDRESS` | Token/pool being traded |
| `EVENT_TIMESTAMP` | Start of the event (crash/boom/depeg detected) |
| `WINDOW_MINUTES` | Time window: 5, 15, 30, or 60 |
| `NET_FLOW_USD` | Net USD flow (positive = bought, negative = sold) |
| `NET_TOKEN_FLOW` | Net token flow |
| `VOLUME_USD` | Total trading volume in USD |
| `SWAP_COUNT` | Number of swaps |
| `SHALLOW_AGENT` | 1 if bot is classified as shallow, 0 otherwise |

## Queries Needed

### 1. Flash Crashes (with time windows)

```sql
-- For each flash crash event, compute bot stats at 5/15/30/60 min windows
WITH crash_events AS (
  -- Your existing crash detection query
  -- Returns: TOKEN_ADDRESS, CRASH_TIMESTAMP, CRASH_SEVERITY, etc.
),
time_windows AS (
  SELECT 5 AS window_minutes UNION ALL
  SELECT 15 UNION ALL
  SELECT 30 UNION ALL
  SELECT 60
),
bot_trades AS (
  SELECT 
    c.TOKEN_ADDRESS,
    c.CRASH_TIMESTAMP as EVENT_TIMESTAMP,
    w.window_minutes,
    t.ORIGIN_FROM_ADDRESS as BOT_ADDRESS,
    SUM(CASE WHEN t.SYMBOL = c.TOKEN_SYMBOL THEN 
      CASE WHEN t.event_name = 'swap_out' THEN -t.AMOUNT_USD 
           ELSE t.AMOUNT_USD END
    ELSE 0 END) as NET_FLOW_USD,
    SUM(CASE WHEN t.SYMBOL = c.TOKEN_SYMBOL THEN 
      CASE WHEN t.event_name = 'swap_out' THEN -t.AMOUNT 
           ELSE t.AMOUNT END
    ELSE 0 END) as NET_TOKEN_FLOW,
    SUM(t.AMOUNT_USD) as VOLUME_USD,
    COUNT(*) as SWAP_COUNT
  FROM crash_events c
  CROSS JOIN time_windows w
  JOIN ethereum.defi.ez_dex_swaps t 
    ON t.BLOCK_TIMESTAMP >= c.CRASH_TIMESTAMP 
    AND t.BLOCK_TIMESTAMP < DATEADD(minute, w.window_minutes, c.CRASH_TIMESTAMP)
    AND (t.TOKEN_IN = c.TOKEN_ADDRESS OR t.TOKEN_OUT = c.TOKEN_ADDRESS)
  WHERE t.ORIGIN_FROM_ADDRESS IN (SELECT bot_address FROM known_mev_bots)
  GROUP BY 1,2,3,4
)
SELECT 
  bt.*,
  CASE WHEN b.is_shallow = 1 THEN 1 ELSE 0 END as SHALLOW_AGENT
FROM bot_trades bt
LEFT JOIN bot_classifications b ON bt.BOT_ADDRESS = b.bot_address
```

### 2. Flash Booms (with time windows)

Same structure as crashes, but using boom detection criteria (rapid price increase).

### 3. Stablecoin Depegs (with time windows)

Same structure, but for stablecoin deviation from peg events.

## Bot Classification

Use the existing `SHALLOW_AGENT` classification based on:
- Trade frequency patterns
- Gas price sensitivity
- MEV strategy signatures (sandwich, arbitrage, etc.)

## Deliverables

Save the following CSV files to `/Users/pabloazar/Dropbox/10.09-TC0Finance/data/`:

1. `crash_bot_stats_5min.csv`
2. `crash_bot_stats_15min.csv`
3. `crash_bot_stats_30min.csv`
4. `crash_bot_stats_60min.csv`
5. `boom_bot_stats_5min.csv`
6. `boom_bot_stats_15min.csv`
7. `boom_bot_stats_30min.csv`
8. `boom_bot_stats_60min.csv`
9. `depeg_bot_stats_5min.csv`
10. `depeg_bot_stats_15min.csv`
11. `depeg_bot_stats_30min.csv`
12. `depeg_bot_stats_60min.csv`

Alternatively, save as single files with `WINDOW_MINUTES` column:
- `crash_bot_stats_highfreq.csv`
- `boom_bot_stats_highfreq.csv`
- `depeg_bot_stats_highfreq.csv`

## Additional Notes

- Use the same event definitions as the existing queries
- Include placebo periods (e.g., 1 week before each event) for comparison
- Ensure we capture the same set of bots across all time windows
- Include a `EVENT_ID` column to link observations across windows
