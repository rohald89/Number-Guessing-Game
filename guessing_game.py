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

Try to guess the random number, can you beat the highscore?! 
""")

def start_game():
    global highscore
    random_number = random.randrange(1, 11)
    tries = 0

    print(f'The current highscore is {highscore}, can you beat that?\nPlease enter a number from 1 to 10')
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
                print("It's higher, try again: ")
                continue
            elif chosen_number > random_number:
                print("It's lower, try again:")
                continue
            elif chosen_number == random_number:
                if highscore > tries:
                    print(f"You set a new highscore!\nIt only took you {tries} tries!\n")
                    highscore = tries
                else:
                    print(f"It took you {tries} tries. Try again to beat the highscore of {highscore}.")
                break
    
    replay = input("Would you like to try again? Y/N ")
    if replay.lower() == 'y':
        start_game()
    else:
        print("Thanks for playing! Cya next time 🙂")

    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()