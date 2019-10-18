__author__ = 'Les Pounder'

"""
    The lines below import modules of code into our game,
    in particular these import time functions allow us to pause and stop the game,
    and random provides a method of choosing random numbers or characters.
"""
from time import *
from random import *
import os,sys
from art import *

"""
    Simple function that clears the terminal screen
"""
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def title():
    print(text2art('g', font='alpha'))
    print(text2art('e', font='alpha'))
    print(text2art('r', font='alpha'))
    print(text2art('a', font='alpha'))
    print(text2art('l', font='alpha'))
    print(text2art('d', font='alpha'))

def north():
    print ("To go north press n then enter")

def east():
    print ("To go east press e then enter")

def south():
    print ("to go south press s then enter")

def west():
    print ("To go west press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name, earth hero?")
    if input() == "gerald":
        print ("hey gerald whats poppin")
        HP = randint(100,200)
        MP = randint(100,200)
    else:
        HP = randint(10,20)
        MP = randint(10,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["yo", "there is somthing emitting a terrible stench upon this town", "hey", "there has been a terrible smell cast upon this village"]
    npcnamechoice = ["fredrick sr.", "fredrick", "fredrick jr.", "fredrick the third"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to fredrick")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "troll"
    print ("\nSuddenly you hear a roar, and from the shadows you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has %s Health Points" % str(enemyHP))
    print ("Your enemy has %s Magic Points" % str(enemyMP))


"""
    We now use our functions in the game code, we call functions title() and setup() for our character.
"""
clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Welcome to bootleg narnia, %s" % name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(HP))
print ("Your magic skill is" + " " + str(MP))



print ("Would you like to venture out into the land? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You are in your home, extremely drunk because of the previous night with your friend Humphrey, and through your cloudy vision, you see your broken sword sitting upon the fireplace")
    print ("Would you like to take your broken sword? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("broken sword")
        print ("You are now carrying your %s, without knowing where to go" % (weapons[0]))
        print ("Armed with your %s you swing open the door to your home and see a green valley gleaming in the sunshine." % (weapons[0]))
    else:
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, You swing open the door to see a green valley full of opportunity awaiting you.")
else:
    print ("well you must be fun at parties.")
    print ("Game Over")
    sys.exit(0)

print ("In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A villager is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou walk to the river which lies to the east of your home.")
    print ("A villager is in your path and greets you")
elif move == 'w':
    print ("\nYou walk to the field of wild flowers, stopping to take in the beauty")
    print ("A villager is in your path and greets you\n")

villager()
enemy()
sleep(3)

fight = input("Do you wish to fight?" )

if fight == "y":
    print("this is running")
    while HP > 0 or enemyHP > 0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print ("You swing your sword and cause %s damage" % str(hit))
        enemyHP = enemyHP - hit
        print (enemyHP)
        enemyhit = randint(0,5)
        print ("The smelly troll swings a club at you and causes %s damage" % str(enemyhit))
        HP = HP - enemyhit
        print (HP)
    if HP <= 0 :
        print ("congrations you did it")
    elif enemyHP <= 0 :
        print ("you died lol")
else:
    print ("You turn and run away from the smelly troll")