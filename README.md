# Helpdesk Incident Log Manager 📋

A lightweight command-line tool for logging, tracking, and resolving IT support incidents — no expensive software required.

## What it does

- Log new support incidents with user, issue description, category, and priority
- View all open and resolved incidents in a clean table format
- Mark incidents as resolved with resolution details and date
- Saves everything to a local CSV file — easy to share or open in Excel

## Why I built this

In small IT teams, support tickets are often tracked in messy spreadsheets or not tracked at all. This tool gives any IT support technician a simple, consistent way to document incidents, which helps identify recurring problems and improve response times.

## How to run

```bash
python helpdesk_log.py
```

No external libraries needed — runs with standard Python 3.

## Menu options

```
=============================
  HELPDESK INCIDENT MANAGER
=============================
1. Log new incident
2. View all incidents
3. Resolve an incident
4. Exit
```

## Example incident log (CSV output)

| ID | Date | User | Issue | Category | Priority | Status | Resolution |
|----|------|------|-------|----------|----------|--------|------------|
| 1 | 01/04/2025 | John Murphy | PC won't start | Hardware | High | Resolved | Replaced faulty RAM |
| 2 | 02/04/2025 | Sara Kelly | Can't access email | Account/Access | Medium | Open | | |

## Skills demonstrated

- Python scripting
- CSV file handling and data persistence
- IT service management thinking (incident tracking, categorisation, resolution)
- Clean CLI interface design
- Practical solution for a real IT support problem

## Author

Gabriella Rodrigues Ormond — IT Support Technician | Dublin, Ireland
