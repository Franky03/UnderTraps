print("Welcome to Under Traps.")
print("Your mission is to find the treasure and become a conqueror.")

while True:
    try:
        choice1= str(input("You are in a dark dungeon and there is only a bridge and a door, the bridge is old and on the other side of the door there are strange sounds, do you want to enter the 'door' or go through the 'bridge'?")).lower()
        if choice1=='door':
            choice2=str(input("You opened the door and found a weak and sick griffin, do you want to help him? 'yes' or 'no':")).lower()
            if choice2=='yes':
                print('You gave the healing potion that was in your backpack to the griffin, he got up and, still weak, acknowledged your kindness.')
        else:
            choice2= str(input("you crossed the bridge safely, arrived outside the dungeon and found an elder almost dead, do you wish to help him? 'yes' or 'no':")).lower()
    except:
        print('ERROR! RELOAD THE GAME!')