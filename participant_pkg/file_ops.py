from pathlib import Path
import csv

workspace = Path("workspace")
# workspace.mkdir(exist_ok=True)
path = workspace / "contacts.csv"

    
def save_participant(path, participant_dict):
    # Use DictWriter for writing dictionaries
    fieldnames = participant_dict.keys()
    file_exists = path.exists()
    with open(path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(participant_dict)

def load_participants(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = csv.reader(f)
        for row in content:
            print(row)
       
    