import random
trump = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
trump_value = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
"10": 10, "J": 10, "Q": 10, "K": 10}
chip_variation = {"1": 5, "2": 10, "3": 25, "4": 50, "5": 100, "6": 500}

def set_game(choosing_spot = False):
    if choosing_spot == True:
        print("""
                    Dealer      
1:Spot1   2:Spot2   3:Spot3   4:Spot4   5:Spot5
""")
        spot_number = choose_spot()
        bet = betting()

def choose_spot():
    finish_choosing = False
    while finish_choosing == False:
        spot_number = input("Enter the number__")
        if int(spot_number) in range(1, 6):
            finish_choosing == True
            return int(spot_number)
        else:
            print("Sorry, Spot{} is not at this table".format(spot_number))

def betting():
    finish_betting = False
    bet = 0
    while finish_betting == False:
        print("Bet:$", bet)
        chip = input("""
1:$5, 2:$10, 3:$25, 4:$50, 5:$100, 6:$500, 7:All-in, 0:Finish betting
Enter the number__""")
        if int(chip) in range(1, 7):
            bet += chip_variation[chip]
        elif int(chip) == 7:
            bet = player_chip
            finish_betting = True
            return bet
        elif int(chip) == 0:
            if bet <= 0:
                print("You can't bet $0")
            else:
                finish_betting = True
                return bet
        else:
            print("Please enter correct number")

def draw_card():
    return random.choice(trump)

def check_black_jack(hand):
    sum = 0
    for card in hand:
        if card == "A":
            sum += trump_value[card][1]
        else:
            sum += trump_value[card]
    if sum == 21:
        return True
    return False