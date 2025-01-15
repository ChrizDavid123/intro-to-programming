## Exercise 3: Alien Colors #3 :ballot_box_with_check:

#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
alien_color = input("What alien color have you shot down? green, yellor or red?: ")

#•	 If the alien is green, print a message that the player earned 5 points.
if alien_color == "green":
    print("Congratulations! You have just earned 5 points!")

#•	 If the alien is yellow, print a message that the player earned 10 points.
elif alien_color == "yellow":
    print("Congratulations! You have just earned 10 points!")

#•	 If the alien is red, print a message that the player earned 15 points.
else:
    print("Congratulations! You have just earned 15 points!")

#•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.