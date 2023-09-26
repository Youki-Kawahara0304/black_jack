import class_functions
import main_functions

player_chip = 1000

player_hands = main_functions.set_multiple_hands()
dealer_hand = class_functions.Dealer_Hand()
main_functions.start_a_game(player_hands)
player_chip = main_functions.payout(dealer_hand, player_hands, player_chip)
print(player_chip)