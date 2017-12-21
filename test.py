# SHIT SHIT SHIT I CAN'T GET THIS TO WORK!!1!!!!!
def start_game(one, two, three):
    death = 0
    while True:
        if (one is True) and (two is False) and (three is False):
            death = first_level(death)
            print(f"You have died {death} times")

        elif (one is True) and (two is True) and (three is False):
            second_level(death)
            print(f"You have died {death} times")

        elif (one is True) and (two is True) and (three is True):
            third_level(death)
            print(f"You have died {death} times")

        else:
            pass

def first_level(death):
    print("First Level Unlocked!")
    input()
    death += 1

def second_level(death):
    print("Second Level Unlocked!")
    input()
    death += 1

def third_level(death):
    print("Third Level Unlocked!")
    input()
    death += 1

start_game(True, False, False)

def while_function():
    number = 0
    while True:
        print(number)

        number = add_one(number)

        print(number)

def add_one(number):
    number = number + 1
    return number
