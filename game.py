black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_blue = "\033[0;94m"
bright_red = "\033[0;91m"
bright_yellow = "\033[0;93m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
import curses
import os
import sys
def slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		slp(0.01)
	print()
def sp1(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		slp(0.05)
	print()
from time import sleep as slp
from random import randint as r
damage=r(1,60)
slow("Before we start, I just wanted to say thank you to these people: AustinBarlow, IndyRishi, 24shim, DSAMax, and my school account, 24wilkec. Thank you all! Remember to favorite this if you like it! - Wilke000. Also, pls don't report me for saying sub to me on YT @ Wilke000, thx lol")
name = input("What is the name of the main character of this story?\n")
friend = input("What is the name of the main character's friend?\n")
weapon = input("What weapon will you wield on your quest?\n")

# Start Story 
sp1("\nYou awaken in a dark cave. Your friend " + friend + " sits beside you.")
sp1(friend + ": You're finally awake! We have to find a way out of this cave!")
sp1("You grab your " + weapon + " and find a way to exit the cave.")

# Decisions
sp1("There are two paths in front of you that lead into the cave. There is a low rumbling noise that seems to be coming from the room to the left. The room on the right has thousands of bats hanging above, but there is a draft coming through that. That might mean either an exit or a huge opening, you might fall down if it is.")

path = input("Do you go left or right? \n ONLY SAY LEFT OR RIGHT\n")

# Left Path  
if path.lower() == "left":
	sp1("As you slowly make your way down the left path, the rumbling grows louder.")
	sp1("Slightly off the path you see a shimmer as the light from the flame of the torches lining the cave walls reflects off of something metal.")
	sp1("You can stay on the path and head toward the source of the noise, or go investigate the objects off the path.")
	choice = input("Stay on path or investigate? (stay or investigate)")

  # Only happens if player decides to investigate
	if choice.lower() == "investigate":
		sp1("You approach the shiny object and see that it is Kylo Ren's Lightsaber, much more powerful than your weak " + weapon + ". You decide to take it with you.")
		weapon = "Kylo Ren's Lightsaber"
  
  # Happens whether or not player investigates
	sp1("You continue on the path and soon recognize the sound as the snoring of an enormous sleeping dragon!")
	slp(2)
	sp1("The dragon wakes up and blocks your way back to safety with his massive tail. Looks like he wants to fight!")

  # Boss Fight 
	dragon_health = 50

	if weapon == "Kylo Ren's Lightsaber":
		damage = 50
  

	sp1("You attack the dragon with your " + weapon + ".")
	if weapon == "Kylo Ren's Lightsaber":
		dragon_health = dragon_health - damage
	else:
		dragon_health = dragon_health - damage
	slp(2)
	input("Click enter to see if you won!")
	slp(1)
	sp1("Suspense growing...")
	slp(2)
	sp1("You can't take it!")
	slp(5)
	if dragon_health > 0:
		sp1("You were defeated by the dragon in an epic battle.\nYOU LOSE")
		slp(2.5)
	else:
		sp1("You defeat the dragon and claim all the treasure he was guarding!\nYOU WIN")
		slp(2.5)

elif path.lower() == "right":
  sp1("As you walk down the cavern the bats begin to shake their wings. A few steps later they all take off in unison, flying away. You follow them and find yourself at the exit of the cave.")
  sp1("When you get out of the cave, you see you are in a barren land, kind of like a desert.")
  desert = input("Do you want to go forward or back into the cave? (Either type cave or forward)\n")

  if desert.lower() == 'cave':
    sp1("You try to turn around... but when you do 	there isn't anything there! The cave has vanished! You head to the desert")
  else:
    sp1("You go forward.")
    slp(5)
    sp1("After a long walk, you go over a hill and see a village!")
    y= input("Do you go into the village or not?(Say yes or no)")
    if y.lower() == 'yes':
      sp1("You head into the village and were never heard from again. "+slp(2.5)+"YOU FAILED!")
    else:
      sp1("You decide it would be too risky and move along. Suddenly, the landscape changes. You are now in a room with 3 doors. One is "+red+"red"+white+", one is "+yellow+"yellow"+white+", and one is "+green+"green"+white+".")
      life = 'life'
      while life == 'life':
        color = input("What door do you want to go through? (Answer yellow, green, or red)\n\n\n\n")
        if color.lower() == 'green':
          sp1("You go into the green door. WHOOPS! You slip and fall down an actual bottomless pit. You never hit the ground and die from starvation and thirst. YOU FAILED")
          
        elif color.lower() == 'red':
          sp1("You go into the red door and see a huge tiger. It seems to be asleep.")
          tiger = input("Do you wake it up or leave it asleep and try to go around it? (Say leave or around)")
          if tiger.lower() == 'around':
            sp1("You are very heavy and your footsteps are loud. The tiger shifts and you get caught touching it. The tiger kills you. YOU FAILED")
            
          else:
            sp1("You wake the tiger up and it speaks to you.")
            slp(2)
            sp1("Tiger: You are very brave young human. I will allow you to live. The walls around you shift and you return home, safly. You never feel the same again. YOU WIN! Congragulations!")
            life = 'win'
        elif color.lower() == 'yellow':
          sp1("As soon as you open the yellow door, you are blinded by the light. You have found the lost gold of åǎæỮẞỎỂƥȸꭓ! You have looked for this gold all your life, and you finally found it! YOU WON! Now, how do you get out?  You relize that this is no win. You see skeletons of past people who have found the treasure. You die 3 days later of thirst. YOU FAILED.")
          
else:
				  sp1("I'm sorry, try again.")
slow("""Made with Python 3.8.2:

          .?77777777777777$.            
          777..777777777777$+           
         .77    7777777777$$$           
         .777 .7777777777$$$$           
         .7777777777777$$$$$$           
         ..........:77$$$$$$$           
  .77777777777777777$$$$$$$$$.=======.  
 777777777777777777$$$$$$$$$$.========  
7777777777777777$$$$$$$$$$$$$.========= 
77777777777777$$$$$$$$$$$$$$$.========= 
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++: 
 7$$$$$$$.==================++++++++++. 
 .,$$$$$$.================++++++++++~.  
         .=========~.........           
         .=============++++++           
         .===========+++..+++           
         .==========+++.  .++           
          ,=======++++++,,++,           
          ..=====+++++++++=.    
""")
slow('Thanks for playing!')


