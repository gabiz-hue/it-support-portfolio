# IT Onboarding Automation 🚀

A Python script that automates the generation of personalised IT onboarding checklists for new employees.

## What it does

- Asks for the new employee's name, department, and email
- Generates a complete, personalised IT onboarding checklist
- Saves the checklist as a `.txt` file for the IT team to use and sign off

## Why I built this

Every time a new employee joins, the IT team needs to go through the same setup process. Doing this from memory leads to missed steps. This script ensures every onboarding follows the same standard, saves time, and creates a record for each new user.

## How to run

```bash
python onboarding.py
```

You will be prompted to enter:
- Employee name
- Department
- Company email
- Any additional notes

A `.txt` checklist file will be created automatically.

## Example output file

```
========================================
  IT ONBOARDING CHECKLIST
  New Employee: John Murphy
  Department: Finance
  Start Date: 01/04/2025
========================================

HARDWARE SETUP
  [ ] Assign and prepare laptop/desktop
  [ ] Connect to company network
  ...

ACCOUNTS & ACCESS
  [ ] Create company email: john.murphy@company.ie
  [ ] Set up MFA
  ...
========================================
```

## Skills demonstrated

- Python scripting and user input handling
- String formatting and file I/O
- IT process knowledge (onboarding, asset management, account setup)
- Practical automation for real IT workflows

## Author

Gabriella Rodrigues Ormond — IT Support Technician | Dublin, Ireland
