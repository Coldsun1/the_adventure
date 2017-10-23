# The ADVENTURE!!!
from sys import exit
from first_level import *


""" # Broken for now
def start_game():
    death_count = 0
    first_unlocked = True
    second_unlocked = False
    third_unlocked = False
    
    print("If you want to LEAVE the game at any point, press: CTRL-C.")
    print("Which level do you wish to play?")
    print("Level status: ")
    print(f"First Unlocked? {first_unlocked}")
    print(f"Second Unlocked? {second_unlocked}")
    print(f"Third Unlocked? {third_unlocked}")


    while True:
        if second_unlocked == True:
            break

        elif third_unlocked == True:
            break

        else:
            pass

        choice = input('> ')
        choice.lower()

        if choice == 'first' and first_unlocked == True:
            start_room_first()

        elif choice == 'second' and second_unlocked == True:
            start_room_second()

        elif choice == 'third' and third_unlocked == True:
            start_room_third()

        else:
            print("I don't understand...")
"""
start_level_first()
