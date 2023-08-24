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

print("Welcome to the Winter Survival Exercise!\n\nIn this exercise you will test your knowledge of survival techniques and science to see if you could survive in an extreme winter environment.\n")
name = input("Enter your name:\n")
begin = input("Are you ready to start? y/n \n")



def validate_begin(begin):
    """
    Validate the entry of y or n to begin game
    Check for blank entries, incorrect letters, non-string entries
    """


scenario = f"{name}, it is mid-January and your light airplane crashed in Northern Canada this morning at 1132am.\nYou are the only survivor.\nYou are in a wilderness area made up of thick woods broken by many lakes and rivers. The last weather report indicated that the temperature would reach minus twenty-five degrees in the daytime and minus forty at night.\nYou are dressed in business clothes as you were on your way to a meeting —suit, street shoes, and overcoat./nWhile escaping from the plane you saw twelve items, but you can only manage to take five out of the plane wreck. Your task is to select five of the items and rank these five items according to their importance for your survival.\nThe items are:\n-A ball of steel wool/n-A small axe\n-A loaded .45-caliber pistol\n-Can of Crisco shortening\n-A newspapers\nCigarette lighter (without fluid)\nExtra shirt and trousers\n-20 x 20 ft. piece of heavy-duty canvas\n-An air map made of plastic\n-Half a bottle of 85-proof whiskey\n-A compass\n-Family-size chocolate bar\n")