from pathlib import Path  # Import Path object for handling file and folder paths
import csv  # Import csv module for reading/writing CSV files

workspace = Path("workspace")  # Create a Path object pointing to "workspace" folder
workspace.mkdir(exist_ok=True)  # Create the folder if it doesn't already exist
path = workspace / "contacts.csv"  # Define the file path for contacts.csv inside workspace



def save_participant(path, participant_dict):
    # Open the CSV file in append mode (a) so new rows get added, not overwrite
    fieldnames = participant_dict.keys()  # Use dict keys as column headers
    file_exists = path.exists()  # Check if the file already exists
    with open(path, "a", encoding="utf-8", newline = "") as f:
      writer = csv.DictWriter(f, fieldnames=fieldnames)  # Create a DictWriter (maps dict to CSV rows)
      if not file_exists:  
            # If file is new, write the header row first
        writer.writeheader()
        
        # Write the participant data as a new row in the CSV
      writer.writerow(participant_dict)


def load_participants(path):
    # Open the CSV file in read mode (r)
    with open(path, "r", encoding="utf-8") as f:
        content = csv.reader(f)  # Create a CSV reader object (iterates over rows)
        for row in content:
           print(row)