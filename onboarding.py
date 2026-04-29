"""
IT Onboarding Checklist Automation
------------------------------------
Automates the creation of a new employee onboarding checklist for IT teams.
Generates a personalised checklist and saves it as a .txt file for each new user.

Author: Gabriella Rodrigues Ormond
"""

import datetime
import os

CHECKLIST_TEMPLATE = """
========================================
  IT ONBOARDING CHECKLIST
  New Employee: {name}
  Department: {department}
  Start Date: {start_date}
  Created: {created_at}
========================================

HARDWARE SETUP
  [ ] Assign and prepare laptop/desktop
  [ ] Install required peripherals (mouse, keyboard, monitor)
  [ ] Connect to company network (wired or Wi-Fi)
  [ ] Label asset with employee name and asset tag
  [ ] Record device in IT asset inventory

OPERATING SYSTEM & SOFTWARE
  [ ] Install and configure Windows / OS
  [ ] Apply all pending system updates
  [ ] Install antivirus and run initial scan
  [ ] Install required software:
        [ ] Google Workspace / Microsoft 365
        [ ] Company VPN client
        [ ] Communication tools (Slack, Teams, etc.)
        [ ] Any department-specific tools for: {department}

ACCOUNTS & ACCESS
  [ ] Create company email account: {email}
  [ ] Set up Google Workspace / Microsoft 365 account
  [ ] Configure email signature
  [ ] Assign correct permissions and access groups
  [ ] Set up MFA (Multi-Factor Authentication)
  [ ] Add to relevant shared drives and folders

NETWORK & SECURITY
  [ ] Confirm VPN access is working
  [ ] Brief employee on password policy
  [ ] Brief employee on data security guidelines
  [ ] Confirm printer access if required

FINAL CHECKS
  [ ] Test all software is working correctly
  [ ] Confirm internet connectivity
  [ ] Walk employee through IT helpdesk contact process
  [ ] Collect signed IT policy acknowledgement form

NOTES:
{notes}

========================================
  Completed by IT: ____________________
  Date completed: _____________________
========================================
"""

def generate_checklist(name, department, email, notes="None"):
    start_date = datetime.date.today().strftime("%d/%m/%Y")
    created_at = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    checklist = CHECKLIST_TEMPLATE.format(
        name=name,
        department=department,
        start_date=start_date,
        created_at=created_at,
        email=email,
        notes=notes
    )

    # Save to file
    filename = f"onboarding_{name.replace(' ', '_').lower()}_{start_date.replace('/', '-')}.txt"
    with open(filename, "w") as f:
        f.write(checklist)

    print(f"\n Checklist created successfully: {filename}")
    print(checklist)
    return filename

if __name__ == "__main__":
    print("IT ONBOARDING CHECKLIST GENERATOR")
    print("-" * 40)
    name       = input("New employee name: ")
    department = input("Department: ")
    email      = input("Company email: ")
    notes      = input("Any additional notes (or press Enter to skip): ") or "None"

    generate_checklist(name, department, email, notes)
