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
def print_intro():
    """ Printing intro and starting game """
    intro = SHEET.worksheet('data').acell('A2').value
    print(intro)
    print(input("Are you ready to begin? y/n \n"))

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
def print_scenario():
    """ Import and print scenario and instructions, import table """
    scenario = SHEET.worksheet('data').acell('B2').value
    print(scenario)
    print(input("Are you ready to select your items? y/n \n"))

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

# Importing and displaying items list
def items_table():
    """ Import and display table of items"""
    data = SHEET.worksheet('data').get('B5:C16')
    col_names = ["Item no.", "Item"]
    print(tabulate(data, headers=col_names, tablefmt="grid"))

# Create dictionary of items
item_descriptions = {
    1: "A ball of steel wool",
    2: "A small axe",
    3: "A loaded .45-caliber pistol",
    4: "Tin of coconut oil",
    5: "A newspaper",
    6: "Cigarette lighter (without fluid)",
    7: "Extra shirt and trousers",
    8: "A 20 x 20 ft. piece of heavy-duty canvas",
    9: "A sectional air map made of plastic",
    10: "Half a bottle of 85-proof whisky",
    11: "A compass",
    12: "A family-size chocolate bar"
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

def item_choices():
    """ Ask user to choose top 5 items """
    first_choice = int(input("\nWhich item would be your first choice? 1-12?\n"))
    second_choice = int(input("Which item would be your second choice? 1-12?\n"))
    third_choice = int(input("Which item would be your third choice? 1-12?\n"))
    fourth_choice = int(input("Which item would be your fourth choice? 1-12?\n"))
    fifth_choice = int(input("Which item would be your fifth choice? 1-12?\n"))
    return first_choice, second_choice, third_choice, fourth_choice, fifth_choice

# Matching item description to item choice
def get_item_description(choice):
    """ Function to get item description based on choice """
    return item_descriptions.get(choice, "")

def match_description_to_choice(first_choice, second_choice, third_choice, fourth_choice, fifth_choice):
    """ Match items chosen to the description of item """
    first_item = get_item_description(first_choice)
    second_item = get_item_description(second_choice)
    third_item = get_item_description(third_choice)
    fourth_item = get_item_description(fourth_choice)
    fifth_item = get_item_description(fifth_choice)
    return first_item, second_item, third_item, fourth_item, fifth_item

def print_choices(first_item, second_item, third_item, fourth_item, fifth_item):
    """ Print choices made """
    print(f"""\nYou have chosen: 
          1. {first_item}
          2. {second_item}
          3. {third_item}
          4. {fourth_item}
          5. {fifth_item}
        """)
    choice_confirm = input("Are you happy with your choices? y/n \n")
    return choice_confirm

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

def print_score():
    """ Display score """
    if total_score <= 5:
        print(f"""
              Your final score is:
              
              {total_score}
              
              which is Excellent! 
              You have a very good chance of survival!""")
    elif total_score >= 6 and total_score <= 12:
        print(f"""
              Your final score is:
              
              {total_score}
              
              which is Very Good! 
              You have a pretty good chance of survival!""")
    elif total_score >= 13 and total_score <= 20:
        print(f"""
              Your final score is:
              
              {total_score}
              
              which is Good. 
              You have a reasonable chance of survival.""")
    else:
        print(f"""
              Your final score is:
              
              {total_score}
              
              which is Not So Good... 
              You have a pretty low chance of survival based on the items you chose.""")
    print(input("\nWould you like the expert's feedback on your choices? y/n \n"))

# Importing item feedback from worksheet
def expert_feedback():
    """ Get expert's feedback on choices made """
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

def final_choice():
    """ Print final action choice """
    print()
    print(input(f"""Do you want to try again, see the expert's item rankings, or quit?
                Type 't' to try again 
                'e' to see expert rankings
                'q' to quit"""))

def try_again():
    """ Restart game """
    main()

def expert_ranking():
    """ See the expert's ranking of items """
    expert_ranking_table = SHEET.worksheet('expert_rankings').get('A1:B12')
    col_names_expert = ["Expert rank", "Item"]
    print("\nThese are the expert's rankings of the items:\n")
    print(tabulate(expert_ranking_table, headers=col_names_expert, tablefmt="grid"))

def print_thank_you():
    """ Print Final thank you """
    print("\nThank you for visiting the Winter Survival Exercise!\n")

def main():
    """ Functions to run the game """
    print_intro()
    print_scenario()
    items_table()
    item_choices()
    get_item_description(choice)
    match_description_to_choice()
    print_choices()
    print_score()
    expert_feedback()
    final_choice()
    print_thank_you()

# Calling game
main()
