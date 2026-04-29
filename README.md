# System Health Checker 🖥️

A lightweight IT support script to quickly assess the health of a machine before opening a repair ticket or escalating an issue.

## What it does

- Displays full system information (OS, hostname, processor)
- Checks disk usage and warns if storage is running low (>85%)
- Shows system uptime
- Generates a clean, readable report in the terminal

## Why I built this

In my IT support work, the first step when a user reports a slow or faulty machine is always a quick health check. Instead of doing this manually every time, I automated the process so any technician can run it in seconds and get a clear overview.

## How to run

Make sure you have Python 3 installed, then:

```bash
python system_health.py
```

## Example output

```
==================================================
   SYSTEM HEALTH CHECK REPORT
   2025-04-01 10:32:15
==================================================

[SYSTEM INFO]
  OS: Linux
  HOSTNAME: office-pc-01
  PROCESSOR: Intel Core i5

[DISK USAGE]
  TOTAL: 238 GB
  USED: 189 GB
  FREE: 49 GB
  PERCENT_USED: 79.4%
  STATUS: OK

[UPTIME]
  UPTIME: 6h 22m

[SUMMARY]
  All checks passed. System looks healthy.
==================================================
```

## Skills demonstrated

- Python scripting
- Use of standard libraries (`platform`, `shutil`, `os`, `datetime`)
- Practical IT support thinking
- Clean output formatting for non-technical users

## Author

Gabriella Rodrigues Ormond — IT Support Technician | Dublin, Ireland
