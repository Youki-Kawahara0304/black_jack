import black_jack_function
player_chip = 1000
player_hands = []

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
        correct_letter = False
        end_setting = input("Enter Y for finishing setting or any other letter for betting another spot")
        if end_setting.upper() == "Y":
            finish_setting = True





set_multiple_hands()
for hand in player_hands:
    print(hand.hand)
    

# black_jack_function.set_game(True)
# player_hand = []
# dealer_hand = []
# for i in range(0, 2):
#     dealer_hand.append(black_jack_function.draw_card())
#     player_hand.append(black_jack_function.draw_card())
# print(dealer_hand[1], " (Dealer) ")
# print(player_hand[0], player_hand[1])
# # check Black_jack, insurance, split
# dealer_black_jack = black_jack_function.check_black_jack(dealer_hand)
# player_black_jack = black_jack_function.check_black_jack(player_hand)
