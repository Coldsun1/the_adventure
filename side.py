# Do not run this!
"You walk to the south door. It slides open smoothly and silently."
print("You walk to the north door. It screaches as you pull it open.\n")

print("You wake up in a room. There are three doors.")
print("There is a giant compass signal on the floor.")
print("There is one door toward the north, one toward the west, one toward the south.")
print("which door do you enter?")
choice = input("> ")

if choice == "north":
print("You walk to the north door. It screaches as you pull it open.")
chest_room()
else:
exit(0)




print("You enter a room with four doors. There is a chest at the center.")

choice = input("> ")

if choice == "open chest":
print("The chest contains a map.")

elif choice == "":
dance_party()
else:
exit(0)

#----------------------------
while True:
choice = input('> ')
if choice == 'walk north':
print("something.")

elif choice == 'walk south':
print("something.")

elif choice == 'walk west':
print("something.")

elif choice == 'walk east':
print("something.")
#---------------------------

"""





def causeway():
    print("CAUSEWAY\n")
    catfish_pond()

def catfish_pond():
    print("CATFISH POND\n")
    end()

def maze():
    print("MAZE")
    jumping()

def jumping():
    print("JUMPING")
    bat_cave()

def bat_cave():
    print("BAT CAVE")


"""
