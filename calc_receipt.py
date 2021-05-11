# Write a Python program which will keep adding a stream of numbers input by the user. The adding stops as soon as user presses q key on the keyboard.

sum = 0

while(True):
    userInput = input("Enter the item price or press 'q' to quit: ")
    if(userInput != 'q'):
        sum += float(userInput)
        print(f"Order total so far: {sum}")

    else:
        print("Thanks for using our calculator")
        print(f"Your Bill total is {sum}. Thanks for shopping with us")
        break



# Sriram Verma Stores
#   1. 5
#   2. 10
#   3. 20
#   4. 26