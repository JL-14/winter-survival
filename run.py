"""Import gspread and Google Sheets link"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('winter-survival-game-content')

def start_screen():
    """
    Open start screen
    """
    print("\nWelcome to the Winter Survival Exercise!\n\nIn this exercise you will test your knowledge of survival techniques and science to see if you could survive in an extreme winter environment. Press 'esc' at any point to quit.\n")

start_screen()

def exit():
    """
    Exit game command
    """
    print("Thank you for visiting the Winter Survival Exercise!")

name = input("Enter your name:\n")
begin = input("Are you ready to start? y/n \n")

def scenario():
    """
    Display the winter survival scenario
    """ 
    print(f"\n{name}, it is mid-January and your light airplane crashed in Northern Canada this morning at 1132am.\n\nYou are the only survivor.\n\nYou are in a snowy wilderness area made up of thick woods broken by many lakes and rivers. The last weather report indicated that the temperature would reach minus twenty-five degrees in the daytime and minus forty at night.\n\nYou are dressed in business clothes as you were on your way to a meeting —suit, street shoes, and overcoat.\n\nWhile escaping from the plane you saw twelve items, but you can only manage to take five out of the plane wreck. Your task is to select five of the items and rank these five items according to their importance for your survival.\n\nThe items are:\n\n-A ball of steel wool\n-A small axe\n-A loaded .45-caliber pistol\n-Can of Crisco shortening\n-A newspaper\n-Cigarette lighter (without fluid)\n-Extra shirt and trousers\n-20 x 20 ft. piece of heavy-duty canvas\n-An air map made of plastic\n-Half a bottle of 85-proof whiskey\n-A compass\n-Family-size chocolate bar\n")

def validate_begin(begin):
    """
    Validate the entry of y or n to begin game
    Check for blank entries, incorrect letters, non-string entries
    """
    if begin.lower() == 'y':
        scenario()
    elif begin.lower() == 'n':
        exit()
    else:
        print("Error! \nPlease enter y for 'yes', or n for 'no'.")
        begin

validate_begin(begin)

items = input("Are you ready to select your items? You will see the list again on the next screen. y/n \n")

def validate_items(items):
    """
    Validate the entry of y or n to begin to select items
    Check for blank entries, incorrect letters, non-string entries
    """
    if item.lower() == 'y':
        selection()
    elif item.lower() == 'n':
        exit()
    else:
        print("Error! \nPlease enter y for 'yes', or n for 'no'.")
        begin


