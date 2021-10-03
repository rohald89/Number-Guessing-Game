import random

highscore = 10

# text art from https://fsymbols.com/text-art/
print(f"""
                    Welcome to the
  
╭━╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╭╮
┃┃╰╮┃┃╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱┃┃
┃╭╮╰╯┣╮╭┳╮╭┫╰━┳━━┳━╮┃┃╱╰╋╮╭┳━━┳━━┳━━┳┳━╮╭━━╮┃┃╱╰╋━━┳╮╭┳━━┫┃
┃┃╰╮┃┃┃┃┃╰╯┃╭╮┃┃━┫╭╯┃┃╭━┫┃┃┃┃━┫━━┫━━╋┫╭╮┫╭╮┃┃┃╭━┫╭╮┃╰╯┃┃━╋╯
┃┃╱┃┃┃╰╯┃┃┃┃╰╯┃┃━┫┃╱┃╰┻━┃╰╯┃┃━╋━━┣━━┃┃┃┃┃╰╯┃┃╰┻━┃╭╮┃┃┃┃┃━╋╮
╰╯╱╰━┻━━┻┻┻┻━━┻━━┻╯╱╰━━━┻━━┻━━┻━━┻━━┻┻╯╰┻━╮┃╰━━━┻╯╰┻┻┻┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
""")

def start_game():
    global highscore
    random_number = random.randrange(1, 11)
    tries = 0

    print(f'The current highscore is {highscore}, can you do better?')
    while True:
        try:
            chosen_number = int(input("> "))
            if chosen_number < 1 or chosen_number > 10:
                print("Please enter a number from 1 and 10")
                continue
        except ValueError:
            print("Oops, something went wrong! Please try again")
            continue
        else:
            tries += 1
            if chosen_number < random_number:
                print("It's higher")
                continue
            elif chosen_number > random_number:
                print("It's lower")
                continue
            elif chosen_number == random_number:
                print(f"You win! It took you {tries} tries")
                if highscore > tries:
                    print("You set a new highscore!")
                    highscore = tries
                break
    
    replay = input("Would you like to try again? Y/N ")
    if replay.lower() == 'y':
        start_game()
    else:
        print("Thanks for playing! Cya next time 🙂")

    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()