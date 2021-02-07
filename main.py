# This is Italian Card Game Scopa
# Scopa rules can be found here https://en.wikipedia.org/wiki/Scopa

import sys
import uipyqt
import scopa
from PyQt5.QtWidgets import *

# how many ### CODE_REVIEW old piontless comment


# this is the main game loop
"""
def run_game():
    while sum_of_all_cards_in_game() != 0:
        for h in range(0, no_of_players):
            play_hand(h)
            # print_status()
            # check_sum_of_cards()

    # if any cards were left on the table, get them to the last person taking cards from the table
    for card in table.copy():
        piles[last_hand_played].append(card)
        table.remove(card)

    print_game_results()
""" ### CODE_REVIEW commented, unused large chunk of code. May become long-lived, reduce readibility and cause confusion


def run_game_with_form():
    app = QApplication(sys.argv)
    sc = scopa.Scopa() ### CODE_REVIEW too short variable name, no context or intent
    ex = uipyqt.ScopaForm(sc) ### CODE_REVIEW too short variable name, no context or intent

    ex.my_move()
    ex.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run_game_with_form()

    # print_status() ### CODE_REVIEW commented, unused code.
    # run_game() ### CODE_REVIEW commented, unused code.
