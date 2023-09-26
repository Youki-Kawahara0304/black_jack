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


# shared between player and dealer
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

def check_bust(hand):# class function, add self.count
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

class Dealer_Hand:
    def __init__(self):
        self.hand = [draw_card() for i in range(0, 2)]
        self.soft_17 = False
        self.bust = False
        self.count = 0
        self.count_2 = 0

    def check_17_bust(self):
        sum = 0
        sum_2 = 0
        for card in self.hand:
            if card == "A":
                sum += trump_value[card][0]
                sum_2 += trump_value[card][1]
            else:
                sum += trump_value[card]
                sum_2 += trump_value[card]
        self.count = sum
        self.count_2 = sum_2
        if sum >= 17 and sum <= 21:
            self.soft_17 = True
        elif sum_2 >= 17 and sum_2 <= 21:
            self.soft_17 = True
        elif sum > 21:
            self.bust = True
            print("Dealer bust")

    def compare_hands(self, player_hand): # use player class count attribute
        player_count = 0
        #  trump_value[player_hand[0]]  + trump_value[player_hand[1]]
        for card in player_hand:
            player_count += trump_value[card]
        if self.count_2 > 21:
            if player_count < self.count:
                return True
        else:
            if player_count < self.count or player_count < self.count_2:
                return True
        return False

