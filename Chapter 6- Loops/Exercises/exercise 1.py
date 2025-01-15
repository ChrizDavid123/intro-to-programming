## Exercise 1: Pizza Toppings :ballot_box_with_check:

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

# print a message saying you’ll add that topping to their pizza.

print("Hello, welcome to Pizza hot!!!")
print("\nYou can add as many toppings as you want on your pizza, but make sure to type quit to end the program.\n")

while True:
    toppings = input("what toppings would you like to add on your pizza?: ")

    if toppings.lower() == "quit":
        print("Thank you for your order!")
        break

    else:
        print(f"Adding {toppings} to your pizza!")

# Source: ChatGPT prompt: how to stop the code from going into an infinite loop. 