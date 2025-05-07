print("You are exploring a rainforest in search of treasure. ")
print("Legend has it that there are some buried on a nearby island.")
print("                                                     ")
one = input("You come across a lake.Do you want to swim across, or wait for a boat? (swim/wait):")
if one == "wait":
    print("You wait for a boat and arrive at the island safely")
elif one == "swim":
   print("You get eaten by a hungry shark.")
   print("GAME OVER!")
   exit()

else:
    print("That is not an option! Are you trying to cheat the system?!")
    print("GAME OVER!")
    exit()
print("                                                       ")
two = input("You come to a cave.Do you want to venture inside or walk on? (venture/walk):")
if two == "venture":
    print("You are squished by boulders never to be seen again.")
    print("GAME OVER!")
    exit()
elif two == "walk":
    print("You walk past the cave safely.")
else:
    print("That is not an option! Are you trying to cheat the system?!")
    exit()
print("                                                   ")
three = input ("You decide to stop for a rest, there is soe colourful fruit hanging on the treee beside you, you are hungry. Do you want to eat it or walk on?(eat/walk):")
if three == "eat":
    print("You eat the fruit, it is poisonous. You die")
    print("GAME OVER!")
    exit()
elif three == "walk":
    print("You ignore the fruit and walk on.")
else:
    print("That is not an option! Are you trying to cheat the system?!")
    exit()
print("                                                       ")
four = input ("You arrive at crossroads, you can go either left right or middle. Which path do you take?(left/right/middle):")
if four == "left":
    print("You are trampled by a herd of wildebeest.")
    print("GAME OVER!")
    exit()
elif four == "right":
    print("You get stung by a poisonous wasp.")
    print("GAME OVER!")
    exit()
elif four == "middle":
    print("You march on and find the buried treasure! Yippee!!")
    print("Congratulations, you completed the journey succesfully")
    print("GAME END")
