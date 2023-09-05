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

# Intro to game
intro = SHEET.worksheet('data').acell('A2').value

def print_intro():
    """ Print intro and start question """
    print(intro)
    print(input("Are you ready to begin? y/n \n"))
print_intro()

# Exit game command with 'esc' key
# !!! Does not yet work !!!
# def exit_program():
#     """ Exiting programme when Esc is pressed """
#     keyboard.add_hotkey('esc', activate_exit)
#     keyboard.wait('esc')
# def activate_exit():
#     print("Exiting the programme, thanks for playing!")
#     keyboard.unhook_all()
#     sys.exit()
# exit_program()

# Scenario section
scenario = SHEET.worksheet('data').acell('B2').value

def print_scenario():
    """ Print scenario and choose items question """
    print(scenario)
    print(input("Are you ready to select your items? y/n \n"))
print_scenario()
# Importing items list
data = SHEET.worksheet('data').get('B5:C16')

# Naming columns for the items table
col_names = ["Item no.", "Item"]

# Continue input question with validation
# !!! Does not yet work !!!
# while True:
#     try:
#         items = str(input("Are you ready to select your items? y/n \n"))
#         if items == 'y':
#             print(data)
#         elif items == 'n':
#             print(scenario)
#             print(items)
#         else:
#             print("Please enter 'y' or 'n'")
#     except ValueError:
#         print("Please enter 'y' or 'n'")
#     else:
#         break

# Displaying the table
def display_table():
    print(tabulate(data, headers=col_names, tablefmt="grid"))
display_table()

first_choice = input("\nWhich item would be your first choice? 1-12?\n")
second_choice = input("Which item would be your second choice? 1-12?\n")
third_choice = input("Which item would be your third choice? 1-12?\n")
fourth_choice = input("Which item would be your fourth choice? 1-12?\n")
fifth_choice = input("Which item would be your fifth choice? 1-12?\n")

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
    1: "Cigarette lighter (without fluid)",
    2: "A ball of steel wool",
    3: "Extra shirt and trousers",
    4: "Tin of coconut oil",
    5: "A 20 x 20 ft. piece of heavy-duty canvas",
    6: "A small axe",
    7: "A family-size chocolate bar",
    8: "A newspaper",
    9: "A loaded .45-caliber pistol",
    10: "Half a bottle of 85-proof whisky",
    11: "A compass",
    12: "A sectional air map made of plastic" 
}

# Matching item description to item choice
def get_item_description(choice):
    """ Function to get item description based on choice """
    return item_descriptions.get(choice, "")

first_item = get_item_description(first_choice)
second_item = get_item_description(second_choice)
third_item = get_item_description(third_choice)
fourth_item = get_item_description(fourth_choice)
fifth_item = get_item_description(fifth_choice)

def print_choices():
    """ Print choices made """
    print(f"""\nYou have chosen: 
        1. {first_item}
        2. {second_item}
        3. {third_item}
        4. {fourth_item}
        5. {fifth_item}
        """)
print_choices()
choice_confirm = input("Are you happy with your choices? y/n \n")

# Convert first_choice to integer for calculating score
first_choice = int(first_choice)
second_choice = int(second_choice)
third_choice = int(third_choice)
fourth_choice = int(fourth_choice)
fifth_choice = int(fifth_choice)

# First item score
matching_expert_key = None

for key, value in expert_view.items():
    if value == first_item:
        matching_expert_key = key
        break

score_one = 0
if matching_expert_key is not None:
    score_one = matching_expert_key - 1
    score_one = abs(score_one)
else: 
    print("No match found")

# Second item score
matching_expert_key_two = None

for key, value in expert_view.items():
    if value == second_item:
        matching_expert_key_two = key
        break

score_two = 0
if matching_expert_key_two is not None:
    score_two = matching_expert_key_two - 2
    score_two = abs(score_two)
else: 
    print("No match found")

# Third item score
matching_expert_key_three = None

for key, value in expert_view.items():
    if value == third_item:
        matching_expert_key_three = key
        break

score_three = 0
if matching_expert_key_three is not None:
    score_three = matching_expert_key_three - 3
    score_three = abs(score_three)
else: 
    print("No match found")

# Fourth item score
matching_expert_key_four = None

for key, value in expert_view.items():
    if value == fourth_item:
        matching_expert_key_four = key
        break

score_four = 0
if matching_expert_key_four is not None:
    score_four = matching_expert_key_four - 4
    score_four = abs(score_four)
else: 
    print("No match found")

# Fifth item score
matching_expert_key_five = None

for key, value in expert_view.items():
    if value == fifth_item:
        matching_expert_key_five = key
        break

score_five = 0
if matching_expert_key_five is not None:
    score_five = matching_expert_key_five - 5
    score_five = abs(score_five)
else: 
    print("No match found")

# Total score
total_score = score_one + score_two + score_three + score_four + score_five

def print_final_score():
    """ Print final score """
    if total_score <= 5:
        print(f"\nYour final score is:\n\n{total_score}\n\nwhich is Excellent! You have a very good chance of survival!\n")
    elif total_score >= 6 and total_score <= 12:
        print(f"\nYour final score is:\n\n{total_score}\n\nwhich is Very Good! You have a pretty good chance of survival!\n")
    elif total_score >= 13 and total_score <= 20:
        print(f"\nYour final score is:\n\n{total_score}\n\nwhich is Good. You have a reasonable chance of survival.\n")
    else:
        print(f"\nYour final score is:\n\n{total_score}\n\nwhich is Not So Good... You have a pretty low chance of survival based on the items chosen.\n")
    print(input("Would you like to see the survival expert's feedback on the items you chose? y/n \n"))
print_final_score()

# Importing item feedback from worksheet
def expert_feedback():
    print("\nThe expert's view on your choices were:\n")
    print(f"1. {first_item}:\n")
    feedback1 = SHEET.worksheet("feedback").cell(first_choice, 2).value
    print(f"{feedback1}\n")
    print(f"2. {second_item}:\n")
    feedback2 = SHEET.worksheet("feedback").cell(second_choice, 2).value
    print(f"{feedback2}\n")
    print(f"3. {third_item}:\n")
    feedback3 = SHEET.worksheet("feedback").cell(third_choice, 2).value
    print(f"{feedback3}\n")
    print(f"4. {fourth_item}:\n")
    feedback4 = SHEET.worksheet("feedback").cell(fourth_choice, 2).value
    print(f"{feedback4}\n")
    print(f"5. {fifth_item}:\n")
    feedback5 = SHEET.worksheet("feedback").cell(fifth_choice, 2).value
    print(f"{feedback5}\n")
expert_feedback()

def again_expert_quit():
    print("Do you want to try again, see the expert's item rankings, or quit?")
    print(input("Type 't' to try again/ 'e' to see expert rankings/ 'q' to quit\n"))
again_expert_quit()

# Expert ranking table
expert_ranking_table = SHEET.worksheet("expert_rankings").get('A1:B12')

# Naming columns for the items table
col_names_expert = ["Expert rank", "Item"]

# Displaying the table
def expert_rankings():
    """ Show expert's rankings """
    print("\nThese are the expert's rankings of the items:\n")
    print(tabulate(expert_ranking_table, headers=col_names_expert, tablefmt="grid"))
expert_rankings()

# Final thank you
def final_thank_you():
    """ Print final thank you """
    print("\nThank you for visiting the Winter Survival Exercise!\n")
final_thank_you()

