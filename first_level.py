from extra import *

def start_room_first():
    print("\nSTART ROOM")
    print(space)

    print("You wake up in a room.")
    print("There is a giant compass signal on the floor.")
    print("There is one door toward the east.")
    print("Which direction do you walk?")
    while True:

        choice = input('> ')
        choice.lower()

        if choice == 'walk north' or choice =='north':
            print(f"You walk into the {choice} wall. How very constructive of you.")


        elif choice == 'walk south' or choice == 'south':
            print(f"You walk into the {choice} wall. How very constructive of you.")


        elif choice == 'walk west' or choice == 'west':
            print(f"You walk into the {choice} wall. How very constructive of you.")

        elif choice == 'walk east' or choice == 'east':
            chest_room()

        elif True:
            print(f"I don't understand your statement.")


def chest_room():
    print("\nCHEST ROOM")
    print(space)
    print("You enter a room with four doors. There is a chest at the center.")
    map = False

    while True:
        choice = input('> ')
        choice.lower()

        if choice == 'walk north' or choice == 'north':
            print("As you push the door open you hear a click behind you.")
            print("As you turn around to investigate, you see a cannon drop from the ceiling.")
            print("BOOOM! You fly backwards through the door with a cannon shaped hole in your belly.")
            dead("You recieved a cannon ball to the belly.")

        elif choice == 'walk south' or choice == 'south':
            print("The door opens to a deep chasm.")
            print("You trip on a bump in the floor and fall out the door.")
            dead("You fell down a chasm.")

        elif choice == 'walk west' or choice == 'west':
            print("You walk back toward the door you entered and try to open it.")
            print("Curiously it appears to have locked behind you.")
            print("I guess you will just have to continue.")

        elif choice == 'walk east' or choice == 'east':
            print("You walk through the door on the east.")
            dance_party(map)

        elif (choice == 'open chest' or choice == 'chest') and map == False:
            print("You walk up to the chest and open it. It squeals loudly as it opens.")
            print("You find a map in the chest.")
            print(map_pic)
            map = True


        elif (choice == 'open chest' or choice == 'chest') and map == True:
            print("You've already opened this...")

        else:
            pass


def dance_party(map):
    print("\nDANCE PARTY")
    print(space)
    print("You enter into large open room with tiles on every surface.")
    print("The room is curiously empty...")
    print("There is a door on the east side.")

    while True:
        choice = input('> ')
        choice.lower()

        if choice == 'follow map' and map == True:
            print("You follow the map and arrive at the door.")
            troll_lair()

        elif choice == 'follow map' and map == False:
            print("You don't have a map.")

        elif choice == 'walk east' or choice == 'east':
            print("As you walk to the door, the tile you step on sinks slightly.")
            print("A giant blade drops from the ceiling and chops you in half.")
            dead("Chopped by a giant blade.")

        elif choice == 'walk north' or choice == 'north':
            print(f"You walk toward the north side.")
            print("A giant blade drops from the ceiling and chops you in half.")
            dead("Chopped by a giant blade.")

        elif choice == 'walk south' or choice == 'south':
            print(f"You walk toward the south side.")
            print("A giant blade drops from the ceiling and chops you in half.")
            dead("Chopped by a giant blade.")

        elif choice == 'walk west' or choice == 'west':
            print("You walk back toward the door you entered and try to open it.")
            print("Curiously it appears to have locked behind you.")
            print("I guess you will just have to continue.")

        else:
            print("I don't understand that...")


def troll_lair():
    print("\nTROLL LAIR")
    print(space)
    print("There is huge troll in the middle of the room.")
    print("He turns and looks at you angrily.")
    print("What do you do?")
    while True:
        choice = input('> ')
        choice.lower()

        if choice == 'walk north' or choice == 'north':
            print("You bump into the north wall.")

        elif choice == 'walk south' or choice == 'south':
            print("You bump into the south wall.")

        elif choice == 'walk west' or choice == 'west':
            print("You walk west toward the door you just entered and try to open it.")
            print("Curiously it appears to have locked behind you.")
            print("I guess you will just have to continue.")

        elif choice == 'walk east' or choice == 'east':
            print("You walk directly at the Troll.")
            print("It is less than amused and whacks you.")
            dead('Killed by a angry Troll.')

        elif choice == 'fight troll' or choice == 'fight':
            print("You walk up to the troll to challenge it.")
            print("A sword appears in your hand.")
            fight_troll()


def fight_troll():
    print("Which part of the troll do you aim for?")
    print("Options: Head, Arm, Belly, Leg, Feet")

    rip = 0
    while True:

        choice = input('> ')
        choice.lower()

        if choice == 'head':
            print("Your attack fails.")
            print("The troll swings at you from the right.")
            troll_dodge('left')

        elif choice == 'arm':
            print("Your attack fails.")
            print("The troll swings at you from the left")
            troll_dodge('right')

        elif choice == 'belly':
            print("Your attack fails.")
            print("The troll swings directly at you with both hands.")
            troll_dodge('back')

        elif choice == 'feet':
            print("Your attack succeeds!")
            print("The troll jumps around and goes and hides in a corner.\n")
            print("You walk to the door on the west and open it.")
            print("It slides open smoothly and silently.")
            end()

        elif choice == 'leg':
            print("Your attack fails.")
            print("The troll swings directly at you with both hands.")
            troll_dodge('back')

        elif rip == 3:
            print("The troll gets tired of looking at you and whacks your head off.")
            dead('Depacitated by an angry Troll.')

        else:
            print("The troll does nothing but he looks like he might attack you soon.")
            rip += 1


def troll_dodge(direction_attack):

    choice = input('> ')
    choice.lower()

    if choice == 'dodge right' and direction_attack == 'right':
        print(f"You dodge {direction_attack} correctly.")
        fight_troll()

    elif choice == 'dodge left' and direction_attack == 'left':
        print(f"You dodge {direction_attack} correctly.")
        fight_troll()

    elif choice == 'dodge back' and direction_attack == 'back':
        print(f"You dodge {direction_attack} correctly.")
        fight_troll()

    else:
        print("You dodge badly.")
        dead("The Troll attacked you.")


def end():
    print("END ROOM\n")
    print(space)
    print("Yay you won the first level.")
    second_unlocked = True
    

troll_lair()
