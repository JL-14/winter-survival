"""Imported modules."""
import os

from tabulate import tabulate
from colorama import Fore, Style

from constants import *


def print_intro():
    """
    Print intro in a clean terminal.
    Require enter-press to proceed.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(INTRO_TEXT)
    input(f"""
{Fore.YELLOW}Press Enter to begin the exercise{Style.RESET_ALL}
        """)


def print_scenario():
    """
    Print_scenario.
    Require enter-press to see and select items.
    """
    print(SCENARIO_TEXT)
    input(f"""
    {Fore.YELLOW}Press Enter to see how the exercise
    is scored\n{Style.RESET_ALL}
    """)


def score_method():
    """
    Print scoring method.
    Require enter-press to proceed.
    """
    print(SCORE_TEXT)
    input(
        f"""
{Fore.YELLOW}Press Enter to see and select your items\n{Style.RESET_ALL}
        """
        )


def select_items():
    """
    Import items from constants module.
    Create table of items.
    """
    data = item_list
    col_names = ["Item no.", "Item"]
    print(tabulate(data, headers=col_names, tablefmt="grid"))


def get_user_choices():
    """
    Get user item choices.
    Add validation for incorrect data entries.
    """
    choices = []
    for item in range(1, 6):
        while True:
            try:
                choice = int(
                    input(
                        f"""
{Fore.YELLOW}{item}. Which item would you rank as number {item}?
Please type an item number between 1 and 12?{Style.RESET_ALL}
                        """
                    )
                )
                if choice < 1 or choice > 12:
                    print(
                        f"""
{Fore.RED}ERROR! You entered {choice}, which is not between 1 and 12.
Please enter a number between 1 and 12!{Style.RESET_ALL}
                        """
                        )
                    continue
                elif choice in choices:
                    print(
                        f"""
{Fore.RED}ERROR! You entered {choice}, which has already been used.
Please enter a new number.{Style.RESET_ALL}
                        """
                        )
                    continue
                choices.append(choice)
                break
            except ValueError:
                print(
                    f"""
{Fore.RED}ERROR! Your entry is not valid.
Please enter a number between 1 and 12!{Style.RESET_ALL}
                    """
                    )
    return tuple(choices)


def get_item_description(choice, item_descriptions):
    """Get description of items chosen."""
    return item_descriptions.get(choice, "")


def get_item_feedback(choice, feedback_dict):
    """Get expert feedback for items chosen."""
    return feedback_dict.get(choice, "")


def calculate_score(choices, expert_view, item_descriptions):
    """Calculate scores based on user choice and expert ranking."""
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
    """Display final score."""
    if score <= 5:
        return """
        Excellent!
You have a very good chance of survival!
        """
    elif 6 <= score <= 12:
        return """
        Very Good!
You have a pretty good chance of survival!
        """
    elif 13 <= score <= 20:
        return """
        OK...
You have a reasonable chance of survival with these items.
        """
    else:
        return """
        Poor...
You have a pretty low chance of survival based on these items alone.
        """


def clean_terminal():
    """Function to clean the terminal window when required."""
    os.system('cls' if os.name == 'nt' else 'clear')


def finish():
    """End of exercise."""
    print("\nThank you for visiting the Winter Survival Exercise!\n")


def main():
    """Run required functions for exercise."""
    print_intro()
    print_scenario()
    score_method()
    select_items()

    # Assign function get_user_choices to choices made
    (first_choice,
        second_choice,
        third_choice,
        fourth_choice,
        fifth_choice) = get_user_choices()

    # Create list of integers for choices made
    choices = (
        [
            int(first_choice),
            int(second_choice),
            int(third_choice),
            int(fourth_choice),
            int(fifth_choice)
        ]
    )

    print("\nYou have chosen:\n")
    # Loop to match item description to choice number
    for i, choice in enumerate(choices, 1):
        item_description = get_item_description(choice, item_descriptions)
        print(f"{i}. {item_description}")

    while True:
        choice_confirm = input(
            f"""
{Fore.YELLOW}Are you happy with your choices? y/n {Style.RESET_ALL}
            """
        )
    # Routing and Validation of choices made, confirmation of choices
        if choice_confirm.lower() == 'y':
            calculate_score(choices, expert_view, item_descriptions)
            break
        elif choice_confirm.lower() == 'n':
            print("""

                ---------------------------------
                Please make your final selection:
                ---------------------------------

            """)
            select_items()
            (
                first_choice,
                second_choice,
                third_choice,
                fourth_choice,
                fifth_choice) = get_user_choices()
            choices = (
                [
                    int(first_choice),
                    int(second_choice),
                    int(third_choice),
                    int(fourth_choice),
                    int(fifth_choice)
                ]
            )
            print("\nYou have chosen:\n")
            for i, choice in enumerate(choices, 1):
                item_description = get_item_description(
                    choice,
                    item_descriptions
                    )
                print(f"{i}. {item_description}")
            choice_confirm = input(
                f"""
{Fore.YELLOW}Press Enter to see your score!{Style.RESET_ALL}
                """
            )
            break
        else:
            print(
                f"""
{Fore.RED}ERROR! Please enter 'y' for yes or 'n' to see the items again
{Style.RESET_ALL}
                """
            )

    total_score = calculate_score(choices, expert_view, item_descriptions)

    print(
        f"""
---------------------------------
Your final score is:

        {total_score}

Which is {display_score(total_score)}
---------------------------------
        """)

    while True:
        feedback_choice = input(
            f"""
{Fore.YELLOW}Would you like to see the survival expert
feedback on the items you chose? y/n {Style.RESET_ALL}
            """
        )
    # Routing and validation for displaying expert feedback
        if feedback_choice.lower() == 'y':
            print(
                f"""
{Fore.GREEN}The expert feedback for your choices were:
                """
            )
            for i, choice in enumerate(choices, 1):
                item_feedback = get_item_feedback(choice, feedback_dict)
                print(f"{i}. {item_feedback}")
            break
        elif feedback_choice.lower() == 'n':
            print("")
            break
        else:
            print(
                f"""
{Fore.RED}ERROR! Please enter 'y' for yes or 'n' for no.{Style.RESET_ALL}
                """
            )

    while True:
        print(
            f"""
{Fore.YELLOW}That is the end of the Winter Survival Exercise, well done!!!
Do you want to try again, see the expert item rankings, or quit?
            """
        )
        choice = input(
            f"""
Type:
't' to try again
'e' to see expert rankings
'q' to quit{Style.RESET_ALL}
            """
        )
        if choice.lower() == 'e':
            expert_ranking_table = expert_list
            col_names_expert = ["Expert rank", "Item"]
            print(
                f"""
{Fore.GREEN}These are the expert rankings of the items:
                """
            )
            print(
                tabulate(
                    expert_ranking_table,
                    headers=col_names_expert,
                    tablefmt="grid"
                )
            )
            print(
                f"""
{Style.RESET_ALL}Thank you for visiting the Winter Survival Exercise!
                """
            )
            break
        elif choice.lower() == 't':
            main()
            break
        elif choice.lower() == 'q':
            while True:
                clean_terminal = input(
                    f"""
{Fore.YELLOW}Do you want to clean the terminal window on exit?
y/n{Style.RESET_ALL}
                    """
                )
                if clean_terminal.lower() == 'y':
                    clean_terminal()
                    os._exit(1)
                elif clean_terminal.lower() == 'n':
                    print("""

Thank you for visiting the Winter Survival Exercise!

""")
                    os._exit(1)
                else:
                    print(
                        f"""
{Fore.RED}ERROR! Please enter 'y' for yes or 'n' for no.{Style.RESET_ALL}
                        """
                    )
        else:
            print(
                f"""
{Fore.RED}ERROR! Please enter 't' to try again,
'e' to see the expert rankings,
or 'q' to quit.{Style.RESET_ALL}
                """
            )

# Loop for option to clean terminal on ending game, with validation
    while True:
        clean_terminal = input(
            f"""
{Fore.YELLOW}Do you want to clean the terminal window on exit?
y/n{Style.RESET_ALL}
            """
        )
        if clean_terminal.lower() == 'y':
            # Code to clean terminal from
            # https://stackoverflow.com/questions/517970/
            # how-to-clear-the-interpreter-console
            clean_terminal()
            os._exit(1)
        elif clean_terminal.lower() == 'n':
            print("\nThank you for visiting the Winter Survival Exercise!\n")
            os._exit(1)
        else:
            print(
                f"""
{Fore.RED}ERROR! Please enter 'y' for yes or 'n' for no.{Style.RESET_ALL}
                """
            )


if __name__ == "__main__":
    main()
