""" Imported modules """
import os
from time import sleep
from tabulate import tabulate
from colorama import Fore, Back, Style
from constants import *


def print_intro():
    """ 
        Print intro 
        Require enter-press to proceed 
        """
    print(intro_text)
    input(f"{Fore.YELLOW}Press Enter to begin the exercise\n{Style.RESET_ALL}")

def print_scenario():
    """ 
        Print_scenario 
        Require enter-press to see and select items
        """
    print(scenario_text)
    input(f"{Fore.YELLOW}Press Enter to see how the exercise is scored\n{Style.RESET_ALL}")


def score_method():
    """ 
        Print scoring method
        Require enter-press to proceed 
        """
    print(score_text)
    input(f"{Fore.YELLOW}Press Enter to see and select your items\n{Style.RESET_ALL}")

def select_items():
    """ 
        Import items from constants module 
        Create table of items
        """
    data = item_list
    col_names = ["Item no.", "Item"]
    print(tabulate(data, headers=col_names, tablefmt="grid"))

def get_user_choices():
    """ 
        Get user item choices 
        Add validation for incorrect data entries
        """
    choices = []
    for item in range(1, 6):
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}{item}. Which item would be your choice number {item}? 1-12?\n{Style.RESET_ALL}"))
                if choice < 1 or choice > 12:
                    print(f"""{Fore.RED}
ERROR! You entered {choice}, which is not between 1 and 12. 
Please enter a number between 1 and 12!
{Style.RESET_ALL}""")
                    continue
                elif choice in choices:
                    print(f"""{Fore.RED}
ERROR! You entered {choice}, which has already been used. 
Please enter a new number.
{Style.RESET_ALL}""")
                    continue
                choices.append(choice)
                break
            except ValueError:
                print(f"""{Fore.RED}
ERROR! Your entry is not valid. 
Please enter a number between 1 and 12!
{Style.RESET_ALL}""")
    return tuple(choices)

def get_item_description(choice, item_descriptions):
    """ Get description of items chosen """
    return item_descriptions.get(choice, "")

# feedback = constants.feedback_dict
def get_item_feedback(choice, feedback_dict):
    """ Get expert feedback for items chosen """
    return feedback_dict.get(choice, "")

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
        return f"""Excellent!
You have a very good chance of survival!"""
    elif 6 <= score <= 12:
        return f"""Very Good!
You have a pretty good chance of survival!"""
    elif 13 <= score <= 20:
        return f"""OK...
You have a reasonable chance of survival with these items."""
    else:
        return f"""a Poor score...
You have a pretty low chance of survival based on these items alone."""

def finish():
    """ End of exercise """
    print("\nThank you for visiting the Winter Survival Exercise!\n")

#------------------------------------------------------

def main():
    """ Run programme """
    print_intro()
    print_scenario()
    score_method()
    select_items()

    # Assign function get_user_choices to choices made
    (
    first_choice, 
    second_choice, 
    third_choice, 
    fourth_choice, 
    fifth_choice
    ) = get_user_choices()

    # Create list of integers for choices made
    choices = (
        [int(first_choice), 
         int(second_choice), 
         int(third_choice), 
         int(fourth_choice), 
         int(fifth_choice)]
         )

    print("\nYou have chosen:\n")
    # Loop to match item description to choice number
    for i, choice in enumerate(choices, 1):
        item_description = get_item_description(choice, item_descriptions)
        print(f"{i}. {item_description}")

    while True:
        choice_confirm = input(f"\n{Fore.YELLOW}Are you happy with your choices? y/n {Style.RESET_ALL}\n")
        # Routing and Validation of choices made, and whether user happy with choices
        if choice_confirm.lower() == 'y':
            calculate_score(choices, expert_view, item_descriptions)
            break
        elif choice_confirm.lower() == 'n':
            # Re-displaying table if user wants to choose again
            print("""
                
                ---------------------------------
                Please make your final selection:
                ---------------------------------
                
                """)
            select_items()
            (first_choice, 
             second_choice, 
             third_choice, 
             fourth_choice, 
             fifth_choice) = get_user_choices()
            choices = (
                [int(first_choice),
                int(second_choice), 
                int(third_choice), 
                int(fourth_choice), 
                int(fifth_choice)]
                )
            print("\nYou have chosen:\n")
            for i, choice in enumerate(choices, 1):
                item_description = get_item_description(choice, item_descriptions)
                print(f"{i}. {item_description}")
            choice_confirm = input(f"\n{Fore.YELLOW}Press Enter to see your score!{Style.RESET_ALL}")
            break
        else:
            print(f"""{Fore.RED}
ERROR! Please enter 'y' for yes or 'n' to see the items again
{Style.RESET_ALL}""")

    total_score = calculate_score(choices, expert_view, item_descriptions)

    print(f"""
---------------------------------
Your final score is:
          
        {total_score}
                  
Which is {display_score(total_score)}
---------------------------------
""")

    while True:
        feedback_choice = input(f"""{Fore.YELLOW}Would you like to see the survival expert's 
feedback on the items you chose? y/n {Style.RESET_ALL}\n""")
        # Routing and validation for displaying expert feedback for each item chosen by user
        if feedback_choice.lower() == 'y':
            print(f"\n{Fore.BLUE}The expert's feedback for your choices were:{Style.RESET_ALL}\n")
            for i, choice in enumerate(choices, 1):
                item_feedback = get_item_feedback(choice, feedback_dict)
                print(f"{i}. {item_feedback}")
            break
        elif feedback_choice.lower() == 'n':
            print("")
            break
        else:
            print(f"\n{Fore.RED}ERROR! Please enter 'y' for yes or 'n' for no.{Style.RESET_ALL}\n")

    # Loop with routing and validation for final step: Try again, see expert ranking, or quit
    while True:
        print(f"{Fore.YELLOW}Do you want to try again, see the expert's item rankings, or quit?{Style.RESET_ALL}")
        choice = input(f"{Fore.YELLOW}-Type 't' to try again/ 'e' to see expert rankings/ 'q' to quit{Style.RESET_ALL}\n")
        if choice.lower() == 'e':
            expert_ranking_table = expert_list
            col_names_expert = ["Expert rank", "Item"]
            print(f"{Fore.BLUE}\nThese are the expert's rankings of the items:\n")
            print(tabulate(expert_ranking_table, headers=col_names_expert, tablefmt="grid"))
            break
        elif choice.lower() == 't':
            main()
            break
        elif choice.lower() == 'q':
            # Loop for option to clean terminal on quitting, with validation
            while True:
                clean_terminal = input(f"{Fore.YELLOW}Do you want to clean the terminal window on exit? y/n{Style.RESET_ALL}\n")
                if clean_terminal.lower() == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    os._exit(1)
                elif clean_terminal.lower() == 'n':
                    print("\nThank you for visiting the Winter Survival Exercise!\n")
                    os._exit(1)
                else:
                    print(f"""{Fore.RED}
ERROR! Please enter 'y' for yes or 'n' for no.
{Style.RESET_ALL}""")
        else:
            print(f"""{Fore.RED}
ERROR! Please enter 't' to try again, 'e' to see the expert's rankings, or 'q' to quit.
{Style.RESET_ALL}""")
            print(choice)

    # Loop for option to clean terminal on ending game, with validation
    while True:
        clean_terminal = input(f"{Fore.YELLOW}Do you want to clean the terminal window on exit? y/n{Style.RESET_ALL}\n")
        if clean_terminal.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            os._exit(1)
        elif clean_terminal.lower() == 'n':
            print("\nThank you for visiting the Winter Survival Exercise!\n")
            os._exit(1)
        else:
            print(f"""{Fore.RED}
ERROR! Please enter 'y' for yes or 'n' for no.
{Style.RESET_ALL}""")

if __name__ == "__main__":
    main()
