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
Provide item descriptions for items chosen
"""

# Create dictionary
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

