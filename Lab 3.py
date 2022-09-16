# welcome message for user and game
print("Welcome to the Flaresheim Guesser!\n")
print(" ")

#variables need for game
#three_rem = 0
#five_rem = 0
#seven_rem = 0
play_again = "Y"

# create a while loop from the beginning of the game
# keep running while loop until user quits game (n/N)
while(play_again == "Y" or play_again == "y"):
    print("Please think of a number between and including 1 and 100.")
    print(" ")

# variables for remainders 3, 5, 7
    three_rem = 0
    five_rem = 0
    seven_rem = 0

# remainder three, use while loop and if elif statements to give errors if number is too low or high
    three_rem = int(input("What is the remainder when your number is divided by 3 ? "))
    while(three_rem < 0 or three_rem > 3):
        if three_rem < 0:
            print("The value entered must be 0 or greater")
        elif three_rem > 3:
            print("The value entered must less than 3")
        three_rem = int(input("What is the remainder when your number is divided by 3? "))
    print(" ")

# remainder five, use while loop and if elif statements to give errors if number is too low or high
    five_rem = int(input("What is the remainder when your number is divided by 5 ? "))
    while(five_rem < 0 or five_rem > 5):
        if five_rem < 0:
            print("The value entered must be 0 or greater")
        elif five_rem > 5:
            print("The value entered must be less than 5")
        five_rem = int(input("What is the remainder when your number is divided by 5? "))
    print(" ")

# remainder seven while loop with if elif statements
    seven_rem = int(input("What is the remainder when your number is divided by 7 ? "))
    while(seven_rem < 0 or seven_rem > 7):
        if seven_rem < 0:
            print("The value entered must be 0 or greater")
        elif seven_rem > 7:
            print("The value entered must be less than 7")
        seven_rem = int(input("What is the remainder when your number is divided by 7? "))
    print(" ")

# use for loop to calculate and output number
    for i in range(1, 101):
        if i%3 == three_rem and i%5 == five_rem and i%7 == seven_rem:
            print(f'You number was {i}')
            print("How amazing was that?")
            print(" ")
    
# ask user to play again using while loop
    play_again = input("Do you want to play again? Y to continue, N to quit ==> ")
    while (play_again != "Y" and play_again != "y" and play_again != "N" and play_again != "n"):
        play_again = input("Do you want to play again? Y to continue, N to quit ==> ")
