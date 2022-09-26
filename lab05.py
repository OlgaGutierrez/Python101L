########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again()->bool:
    play = input("Do you want to play again? ==> ") .lower()
    options = ["n", "y", "no", "yes"]

    if play not in options:
        print("n/You must enter Y/YES/N/N to continue. PLease try again")
        return play_again()

    if (play=="yes" or play=="y"):
        return True
    return False

def get_wager(bank:int)->int:
    chips = int(input("How many chips do you want to wager? ==>"))
    if(chips <1):
        print("The wager amount must be greater than 0. Please enter again.")
        return get_wager(bank)
    elif (chips>bank):
        print("The wager amount cannont be greater than how much you have.",bank)
        return get_wager(bank)
    return chips

def get_slot_results() -> tuple:
    reel1 = random.randint(0, 10)
    reel2 = random.randint(0, 10)
    reel3 = random.randint(0, 10)
    return reel1, reel2, reel3

def get_matches (reela, reelb, reelc)-> int:
    if (reela==reelb==reelc):
        return 3
    elif (reela == reelb or reela==reelc or reelb==reelc):
        return 2
    return 0

def get_bank()-> int:
    chips = int(input("How many chips do you want to start with? ==>"))
    if (chips<1):
        print("Too low a value, you can only choose 1 - 100 chips")
        return get_bank()
    elif (chips>100):
        print("Too high a value, you can only choose 1 - 100 chips")
        return get_bank()
    return chips

def get_payout(wager,matches):
    if matches == 3:
        return wager*10
    elif matches ==2:
        return wager*3
    return wager*-1

if __name__=="__main__":
    playing = True
    while playing:
        bank = get_bank()
        start_chips = bank
        most = bank
        count = 0
        while True:
            wager = get_wager(bank)
            reel1,reel2,reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank+payout
            print("Your spin", reel1, reel2, reel3)
            print("YOu matched", matches, "reels")
            print("You win/lost", payout)
            print("Current bank", bank)
            print()
            count = count+1
            if most<bank:
                most = bank
            if bank<1:
                break
        print("You lost all" ,start_chips, "in" ,count, "spins")
        print("The most chips you had was",most)
        playing = play_again()
ram
