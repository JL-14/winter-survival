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

"""
Change item numbers to item descriptions
"""
first_item = ""
if first_choice == '1':
    first_item = "A ball of steel wool"
elif first_choice == '2':
    first_item = "A small axe"
elif first_choice == '3':
    first_item = "A loaded .45-caliber pistol"
elif first_choice == '4':
    first_item = "Tin of coconut oil"
elif first_choice == '5':
    first_item = "A newspaper"
elif first_choice == '6':
    first_item = "Cigarette lighter (without fluid)"
elif first_choice == '7':
    first_item = "Extra shirt and trousers"
elif first_choice == '8':
    first_item = "A 20 x 20 ft. piece of heavy-duty canvas"
elif first_choice == '9':
    first_item = "A sectional air map made of plastic"
elif first_choice == '10':
    first_item = "Half a bottle of 85-proof whisky"
elif first_choice == '11':
    first_item = "A compass"
elif first_choice == '12':
    first_item = "A family-size chocolate bar"

second_item = ""
if second_choice == '1':
    second_item = "A ball of steel wool"
elif second_choice == '2':
    second_item = "A small axe"
elif second_choice == '3':
    second_item = "A loaded .45-caliber pistol"
elif second_choice == '4':
    second_item = "Tin of coconut oil"
elif second_choice == '5':
    second_item = "A newspaper"
elif second_choice == '6':
    second_item = "Cigarette lighter (without fluid)"
elif second_choice == '7':
    second_item = "Extra shirt and trousers"
elif second_choice == '8':
    second_item = "A 20 x 20 ft. piece of heavy-duty canvas"
elif second_choice == '9':
    second_item = "A sectional air map made of plastic"
elif second_choice == '10':
    second_item = "Half a bottle of 85-proof whisky"
elif second_choice == '11':
    second_item = "A compass"
elif second_choice == '12':
    second_item = "A family-size chocolate bar"

third_item = ""
if third_choice == '1':
    third_item = "A ball of steel wool"
elif third_choice == '2':
    third_item = "A small axe"
elif third_choice == '3':
    third_item = "A loaded .45-caliber pistol"
elif third_choice == '4':
    third_item = "Tin of coconut oil"
elif third_choice == '5':
    third_item = "A newspaper"
elif third_choice == '6':
    third_item = "Cigarette lighter (without fluid)"
elif third_choice == '7':
    third_item = "Extra shirt and trousers"
elif third_choice == '8':
    third_item = "A 20 x 20 ft. piece of heavy-duty canvas"
elif third_choice == '9':
    third_item = "A sectional air map made of plastic"
elif third_choice == '10':
    third_item = "Half a bottle of 85-proof whisky"
elif third_choice == '11':
    third_item = "A compass"
elif third_choice == '12':
    third_item = "A family-size chocolate bar"

fourth_item = ""
if fourth_choice == '1':
    fourth_item = "A ball of steel wool"
elif fourth_choice == '2':
    fourth_item = "A small axe"
elif fourth_choice == '3':
    fourth_item = "A loaded .45-caliber pistol"
elif fourth_choice == '4':
    fourth_item = "Tin of coconut oil"
elif fourth_choice == '5':
    fourth_item = "A newspaper"
elif fourth_choice == '6':
    fourth_item = "Cigarette lighter (without fluid)"
elif fourth_choice == '7':
    fourth_item = "Extra shirt and trousers"
elif fourth_choice == '8':
    fourth_item = "A 20 x 20 ft. piece of heavy-duty canvas"
elif fourth_choice == '9':
    fourth_item = "A sectional air map made of plastic"
elif fourth_choice == '10':
    fourth_item = "Half a bottle of 85-proof whisky"
elif fourth_choice == '11':
    fourth_item = "A compass"
elif fourth_choice == '12':
    fourth_item = "A family-size chocolate bar"

fifth_item = ""
if fifth_choice == '1':
    fifth_item = "A ball of steel wool"
elif fifth_choice == '2':
    fifth_item = "A small axe"
elif fifth_choice == '3':
    fifth_item = "A loaded .45-caliber pistol"
elif fifth_choice == '4':
    fifth_item = "Tin of coconut oil"
elif fifth_choice == '5':
    fifth_item = "A newspaper"
elif fifth_choice == '6':
    fifth_item = "Cigarette lighter (without fluid)"
elif fifth_choice == '7':
    fifth_item = "Extra shirt and trousers"
elif fifth_choice == '8':
    fifth_item = "A 20 x 20 ft. piece of heavy-duty canvas"
elif fifth_choice == '9':
    fifth_item = "A sectional air map made of plastic"
elif fifth_choice == '10':
    fifth_item = "Half a bottle of 85-proof whisky"
elif fifth_choice == '11':
    fifth_item = "A compass"
elif fifth_choice == '12':
    fifth_item = "A family-size chocolate bar"

print(f"\nYou have chosen: {first_item}, {second_item}, {third_item}, {fourth_item} and {fifth_item}.\n")

choice_confirm = input("Are you happy with your choices? y/n \n")
