## Exercise 2: Alien Colors #2 :ballot_box_with_check:

#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
alien_color = str(input("What alien color have you shot down? green, yellor or red?: "))

#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
if alien_color == "green":
    print("Congratulations! You have just earned 5 points!")

#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
else:
    print("Congratulations! You have just earned 10 points!")

#•Write one version of this program that runs the if block and another that runs the else block.
