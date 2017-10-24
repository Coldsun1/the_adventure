# The ADVENTURE!!!
from sys import exit
death_count = 0
from extra import *
from first_level import *




def start_game(first_unlocked, second_unlocked, third_unlocked, death_count):
    print(f"You've died {death_count} times.")
    print("Which level do you wish to play?")
    print("Level status: ")

    print(f"First Unlocked? {first_unlocked}")
    print(f"Second Unlocked? {second_unlocked}")
    print(f"Third Unlocked? {third_unlocked}")


    while True:

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

print("If you want to LEAVE the game at any point, press: CTRL-C.")

start_game(True, False, False, death_count)
