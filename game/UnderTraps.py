import func
from time import sleep
death=False
char= dict()
func.line(42)
print(f"{'Welcome to Under Traps.':^42}")
print(f"{'Your mission is to find the treasure and become a conqueror.':^42}")
func.line(42)

while True:
    try:
        func.line(50)
        while True:
            choice1= str(input("\nYou are in a dark dungeon and there is only a bridge and a door, the bridge is old and on the other side of the door there are strange sounds, do you want to enter the 'door' or go through the 'bridge'? ")).lower().strip()
            if choice1 =='door' or choice1=='bridge':
                break
            else:
                print('ERROR! TYPE A VALID OPTION!')
        if choice1=='door':
            func.line(50)
            while True:
                choice2=str(input("\nYou opened the door and found a weak and sick griffin, do you want to help him? 'yes' or 'no': ")).lower().strip()
                if choice2=='yes' or choice2=='no':
                    break
                else:
                    print('ERROR! TYPE A VALID OPTION!')
            if choice2=='yes':
                func.line(50)
                print('The griffon needs to know you first, say your name and class...')
                name= str(input('Say your name: ')).strip()
                clas= str(input('Define your class: ')).strip()
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
                while True:
                    choice3= str(input("\nDo you accept having the griffin as your partner? 'yes' or 'no':")).lower().strip()
                    if choice3=='yes' or choice3=='no':
                        break
                    else:
                        print('ERROR! TYPE A VALID OPTION!')

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
                name= str(input('Say your name: ')).strip()
                clas= str(input('Define your class: ')).strip()
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
            while True:
                choice2= str(input("You crossed the bridge safely, arrived outside the dungeon and found an elder almost dead, do you wish to help him? 'yes' or 'no': ")).lower().strip()
                if choice2=='yes' or choice2=='no':
                    break
                else:
                    print('ERROR! TYPE A VALID OPTION!')
            if choice2=='yes':
                func.line(50)
                print("You gave the healing potion that was in your backpack to the elder, the potion has a better effect on humans, healing all of the elder's wounds.")
                quest1= str(input("The elder asked which city you were from, say the city:")).lower().strip()
                if quest1== 'crifina':
                    print("Elder: Ohh, so you're from crifina, this is my hometown...thanks for the potion... what's your name?")
                    name= str(input('Say your name: ')).strip()
                    clas= str(input('Define your class: ')).strip()
                    txt= 'Character Profile.txt'
                    func.cadastrar(txt, name, clas)
                    already= func.arquivoExiste(txt)
                    if already == False:
                        func.criarArquivo(txt)
                    print(f"So, {name} of crifina, I am very grateful for your help. I will definitely see you again...bye!")
                    print("You notice that the elder carries a staff with a jewel, but at the moment this does not pique your interest.")
                    sleep(4)
                    print('There in front is the gate to exit the dungeon, go to LEVEL2!')
                    print('The elder owes you a favor')
                    break
                else:
                    print(f"Elder: you're from {quest1}, i've heard many stories there, i prefer not to get involved with people of your class, thanks for the potion... what's your name?")
                    name= str(input('Say your name: ')).strip()
                    clas= str(input('Define your class: ')).strip()
                    txt= 'Character Profile.txt'
                    func.cadastrar(txt, name, clas)
                    already= func.arquivoExiste(txt)
                    if already == False:
                        func.criarArquivo(txt)
                    print(f"From now on, I'll take care of myself, {name}.")
                    sleep(2)
                    print('There in front is the gate to exit the dungeon, go to LEVEL2!')
                    print('The elder hates you for your class')
                    break
            else:
                func.line(50)
                print('You left the elder for death, in fact, he is the dungeon mage and for your lack of compassion, you were sentenced to death by the mage!')
                print('Say your name and class before die...')
                name= str(input('Say your name: ')).strip()
                clas= str(input('Define your class: ')).strip()
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
char['Name']= name
char['Class']= clas
if not death:
    while True:
        prof= str(input("Do you want to see your profile? 'yes' or 'no': ")).lower().strip()
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

if choice1=='door':
    while True:
        func.line()
        print("Leaving the dungeon, you find yourself in a dark and silent swamp, it's as if everything is dead, but you are not alone, your new partner is on your side.\n")
        griffin= str(input("Say a name to your partner: ")).strip()
        char['Griffin']= griffin
        print(f"Nice, from now on he will be called {griffin}.")
        print(f"LOOK, LOOK... {griffin} found a small light far away...")
        while True:
            func.line()
            choice4= str(input("Do you want go there? 'yes' or 'no': ")).lower().strip()
            if choice4=='yes' or choice4=='no':
                break
            else:
                print('ERROR! TYPE A VALID OPTION!')
        if choice4=='yes':
            print("Walking...")
            sleep(3)
            print(f"Getting closer, you see it's a tavern, seems to have few people inside... you need to hide {griffin} so you don't get people's attention.")
            print("Entering the tavern, you only find some old drunks and some templars, ask for information about the lost treasure of the seven kingdoms from the woman at the bar...")
            sleep(5)
            print("Talking", end='')
            sleep(1)
            func.points(5)
            print()
            print("Unfortunately the woman has no information, she said that many people look for the treasure, but no one knows any tips.")
            print("Somebody:  -s",end='')
            sleep(1)
            for c in range(0,4):
                print('h', end='', flush=True)
                sleep(0.5)
            print()
            print("Do you want to get a lot of attention, friend? you shouldn't talk about it in public places.")
            sleep(2)
            print("You turn arround  and see that it is one of the templars, go talk go talk to him, he seems to have information.")
            sleep(1)
            func.points(5)
            print()
            print("Templar: -So you want know about the treasure of the seven kingdoms, not even us templars don't found this crap...")
            print("You said: finding the treasure is very important for my journey.")
            print("Do you have any information about him ?")
            func.points()
            print()
            print("Silence in the tavern")
            func.points()
            print("Partially, said the templar, there's a man who knows more about the treasure, they say he's even seen it... but I don't recommend you talk to him, he's a lunatic.")
            sleep(2)
            print("You asked where to find that man.")
            print("Templar: -Go to Kitana, a town 1.8 miles from here. He explained all the way.")
            sleep(2)
            print("You thanked the templar, took your things, called the griffin and left for Kitana.")
            print("GO TO LEVEL 3!")
            break
        if choice4=='no':
            func.line()
            print("You decided to look for another way through the swamp", end='')
            func.points(5)
            print("You and the griffin stepped on something strange... WAIT... is this thing alive?!")
            sleep(2)
            print("Oh no, this creature is giant...")
            print("The creature swallowed you and the griffin, GAME OVER!!")
            death=True
            break
#FAZER A OPÇÃO DA PONTE E DESENVOLVER A FASE 3
#if choice1=='bridge':