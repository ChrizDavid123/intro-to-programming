## Exercise 5: USB Shopper :ballot_box_with_check:

# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.

usb_stick_price = 6
balance = 50 

print("one USB stick costs £6")
print("Your balance is", balance)

sticks_for_50 = int(balance / usb_stick_price)
remaining = int(balance % usb_stick_price)

print("You can buy",sticks_for_50,"USB sticks for £",balance)
print("your balance is",remaining)




