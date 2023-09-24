import random
trump = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
trump_value = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
"10": 10, "J": 10, "Q": 10, "K": 10}
chip_variation = {"1": 5, "2": 10, "3": 25, "4": 50, "5": 100, "6": 500}

class Hand:
    def __init__(self, spot_number, bet, inheritance = None):
        self.number = spot_number
        self.bet = bet
        if inheritance == None:
            self.hand = [draw_card() for i in range(0, 2)]
        else:
            self.hand = [inheritance, draw_card()]
        self.black_jack = False
        self.insurance = False
        self.split = False
        self.splited_hands = []
        self.bust  = False

    def split_hand(self):
        self.split = True
        for card in self.hand:
            self.splited_hands.append(Hand(self.spot_number, self.bet, card))

    def hit_double(self, double = False):
        self.hand.append(draw_card())
        print(self.hand)
        self.bust = check_bust(self.hand)
        if double == True:
            self.bet = self.bet * 2

def choose_spot():
    finish_choosing = False
    while finish_choosing == False:
        spot_number = input("Enter the number__")
        if int(spot_number) in range(1, 6):
            finish_choosing == True
            return int(spot_number)
        else:
            print("Sorry, Spot{} is not at this table".format(spot_number))

def betting(player_chip):
    finish_betting = False
    limit = player_chip
    bet = 0
    while finish_betting == False:
        print("Bet:$", bet)
        chip = input("""
1:$5, 2:$10, 3:$25, 4:$50, 5:$100, 6:$500, 7:All-in, 
0:Finish betting
Enter the number__""")
        if int(chip) in range(1, 7):
            if limit >= chip_variation[chip]:
                bet += chip_variation[chip]
                limit -= chip_variation[chip]
            else:
                print("You seem not to have enough chip")
        elif int(chip) == 7:
            bet += player_chip
            finish_betting = True
            return bet
        elif int(chip) == 0:
            if bet == 0:
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

def check_bust(hand):
    sum = 0
    for card in hand:
        if card == "A":
            sum += trump_value[card][0]
        else:
            sum += trump_value[card]
    if sum > 21:
        print("Bust")
        return True
    return False
