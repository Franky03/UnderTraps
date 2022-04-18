import func
from time import sleep
death=False
func.line(42)
print(f"{'Welcome to Under Traps.':^42}")
print(f"{'Your mission is to find the treasure and become a conqueror.':^42}")
func.line(42)

while True:
    try:
        func.line(50)
        choice1= str(input("\nYou are in a dark dungeon and there is only a bridge and a door, the bridge is old and on the other side of the door there are strange sounds, do you want to enter the 'door' or go through the 'bridge'?")).lower()
        if choice1=='door':
            func.line(50)
            choice2=str(input("\nYou opened the door and found a weak and sick griffin, do you want to help him? 'yes' or 'no':")).lower()
            sleep(2)
            if choice2=='yes':
                func.line(50)
                print('The griffon needs to know you first, say your name and class...')
                name= str(input('Say your name: '))
                clas= str(input('Define your class: '))
                txt= 'Character Profile.txt'
                func.cadastrar(txt, name, clas)
                already= func.arquivoExiste(txt)
                if already == False:
                    func.criarArquivo(txt)
                print('You gave the healing potion that was in your backpack to the griffin, he got up and, still weak, recognized your kindness.')
                sleep(4)
                print("You walk around the room looking for exits... wait...")
                sleep(4)
                print("The griffin is walking beside you, he wants to follow you, maybe it's his survival instincts.")
                sleep(4)
                func.line(50)
                choice3= str(input("\nDo you accept having the griffin as your partner? 'yes' or 'no':")).lower()
                if choice3== 'yes':
                    print("Great, the griffin unexpectedly flies you out of the dungeon, maybe that was the only way out, go to LEVEL2!")
                    break
                else:
                    func.line(50)
                    print("You decided to leave the griffin aside and didn't find any way out, go back to the beginning.")
                    sleep(4)
                    print("Now the only way is to cross the bridge, go ahead.")
                    sleep(4)
                    print("Oh no, you're halfway across the bridge when the griffin runs towards you...")
                    sleep(2)
                    print("the bridge breaks!!! you fall and die... GAME OVER!")
                    death=True
                    break
            else:
                print("You leave the griffon aside and go back to the dungeon trying to find another way out... without looking at the ground, you step into a trap, it's very lethal... before you die, say your name and class: ")
                name= str(input('Say your name: '))
                clas= str(input('Define your class: '))
                txt= 'Character Profile.txt'
                func.cadastrar(txt, name, clas)
                already= func.arquivoExiste(txt)
                if already == False:
                    func.criarArquivo(txt)
                sleep(4)
                death=True
                break
        else:
            func.line(50)
            choice2= str(input("You crossed the bridge safely, arrived outside the dungeon and found an elder almost dead, do you wish to help him? 'yes' or 'no':")).lower()
            if choice2=='yes':
                func.line(50)
                print("You gave the healing potion that was in your backpack to the elder, the potion has a better effect on humans, healing all of the elder's wounds.")
                quest1= str(input("The elder asked which city you were from, say the city:")).lower()
                if quest1== 'crifina':
                    print("Elder: Ohh, so you're from crifina, this is my hometown...thanks for the potion... what's your name?")
                    name= str(input('Say your name: '))
                    clas= str(input('Define your class: '))
                    txt= 'Character Profile.txt'
                    func.cadastrar(txt, name, clas)
                    already= func.arquivoExiste(txt)
                    if already == False:
                        func.criarArquivo(txt)
                    print(f"So, {name} of crifina, I am very grateful for your help. I will definitely see you again...bye!")
                    print("You notice that the elder carries a staff with a jewel, but at the moment this does not pique your interest.")
                    sleep(4)
                    print('There in front is the gate to exit the dungeon, go to LEVEL2!')
                    func.conq(txt, 'The elder owes you a favor')
                    break
                else:
                    print(f"Elder: you're from {quest1}, i've heard many stories there, i prefer not to get involved with people of your class, thanks for the potion... what's your name?")
                    name= str(input('Say your name: '))
                    clas= str(input('Define your class: '))
                    txt= 'Character Profile.txt'
                    func.cadastrar(txt, name, clas)
                    already= func.arquivoExiste(txt)
                    if already == False:
                        func.criarArquivo(txt)
                    print(f"From now on, I'll take care of myself, {name}.")
                    sleep(2)
                    print('There in front is the gate to exit the dungeon, go to LEVEL2!')
                    func.conq(txt, 'The elder hates you for your class')
                    break
            else:
                func.line(50)
                print('You left the elder for death, in fact, he is the dungeon mage and for your lack of compassion, you were sentenced to death by the mage!')
                print('Say your name and class before die...')
                name= str(input('Say your name: '))
                clas= str(input('Define your class: '))
                txt= 'Character Profile.txt'
                func.cadastrar(txt, name, clas)
                already= func.arquivoExiste(txt)
                if already == False:
                    func.criarArquivo(txt)
                print("... GAME OVER!")
                death= True
                break
    except:
        print('ERROR! RELOAD THE GAME!')
if not death:
    while True:
        prof= str(input("Do you want to see your profile? 'yes' or 'no': ")).lower()
        if prof=='yes':
            func.lerArquivo(txt)
            break
        elif prof=='no':
            break
        else:
            print('ERROR')
else:
    func.lerArquivo(txt)

#LEVEL 2 NO PANTANO, SOZINHO OU COM GRIFFO

