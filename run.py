# Import packages for the programme
import sys
import os
from tabulate import tabulate
import keyboard
import threading
import intro_module
import scenario_module
import constants
import feedback

def check_for_esc():
    while True:
        if keyboard.is_pressed('esc'):
            print("Thank you for visiting the Winter Survival experience, now exiting...")
            os._exit(1)
exit_thread = threading.Thread(target = check_for_esc)
exit_thread.start()

def print_intro():
    """ Print intro """
    print(intro_module.intro_text)
    input("Press Enter to proceed\n")

def print_scenario():
    """ Print_scenario """
    print(scenario_module.scenario_text)
    input("Press Enter to select your items\n")

def select_items():
    """ Import items from constants module """
    data = constants.item_list
    col_names = ["Item no.", "Item"]
    print(tabulate(data, headers=col_names, tablefmt="grid"))

def get_user_choices():
    """ Get user item choices """
    choices = []
    for i in range(1, 6):
        while True:
            try:
                choice = int(input(f"Which item would be your choice number {i}? 1-12?\n"))
                if choice < 1 or choice > 12:
                    print(f"ERROR! You entered {choice}, which is not between 1 and 12. Please enter a number between 1 and 12!")
                    continue
                elif choice in choices:
                    print(f"ERROR! You entered {choice}, which has already been used. Please enter a new number.")
                    continue
                choices.append(choice)
                break
            except ValueError:
                print("ERROR! Please enter a number between 1 and 12!\n")
    return tuple(choices)

def get_item_description(choice, item_descriptions):
    """ Get description of items chosen """
    return item_descriptions.get(choice, "")

feedback = feedback.feedback_dict
def get_item_feedback(choice, feedback):
    """ Get feedback for items chosen """
    return feedback.get(choice, "")

def calculate_score(choices, expert_view, item_descriptions):
    """ Calculate scores based on user choice and expert ranking """
    score = 0
    for i, choice in enumerate(choices, 1):
        matching_expert_key = 0
        item_description = item_descriptions.get(int(choice), "")
        for key, value in expert_view.items():
            if value == item_description:
                matching_expert_key = key
                break
        if matching_expert_key != 0:
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

def finish():
    """ End of exercise """
    print("\nThank you for visiting the Winter Survival Exercise!\n")

#------------------------------------------------------

def main():
    """ Run programme """

    print_intro()

    print_scenario()

    select_items()

    first_choice, second_choice, third_choice, fourth_choice, fifth_choice = get_user_choices()

    choices = [int(first_choice), int(second_choice), int(third_choice), int(fourth_choice), int(fifth_choice)]
    first_choice = int(first_choice)
    second_choice = int(second_choice)
    third_choice = int(third_choice)
    fourth_choice = int(fourth_choice)
    fifth_choice = int(fifth_choice)

    print(f"\nYou have chosen:\n")
    for i, choice in enumerate(choices, 1):
        item_description = get_item_description(choice, constants.item_descriptions)
        print(f"{i}. {item_description}")

    choice_confirm = input("\nAre you happy with your choices? y/n \n")

    if choice_confirm.lower() == 'y':
        calculate_score(choices, constants.expert_view, constants.item_descriptions)
    elif choice_confirm.lower() == 'n':
        print(f"""
              ---------------------------------
              Please make your final selection:
              ---------------------------------
              """)
        select_items()
        first_choice, second_choice, third_choice, fourth_choice, fifth_choice = get_user_choices()
        choices = [int(first_choice), int(second_choice), int(third_choice), int(fourth_choice), int(fifth_choice)]

        print(f"\nYou have chosen:\n")
        for i, choice in enumerate(choices, 1):
            item_description = get_item_description(choice, constants.item_descriptions)
            print(f"{i}. {item_description}")

        choice_confirm = input("\nPress Enter to see your score! \n")
    else:
        print("Please enter 'y' for yes or 'n' to see the items again")

    total_score = calculate_score(choices, constants.expert_view, constants.item_descriptions)

    print(f"\nYour final score is:\n\n{total_score}\n\nwhich is {display_score(total_score)}\n")

    feedback_choice = input("Would you like to see the survival expert's feedback on the items you chose? y/n \n")

    if feedback_choice.lower() == 'y':
        print("\nThe expert's feedback for your choices were:\n")
        for i, choice in enumerate(choices, 1):
            item_feedback = get_item_feedback(choice, feedback)
            print(f"{i}. {item_feedback}")

    elif feedback_choice.lower() == 'n':
        print("")
    else:
        print("\nERROR! Please enter 'y' for yes or 'n' for no.\n")

    while True:
        print("Do you want to try again, see the expert's item rankings, or quit?\n")
        choice = input("-Type 't' to try again/ 'e' to see expert rankings/ 'q' to quit\n")
        if choice.lower() == 'e':
            expert_ranking_table = constants.expert_list
            col_names_expert = ["Expert rank", "Item"]
            print("\nThese are the expert's rankings of the items:\n")
            print(tabulate(expert_ranking_table, headers=col_names_expert, tablefmt="grid"))
            break
        elif choice.lower() == 't':
            main()
            break
        elif choice.lower() == 'q':
            while True:
                clean_terminal = input("Do you want to clean the terminal window on exit? y/n\n")
                if clean_terminal.lower() == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    os._exit(1)
                elif clean_terminal.lower() == 'n':
                    print("\nThank you for visiting the Winter Survival Exercise!\n")
                    os._exit(1)
                else:
                    print("Please enter 'y' for yes or 'n' for no.\n")
        else: 
            print("\nERROR! Please enter 't' to try again, 'e' to see the expert's rankings, or 'q' to quit.\n")
            choice = input("-Type 't' to try again/ 'e' to see expert rankings/ 'q' to quit\n")

    while True:
        clean_terminal = input("Do you want to clean the terminal window on exit? y/n\n")
        if clean_terminal.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            os._exit(1)
        elif clean_terminal.lower() == 'n':
            print("\nThank you for visiting the Winter Survival Exercise!\n")
            os._exit(1)
        else:
            print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
    main()
