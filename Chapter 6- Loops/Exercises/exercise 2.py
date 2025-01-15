## Exercise 2: Movie Tickets: :ballot_box_with_check:

# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; 
# if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

print("Hello welcome to Vox cinemas!")

print("\nUnder 3 = free")
print("Between 3 and 12 = $10")
print("Over 12 = $15 ")

while True:
    ticket = int(input("\nHow old are you?: "))

    if ticket <= 3:
        print("your ticket costs $0(FREE)")

    elif ticket <= 12:
        print("your ticket costs $10")

    elif ticket >= 13:
        print("your ticket costs $15")

    else:
        print("Sorry, invalid response")