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

def validate_items(items):
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

print(f"\nYou have chosen {first_choice}, {second_choice}, {third_choice}, {fourth_choice} and {fifth_choice}.\n")

choice_confirm = input("Are you happy with your choices? y/n \n")
