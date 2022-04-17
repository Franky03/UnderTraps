import func
from time import sleep

print("Welcome to Under Traps.")
print("Your mission is to find the treasure and become a conqueror.")

while True:
    try:
        func.line(60)
        choice1= str(input("\nYou are in a dark dungeon and there is only a bridge and a door, the bridge is old and on the other side of the door there are strange sounds, do you want to enter the 'door' or go through the 'bridge'?")).lower()
        if choice1=='door':
            func.line(60)
            choice2=str(input("\nYou opened the door and found a weak and sick griffin, do you want to help him? 'yes' or 'no':")).lower()
            sleep(2)
            if choice2=='yes':
                func.line(60)
                print('You gave the healing potion that was in your backpack to the griffin, he got up and, still weak, recognized your kindness.')
                sleep(4)
                print("You walk around the room looking for exits... wait...")
                sleep(4)
                print("The griffin is walking beside you, he wants to follow you, maybe it's his survival instincts.")
                sleep(4)
                func.line(60)
                choice3= str(input("\nDo you accept having the griffin as your partner? 'yes' or 'no':")).lower()
                if choice3== 'yes':
                    print("Great, the griffin unexpectedly flies you out of the dungeon, maybe that was the only way out.")
                    break
                else:
                    func.line(60)
                    print("You decided to leave the griffin aside and didn't find any way out, go back to the beginning.")
                    sleep(4)
                    print("Now the only way is to cross the bridge, go ahead.")
                    sleep(4)
                    print("Oh no, you're halfway across the bridge when the griffin runs towards you...")
                    sleep(2)
                    print("the bridge breaks!!! you fall and die... GAME OVER!")
                    break
            else:
                print("You leave the griffon aside and go back to the dungeon trying to find another way out... without looking at the ground, you step into a trap, it's very lethal... you die... GAME OVER")
                sleep(4)
                break
        else:
            func.line(60)
            choice2= str(input("you crossed the bridge safely, arrived outside the dungeon and found an elder almost dead, do you wish to help him? 'yes' or 'no':")).lower()
    except:
        print('ERROR! RELOAD THE GAME!')