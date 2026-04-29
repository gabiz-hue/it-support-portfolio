"""
Helpdesk Incident Log Manager
-------------------------------
A simple CSV-based incident tracker for small IT support teams.
Log, view, and update support tickets without needing expensive software.

Author: Gabriella Rodrigues Ormond
"""

import csv
import os
import datetime

LOG_FILE = "incident_log.csv"
HEADERS = ["ID", "Date", "User", "Issue", "Category", "Priority", "Status", "Resolution", "Resolved Date"]

CATEGORIES = ["Hardware", "Software", "Network", "Account/Access", "Other"]
PRIORITIES = ["Low", "Medium", "High", "Critical"]
STATUSES   = ["Open", "In Progress", "Resolved", "Closed"]

def initialise_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
        print(f"Incident log created: {LOG_FILE}")

def get_next_id():
    with open(LOG_FILE, "r") as f:
        rows = list(csv.reader(f))
        return len(rows)  # header counts as row 1, so IDs start at 1

def log_incident():
    print("\n--- LOG NEW INCIDENT ---")
    user     = input("User name: ")
    issue    = input("Issue description: ")

    print("Categories:", ", ".join(f"{i+1}. {c}" for i, c in enumerate(CATEGORIES)))
    cat_idx  = int(input("Select category (number): ")) - 1
    category = CATEGORIES[cat_idx]

    print("Priority:", ", ".join(f"{i+1}. {p}" for i, p in enumerate(PRIORITIES)))
    pri_idx  = int(input("Select priority (number): ")) - 1
    priority = PRIORITIES[pri_idx]

    incident_id = get_next_id()
    date = datetime.date.today().strftime("%d/%m/%Y")

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([incident_id, date, user, issue, category, priority, "Open", "", ""])

    print(f"\n Incident #{incident_id} logged successfully.")

def view_incidents():
    print("\n--- ALL INCIDENTS ---")
    with open(LOG_FILE, "r") as f:
        rows = list(csv.reader(f))

    if len(rows) <= 1:
        print("No incidents logged yet.")
        return

    print(f"{'ID':<5} {'Date':<12} {'User':<15} {'Category':<12} {'Priority':<10} {'Status':<12} {'Issue'}")
    print("-" * 90)
    for row in rows[1:]:
        print(f"{row[0]:<5} {row[1]:<12} {row[2]:<15} {row[4]:<12} {row[5]:<10} {row[6]:<12} {row[3][:50]}")

def resolve_incident():
    print("\n--- RESOLVE INCIDENT ---")
    view_incidents()
    incident_id = input("\nEnter Incident ID to resolve: ")
    resolution  = input("Resolution details: ")
    resolved_date = datetime.date.today().strftime("%d/%m/%Y")

    rows = []
    updated = False
    with open(LOG_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == incident_id:
                row[6] = "Resolved"
                row[7] = resolution
                row[8] = resolved_date
                updated = True
            rows.append(row)

    if updated:
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"\n Incident #{incident_id} marked as resolved.")
    else:
        print(f" Incident #{incident_id} not found.")

def main():
    initialise_log()
    while True:
        print("\n=============================")
        print("  HELPDESK INCIDENT MANAGER")
        print("=============================")
        print("1. Log new incident")
        print("2. View all incidents")
        print("3. Resolve an incident")
        print("4. Exit")
        choice = input("\nSelect option: ")

        if choice == "1":
            log_incident()
        elif choice == "2":
            view_incidents()
        elif choice == "3":
            resolve_incident()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
