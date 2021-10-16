import random
import time
from levels import LEVELS


def intro_menu():
    """main menu of game"""
    print("MENU\n"
          "\t1. Play Game\n"
          "\t2. Rules\n"
          "\t3. High Scores\n"
          "\t4. About\n")

    user_choice = input("> ")

    if user_choice == "1":
        level_up(1, 0)
    elif user_choice == "2":
        print("\nRules:\n"
              "\t> Simply type 'higher' or 'lower' for each number generated!\n"
              "\t> Each level has a different possible range of numbers\n"
              "\t> Unused lives roll over to the next level\n"
              "\t> Type 'menu' at any time to return to the menu\n\n")
        intro_menu()
    elif user_choice == "3":
        print("\n\nHigh Scores coming soon\n\n")
        time.sleep(1)
        intro_menu()
    elif user_choice == "4":
        print("\n\nThis game was produced by Alex Kociuba Oct 2021\n\n")
        time.sleep(2)
        intro_menu()
    else:
        print("Invalid option; please type 1-4")
        intro_menu()


def new_number_list(max_number, iterations):
    """create a random list without consecutive duplicate numbers"""
    current_number = [random.randint(1, max_number)]
    while iterations > 0:
        a_list = list(range(1, max_number))
        to_pick_from = [x for x in a_list if x != current_number[-1]]
        new_num = random.choice(to_pick_from)
        current_number.append(new_num)
        iterations -= 1
    return current_number


def level_up(level, life_roll_over):
    """set level hardness parameters - round length, messages, number ranges, life management"""
    if level == 1:
        a_random_list = new_number_list(LEVELS[1]["max number"], LEVELS[1]["iterations"])
        play_game(a_random_list, LEVELS[1]["lives"], 1, LEVELS[1]["message"], 0)

    elif level == 2:
        a_random_list = new_number_list(LEVELS[2]["max number"], LEVELS[2]["iterations"])
        play_game(a_random_list, LEVELS[2]["lives"], 2, LEVELS[2]["message"], life_roll_over)

    elif level == 3:
        a_random_list = new_number_list(LEVELS[3]["max number"], LEVELS[3]["iterations"])
        play_game(a_random_list, LEVELS[3]["lives"], 3, LEVELS[3]["message"], life_roll_over)

    elif level == 4:
        a_random_list = new_number_list(LEVELS[4]["max number"], LEVELS[4]["iterations"])
        play_game(a_random_list, LEVELS[4]["lives"], 4, LEVELS[4]["message"], life_roll_over)


def play_game(numbers, lives, level, message, life_roll_over):
    """the main game; user guesses and number checks"""
    print(message)
    list_length = len(numbers)
    index_count = 0
    current_level = level
    lives += life_roll_over
    print(f"Current lives: {lives}\n")
    while list_length > 1:
        user_guess = input(f"higher or lower than {numbers[index_count]}?: ").lower()
        print(f"the number drawn is {numbers[index_count + 1]}")
        if user_guess == "lower" and numbers[index_count] > numbers[
            index_count + 1] or user_guess == "higher" and \
                numbers[index_count] < numbers[index_count + 1]:
            print("✔️")

        elif user_guess == "menu":
            intro_menu()
        else:
            print("❌")
            lives -= 1

            if lives == 0:
                print(f"\n☠️☠️☠️☠️ NO LIVES LEFT ☠️☠️☠️☠️\n☠☠☠☠☠️ GAME OVER ☠☠☠☠☠\n\n")
                intro_menu()
            print(f"lives remaining {lives}")
        index_count += 1
        list_length -= 1

    else:
        if level == 4:
            print(
                f'\n🤍🤍🤍 You completed the game! 🤍🤍🤍\n')
        else:
            print(f'\nYou have completed level {level}!\nYour lives are rolled over!\n')
            current_level += 1

            time.sleep(0.5)
            print("LOADING")
            time.sleep(0.5)
            print("NEXT")
            time.sleep(0.5)
            print("LEVEL...\n\n\n")
            time.sleep(0.5)
            (level_up(current_level, lives))


# runs the program
intro_menu()
