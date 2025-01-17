## Exercise 5: No Pastrami :ballot_box_with_check:

#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Ham sandwich", "Tuna sandwich", "Chicken Sandwich", "Cheese sandwich", "Pastrami Sandwich", "Pastrami Sandwich", "Pastrami Sandwich"]
finished_sandwiches = []

while "Pastrami Sandwich" in sandwich_orders: 
    sandwich_orders.remove("Pastrami Sandwich")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}!")
    finished_sandwiches.append(sandwich)

print("The deli has run out of pastrami!")

print("\nThe sandwiches that are made are: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

print("\nEnjoy your meal!")