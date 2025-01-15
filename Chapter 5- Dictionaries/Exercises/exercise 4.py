## Exercise 4: Rivers :ballot_box_with_check:

#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
rivers = {"Nile River": "Egypt", 
          "Yellow River": "China", 
          "Amazon River": "Brazil"}

#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print(f"the {river} runs through {country} \n")

#* Use a loop to print the name of each river included in the dictionary.
for river, country in rivers.items():
    print(f"{river} \n")

#* Use a loop to print the name of each country included in the dictionary.
for river, country in rivers.items():
    print(f"{country} \n")