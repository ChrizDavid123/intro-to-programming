## Exercise 2: Glossary :ballot_box_with_check:

#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

#* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line 
# and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

programming_words = {"if statement": "an if statement is used to ask if a code should be executed. If true, the code will be executed. ", 
                     "elif statement": "it is executed if the previous conditions like an if statement or another elif statement is confirmed false. ", 
                     "print()": "the print() is a tool used to execute a variable", 
                     "else statement": "it is executed if all conditions like if statements or elif statements all confirmed false.", 
                     "Variable": "is is a tool that stores data to be used later on in the program"}

print(f"if statement: \n-{programming_words['if statement']} ")
print(f"\nelif statement: \n-{programming_words['elif statement']}")
print(f"\nprint(): \n-{programming_words['print()']}")
print(f"\nelse statement: \n-{programming_words['else statement']}")
print(f"\nvariable: \n-{programming_words['Variable']}")

