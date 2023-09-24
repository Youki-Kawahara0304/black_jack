import black_jack_function
player_chip = 1000
player_hands = []
dealer_hand = [black_jack_function.draw_card() for i in range(0, 2)]

def set_multiple_hands():
    finish_setting = False
    spot_already_taken = [False, False, False, False, False]
    while finish_setting == False:
        number_of_spots = 1
        for i in spot_already_taken:
            if i == False:
                print("Spot", number_of_spots, " is available to bet")
                number_of_spots += 1
            else:
                print("Spot", number_of_spots, " is already taken")
                number_of_spots += 1
        spot_number = black_jack_function.choose_spot()
        bet = black_jack_function.betting(player_chip)
        player_hands.append(black_jack_function.Hand(spot_number, bet))
        spot_already_taken[spot_number - 1] = True
        for hand in player_hands:
            print("Spot{} : Bet{}".format(int(hand.number), int(hand.bet)))
        end_setting = input("Enter Y for finishing setting or any other letter for betting another spot__")
        if end_setting.upper() == "Y":
            finish_setting = True

# check Black_jack, insurance, split
def start_a_game(player_hands, insurance_check = True):
    for hand in player_hands:
        print(hand.hand[0], hand.hand[1])
        if black_jack_function.check_black_jack(hand.hand) == True:
            print("Black Jack!")
            hand.black_jack = True
            continue
        elif dealer_hand[0] == "A" and insurance_check == True:
            insurance = input("Insurance? Enter Y for yes, any other letter for no__")
            if insurance.upper() == "Y":
                hand.insurance = True
                continue
        elif hand.hand[0] == hand.hand[1]:
            split = input("Split? Enter Y for yes, any other letter for no__")
            if split.upper() == "Y":
                hand.split_hand()
                start_a_game(hand.splited_hands, False)
                continue
        else:
            main_feature(hand)
            
def main_feature(player_hand, eligibility_for_double = True):
    if eligibility_for_double == True:
        print("1:Hit 2:Double 3:Stand")
    else:
        print("1:Hit 3:Stand")
    decision = input("Enter the number__")
    if int(decision) == 1:
        player_hand.hit_double()
        if player_hand.bust != True:
            main_feature(player_hand)
    elif int(decision) == 2 and eligibility_for_double == True:
        player_hand.hit_double(True)
    elif int(decision) == 3:
        return

set_multiple_hands()
print(dealer_hand[0], " (Dealer) ")
start_a_game(player_hands)

# dealer_black_jack = black_jack_function.check_black_jack(dealer_hand)






    

