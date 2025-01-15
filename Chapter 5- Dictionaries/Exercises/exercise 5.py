## Exercise 5: Pets :ballot_box_with_check:

#Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet

pets = [
    {"Kind": "Dog", 
    "Breed": "Yorkshire", 
     "Owner": "Dave"}, 
    
    {"Kind": "Cat",
    "Breed": "Garfield", 
     "Owner": "Jomari"}, 

    {"Kind": "Bird", 
    "Breed": "Eagle", 
     "Owner": "JR"}, 
]
    
for pet in pets:
    print(f"Type of pet: {pet["Kind"]}\nBreed: {pet["Breed"]}\nOwner: {pet["Owner"]} \n")
