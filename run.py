"""Import gspread and Google Sheets link"""
import sys
import keyboard
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('winter-survival-game-content')

intro = SHEET.worksheet("data").acell('A2').value
print(intro)

# Exit game command with 'esc' key
if keyboard.is_pressed('Esc'):
    print("You pressed Esc so exiting game")
    sys.exit(0)

name = input("Enter your name:\n")

scenario = SHEET.worksheet("data").acell('B2').value

print(scenario)

items = input("Are you ready to select your items? y/n \n")

data = SHEET.worksheet("data").get('B5:C16')
data_list = data

def validate_items():
    """
    Validate the entry of y or n to begin to select items
    Check for blank entries, incorrect letters, non-string entries
    """
    if items.lower() == 'y':
        print(data)
    elif items.lower() == 'n':
        print(scenario)
    else:
        print("Error! \nPlease enter y for 'yes', or n for 'no'.")
        print(items)

# Naming columns for the items table
col_names = ["Item no.", "Item"]

# Displaying the table
print(tabulate(data, headers=col_names, tablefmt="grid"))

first_choice = input("\nWhich item would be your first choice? 1-12?\n")
second_choice = input("Which item would be your second choice? 1-12?\n")
third_choice = input("Which item would be your third choice? 1-12?\n")
fourth_choice = input("Which item would be your fourth choice? 1-12?\n")
fifth_choice = input("Which item would be your fifth choice? 1-12?\n")

"""
Create dictionary for item numbers and item descriptions
Match description to key chosen by user
"""
# Create dictionary of items
item_descriptions = {
    '1': "A ball of steel wool",
    '2': "A small axe",
    '3': "A loaded .45-caliber pistol",
    '4': "Tin of coconut oil",
    '5': "A newspaper",
    '6': "Cigarette lighter (without fluid)",
    '7': "Extra shirt and trousers",
    '8': "A 20 x 20 ft. piece of heavy-duty canvas",
    '9': "A sectional air map made of plastic",
    '10': "Half a bottle of 85-proof whisky",
    '11': "A compass",
    '12': "A family-size chocolate bar"
}

# Create dictionary of expert views
expert_view = {
    2: "A ball of steel wool",
    6: "A small axe",
    9: "A loaded .45-caliber pistol",
    4: "Tin of coconut oil",
    8: "A newspaper",
    1: "Cigarette lighter (without fluid)",
    3: "Extra shirt and trousers",
    5: "A 20 x 20 ft. piece of heavy-duty canvas",
    12: "A sectional air map made of plastic",
    10: "Half a bottle of 85-proof whisky",
    11: "A compass",
    7: "A family-size chocolate bar"
}

def get_item_description(choice):
    """
    Function to get item description based on choice
    """
    return item_descriptions.get(choice, "")

first_item = get_item_description(first_choice)
second_item = get_item_description(second_choice)
third_item = get_item_description(third_choice)
fourth_item = get_item_description(fourth_choice)
fifth_item = get_item_description(fifth_choice)

print(f"\nYou have chosen: {first_item}, {second_item}, {third_item}, {fourth_item}, and {fifth_item}.\n")

choice_confirm = input("Are you happy with your choices? y/n \n")


#Convert first_choice to integer for calculating score
first_choice = int(first_choice)
second_choice = int(second_choice)
third_choice = int(third_choice)
fourth_choice = int(fourth_choice)
fifth_choice = int(fifth_choice)


"""
Calculate score
"""
#First item score
matching_expertkey = None

for key, value in expert_view.items():
    if value == first_item:
        matching_expertkey = key
        break

score1 = 0
if matching_expertkey is not None:
    score1 = matching_expertkey - 1
    print(score1)
else: 
    print("No match found")

#second item score
matching_expertkey2 = None

for key, value in expert_view.items():
    if value == second_item:
        matching_expertkey2 = key
        break

score2 = 0
if matching_expertkey2 is not None:
    score2 = matching_expertkey2 - 2
    print(score2)
else: 
    print("No match found")

#Third item score
matching_expertkey3 = None

for key, value in expert_view.items():
    if value == third_item:
        matching_expertkey3 = key
        break

score3 = 0
if matching_expertkey3 is not None:
    score3 = matching_expertkey3 - 3
    print(score3)
else: 
    print("No match found")

#Fourth item score
matching_expertkey4 = None

for key, value in expert_view.items():
    if value == fourth_item:
        matching_expertkey4 = key
        break

score4 = 0
if matching_expertkey4 is not None:
    score4 = matching_expertkey4 - 4
    print(score4)
else: 
    print("No match found")

#Fifth item score
matching_expertkey5 = None

for key, value in expert_view.items():
    if value == fifth_item:
        matching_expertkey5 = key
        break

score5 = 0
if matching_expertkey5 is not None:
    score5 = matching_expertkey5 - 5
    print(score5)
else: 
    print("No match found")

#Total score
total_score = score1 + score2 + score3 + score4 + score5
print(total_score)
