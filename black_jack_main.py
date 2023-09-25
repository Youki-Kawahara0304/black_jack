import black_jack_function
player_chip = 1000
player_hands = []
dealer_hand = black_jack_function.Dealer_Hand()

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


def start_a_game(player_hands, insurance_check = True):
    for hand in player_hands:
        print(hand.hand[0], hand.hand[1])
        if black_jack_function.check_black_jack(hand.hand) == True:
            print("Black Jack!")
            hand.black_jack = True
            continue
        elif dealer_hand.hand[0] == "A" and insurance_check == True:
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

def payout(dealer_hand, player_hands, player_chip):
    dealer_hand.check_17_bust()
    for player_hand in player_hands:
        print(player_hand.hand)

        if black_jack_function.check_black_jack(dealer_hand.hand) == True:
            if player_hand.black_jack == True:
                print("Push")
            elif player_hand.split != True:
                if player_hand.insurance == True:
                    print("Dealer Black Jack")
                    Print("Insurance ${}".format(str(player_hand.bet * 1.5))) # take insurance as chip
                else:
                    print("Dealer Black Jack")
                    player_chip -= player_hand.bet
            else:
                payout(dealer_hand, player_hand.splited_hands)    

        elif player_hand.black_jack == True:
            print("You win ${}".format(str(player_hand.bet * 2.5)))
        elif player_hand.split == True:
            payout(dealer_hand, player_hand.splited_hands) 
        elif player_hand.bust == True:
            if dealer_hand.bust == True:
                player_chip -= player_hand.bet # + insurance     
        elif dealer_hand.bust == True:
            print("You win ${}".format(str(player_hand.bet * 2)))

        else:
            if dealer_hand.compare_hands(player_hand.hand) == True:
                player_chip -= player_hand.bet # + insurance
            elif dealer_hand.soft_17 == True and dealer_hand.compare_hands(player_hand.hand) != True :
                print("You win ${}".format(str(player_hand.bet * 2)))
            else:
                dealer_draw = True
                while dealer_draw == True:
                    dealer_hand.hand.append(draw_card())
                    dealer_hand.check_17_bust()
                    print("Dealer draws")
                    print(dealer_hand.hand)
                    if dealer_hand.bust == True:
                        print("You win ${}".format(str(player_hand.bet * 2)))
                        dealer_draw = False
                    elif dealer_hand.compare_hands(player_hand.hand) == True:
                        player_chip -= player_hand.bet # + insurance
                        dealer_draw = False
                    elif dealer_hand.soft_17 == True and dealer_hand.compare_hands(player_hand.hand) != True :
                        print("You win ${}".format(str(player_hand.bet * 2)))
                        dealer_draw = False
    return player_chip            
                    

set_multiple_hands()
print(dealer_hand.hand[0], " (Dealer) ")
start_a_game(player_hands)
print("Dealer hand ", dealer_hand.hand[0], dealer_hand.hand[1])
print(payout(dealer_hand, player_hands, player_chip))
# print("End result")
# def test_func(hands):
#     for hand in hands:
#         if hand.split != True:
#             print(hand.hand)
#             print(hand.bet, "Bet")
#             print(hand.bust, "Bust")
#         else:
#             test_func(hand.splited_hands)
# test_func(player_hands)
