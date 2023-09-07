# Import packages for the programme
import sys
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

def authenticate_gspread():
    """ Set authentication parameters """
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    return GSPREAD_CLIENT.open('winter-survival-game-content')

def print_intro():
    """ Print intro """
    intro = authenticate_gspread().worksheet('data').acell('A2').value
    print(intro)
    input("Press Enter to proceed\n")

def print_scenario():
    """ Print_scenario """
    scenario = authenticate_gspread().worksheet('data').acell('B2').value
    print(scenario)
    input("Are you ready to select your items? y/n \n")

def select_items():
    """ Import items from spreadsheet """
    SHEET = authenticate_gspread()
    data = SHEET.worksheet('data').get('B5:C16')
    col_names = ["Item no.", "Item"]
    print(tabulate(data, headers=col_names, tablefmt="grid"))

def get_user_choices():
    """ Get user item choices """
    first_choice = input("\nWhich item would be your first choice? 1-12?\n")
    second_choice = input("Which item would be your second choice? 1-12?\n")
    third_choice = input("Which item would be your third choice? 1-12?\n")
    fourth_choice = input("Which item would be your fourth choice? 1-12?\n")
    fifth_choice = input("Which item would be your fifth choice? 1-12?\n")
    return first_choice, second_choice, third_choice, fourth_choice, fifth_choice

def get_item_description(choice, item_descriptions):
    """ Get description of items chosen """
    return item_descriptions.get(choice, "")

# !!! Not currently working !!!
def calculate_score(choices, expert_view):
    """ Calculate scores based on user choice and expert ranking """
    score = 0
    for i, choice in enumerate(choices, 1):
        matching_expert_key = None
        for key, value in expert_view.items():
            if value == choice:
                matching_expert_key = key
                break
        if matching_expert_key is not None:
            score += abs(matching_expert_key - i)
    return score

def display_score(score):
    """ Display final score """
    if score <= 5:
        return "Excellent! You have a very good chance of survival!"
    elif 6 <= score <= 12:
        return "Very Good! You have a pretty good chance of survival!"
    elif 13 <= score <= 20:
        return "Good. You have a reasonable chance of survival."
    else:
        return "Not So Good... You have a pretty low chance of survival based on the items chosen."

def get_feedback(SHEET, choices):
    " Import expert feedback for items chosen "
    feedback = []
    for choice in choices:
        feedback.append(SHEET.worksheet("feedback").cell(int(choice), 2).value)
    return feedback

def main():
    """ Run programme """
    print_intro()

    print_scenario()

    select_items()

    first_choice, second_choice, third_choice, fourth_choice, fifth_choice = get_user_choices()

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

    choices = [first_choice, second_choice, third_choice, fourth_choice, fifth_choice]

    print(f"\nYou have chosen:\n")
    for i, choice in enumerate(choices, 1):
        item_description = get_item_description(choice, item_descriptions)
        print(f"{i}. {item_description}")

    choice_confirm = input("\nAre you happy with your choices? y/n \n")

    total_score = calculate_score(choices, expert_view)

    print(f"\nYour final score is:\n\n{total_score}\n\nwhich is {display_score(total_score)}\n")

    feedback_choice = input("Would you like to see the survival expert's feedback on the items you chose? y/n \n")

    if feedback_choice.lower() == 'y':
        feedback = get_feedback(authenticate_gspread(), choices)
        print("\nThe expert's view on your choices were:\n")
        for i, (choice, item_feedback) in enumerate(zip(choices, feedback), 1):
            item_description = get_item_description(choice, item_descriptions)
            print(f"{i}. {item_description}:\n{item_feedback}\n")

    print("Do you want to try again, see the expert's item rankings, or quit?")
    choice = input("Type 't' to try again/ 'e' to see expert rankings/ 'q' to quit\n")

    if choice == 'e':
        expert_ranking_table = authenticate_gspread().worksheet("expert_rankings").get('A1:B12')
        col_names_expert = ["Expert rank", "Item"]
        print("\nThese are the expert's rankings of the items:\n")
        print(tabulate(expert_ranking_table, headers=col_names_expert, tablefmt="grid"))

    print("\nThank you for visiting the Winter Survival Exercise!\n")

if __name__ == "__main__":
    main()
