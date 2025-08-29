from pathlib import Path
import csv

def save_participant(path,dictionary):
    participant_header = ['Name','Age','Track' ,'Phone_Number']
    if path.exists()==True:
        with open(path,"r",newline="", encoding="utf-8") as f:
            writer= csv.reader(f)
        if f.readline == "":
                writer = csv.DictWriter(f,fieldnames=participant_header)
                writer.writeheader()
                writer.writerow(dictionary)
        elif f.readline != "":
            with open(path,"a",newline="", encoding="utf-8") as f:
                writer= csv.writer(f)
                writer.writerow(dictionary)
    else:
        with open(path,"w",newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f,fieldnames=participant_header)
            writer.writeheader()
            writer.writerow(dictionary)
def load_participants(path):
    with open(path, "r", newline="" ,encoding="utf-8") as f:
        writer = csv.reader(f)
        for row_num, row in enumerate(writer):
            if row_num== 0:
                print(f"Headers: {'|'.join(row)}")
                print("-"*40)
            else: #Data rows
                name,age,Track,Phone_number =row
                
                print(f"{name} ({age} years) - {Track} --- {Phone_number}")
