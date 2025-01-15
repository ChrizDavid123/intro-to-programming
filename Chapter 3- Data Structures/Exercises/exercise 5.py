## Exercise 5: Change Guest List :ballot_box_with_check:

#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.

names = ["Mom", "Dad", "Sister"]

print(f"\nUnfortunately, {names[2]} can't make it to dinner tonight")

replace = names.index("Sister")
names[replace] = "Uncle"

print(f"\n Dear {names[2]} \n I would like to ask if you would come dinner with me and my mom and my dad, its been awhile since i first saw you and i believe this is a great opportunity to reconnect with each other.")

print(f"\nNew guest list: {names}")