## Exercise 4: Deli :ballot_box_with_check:

# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches.Loop through the list of sandwich orders and print a message for each order, 
# such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["Ham sandwich", "Tuna sandwich", "Chicken Sandwich", "Cheese sandwich",]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich}!")
    finished_sandwiches.append(sandwich)

print("\nThe sandwiches that are made are: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")