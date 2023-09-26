import class_functions
import main_functions

player_chip = 1000
player_hands = []
choose_spot = True
game_over = False
while game_over == False:    
    player_hands = main_functions.set_multiple_hands()
    dealer_hand = class_functions.Dealer_Hand()
    print(dealer_hand.hand, " Dealer ")
    main_functions.start_a_game(player_hands)
    player_chip = main_functions.payout(dealer_hand, player_hands, player_chip)
    print(player_chip)
    if player_chip == 0:
        game_over  == True
    else:
        next_game = inpit("Please enter any letter or \"E\" for end game__")
        if next_game.upper() == "E":
            game_over = True 
print("Thank you so much for your play")


