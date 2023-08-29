"""Import gspread and Google Sheets link"""
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import sys

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

def exit_game():
    """
    Exit game command
    """
    print("\nThank you for visiting the Winter Survival Exercise!\n")
    exit()

name = input("Enter your name:\n")

begin = input("Are you ready to start? y/n \n")

scenario = SHEET.worksheet("data").acell('B2').value

def validate_begin(begin):
    """
    Validate the entry of y or n to begin game
    Check for blank entries, incorrect letters, non-string entries
    """
    if begin.lower() == 'y':
        print(scenario)
    elif begin.lower() == 'n':
        print(intro)
    else:
        print("Error! \nPlease enter y for 'yes', or n for 'no'.")
        begin

validate_begin(begin)

items = input("Are you ready to select your items? y/n \n")

def validate_items(items):
    """
    Validate the entry of y or n to begin to select items
    Check for blank entries, incorrect letters, non-string entries
    """
    if items.lower() == 'y':
        # selection()
    elif items.lower() == 'n':
        print(scenario)
    else:
        print("Error! \nPlease enter y for 'yes', or n for 'no'.")
        print(items)


