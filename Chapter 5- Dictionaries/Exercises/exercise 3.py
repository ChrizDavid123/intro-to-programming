## Exercise 3: Glossary 2 :ballot_box_with_check:
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs 
#through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

programming_words = {"if statement": "an if statement is used to ask if a code should be executed. If true, the code will be executed. ", 
                     "elif statement": "it is executed if the previous conditions like an if statement or another elif statement is confirmed false. ", 
                     "print()": "the print() is a tool used to execute a variable", 
                     "else statement": "it is executed if all conditions like if statements or elif statements all confirmed false.", 
                     "Variable": "is is a tool that stores data to be used later on in the program", 
                     "input()": "the input is used for the user to interect and type in", 
                     "while": "its used to continously print a statement as long as the condition is true", 
                     "break": "its used to stop a loop from continuing", 
                     "list": "its used to store different items and words in a variable", 
                     "Boolean": "it is a data type that represents two values of true or false"}


for words, definition in programming_words.items():
    print(f"{words}: \n{definition} \n")

# source: ChatGPT prompt: how to do code forloop to print every single item in the dictionary?