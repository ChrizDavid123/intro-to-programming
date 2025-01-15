## Exercise 7: Seeing the World :ballot_box_with_check:
# Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Poland", "Japan", "Singapore", "Canada", "Germany"]

#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
print("Original List: ")
print(places)

#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.
print("\nAlphabetical order: ")
print(sorted(places))

#•	 Show that your list is still in its original order by printing it.
print("\nList is still in original order: ")
print(places)

#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("\nReversed alphabetical order using sorted(): ")
print(sorted(places, reverse = True))

#•	 Show that your list is still in its original order by printing it again.
print("\n List is still in original order: ")
print(places)

#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print("\nList is now in a different order: ")
print(places)

#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print("\nBack to original order again")
print(places)

#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print("\nalphabetical order using sort(): ")
print(places)

#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse = True)
print("\nBack to reversed order using sort()")
print(places)