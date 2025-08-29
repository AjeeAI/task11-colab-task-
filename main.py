from pathlib import Path
import file_ops  # Import your custom module with save_participant function

workspace = Path("workspace")  # Path object for workspace folder
# workspace.mkdir(exist_ok=True)  # (commented out) creates the workspace folder if missing
path = workspace / "contacts.csv"  # Define CSV file path inside workspace

participant_dict = {}  # Dictionary to store user details temporarily

while True:  # Keep asking until user decides to stop
   

   while True:
    try:
        name = input("Enter user name: ")  # Ask for name
        if name == "":  # Prevent empty input
            print("This field cannot be empty!")
            continue
        elif name.isdigit():
            print("Name cannot be a number! Try again.")
            continue
        else:
            participant_dict["Name"] = name  # Save name in dictionary
    except Exception as e:  # Catch unexpected input errors
        print(f"The error was {e}")

    while True:
        try:
            age = int(input("Enter user age: "))  # Ask for age, must be integer
            if age == "":  # This check won’t actually trigger (since age is int)
                print("This field cannot be empty!")
                continue
            else:
                participant_dict["Age"] = age  # Save age in dictionary
                break
        except Exception as e:
            print(f"The error was {e}")
            continue

    while True:
        try:
            number = input("Enter user phone number: ")  # Ask for phone number
            if number == "":  # Check for empty input
                print("This field cannot be empty!")
                continue
            elif len(number) != 11:  # Validate phone number length
                print("Invalid length. Phone number must be 11 digits.")
                continue
            elif number.isalpha():
                print("Only digits allowed.")
                continue
            else:
                participant_dict["Phone number"] = number  # Save number in dictionary
                break
        except Exception as e:
            print(f"The error was {e}")

    while True:
        try:
            track = input("Enter user track: ")  # Ask for user’s track
            if track == "":  # Prevent empty input
                print("This field cannot be empty!")
                continue
            else:
                participant_dict["Track"] = track  # Save track in dictionary
                break
        except Exception as e:
            print(f"The error was {e}")

    # Save collected details into the CSV file via file_ops
    file_ops.save_participant(path, participant_dict)
    file_ops.load_participants(path)
    while True:
        try:
            exit = input("\nDo you wish to continue?\n 1. Yes\n 2. No\n")
            if exit == "1":
                break  # break inner loop, return to "Enter user name"
            elif exit == "2":
                print("Your details have been collected successfully.")
                quit()  # end the whole program
            else:
                raise Exception("Enter 1 or 2")
        except Exception as e:
            print(e)
            continue  # repeat this same question if input is wrong


    