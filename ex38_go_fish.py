import random
import collections


def make_new_deck():
    deck = []
    for i in range(0, 52):
        deck.append(i)
        i += 1
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def card_suit(card_number):
    suit_code_options = 'Spades Hearts Diamonds Clubs'.split(' ')
    suit_code = card_number % 4
    return suit_code_options[suit_code]


def card_index_value_convert(card_number, switch):
    card_value_options = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')
    if switch:  # convert from card index value to card value
        card_value = card_number % 13
        return card_value_options[card_value]
    if not switch:  # convert from card value to card index value. shit but it could be one of four.
        z = card_value_options.index(card_number)
        potential_cards = [z + (13 * x) for x in range(0, 4)]
        return potential_cards


def card_id(card_number):
    return card_index_value_convert(card_number, True) + " of " + card_suit(card_number)


def hand_id(cardlist):
    """return card IDs of a list of cards"""
    hand_id_list = []
    for card in cardlist:
        hand_id_list.append(card_id(card))
    return hand_id_list


def deal(deck, hand_list, player, cards_dealt):
    """assigns cards_dealt to hand_list[player] and removes them from deck"""
    new_cards = random.sample(deck, cards_dealt)
    hand_list[player] = new_cards
    for cards in new_cards:
        deck.remove(cards)
    return deck, hand_list


def start_game(num_players):
    """input number of players, outputs player_list, hand_list, and game_deck"""
    game_deck = make_new_deck()
    player_list = []
    hand_list = [None]*num_players
    # print(hand_list)
    for player in range(0, num_players):
        hand_list[player] = [None]
    # print("\nHand list before any assignment is:", end=" ")
    # print(hand_list)
    for player in range(0, num_players):  # assign player_list
        player_list.append("Player " + player.__str__())
    # print("Player list is: ", player_list)
    for player in range(0, num_players):  # assign hands
        # print("\nAssigning values for player {}".format(player))
        game_deck, hand_list = deal(game_deck, hand_list, player, 5)
        # print(f"Hand list is {hand_list}")
        # print(hand_list[player])
        # print(hand_list)
    print(player_list)
    # print(card_value_check(hand_list[0], '2'))
    print(hand_list)
    return game_deck, player_list, hand_list


def card_value_check(cardlist, value):
    """check if a cardlist has a card of that specific value"""
    for card in cardlist:
        if card_index_value_convert(card, True) == value:  # check if the value is in the list
            # print(f"You have a {card_value(card)} which is a {card}!!!! Card value check gotcha")
            return True
    return False


def turn(game_deck, player_list, hand_list, current_player):
    """prompt for another player and a card value. perform card value check. if true, grab card and go again
    if false, deal 1 card from deck check deck to see i9f no cards left. """
    z = 1
    while z == 1:
        print(hand_list)
        print("Player {}, your hand is: {}".format(current_player, hand_id(hand_list[current_player])))
        card_looking = str(input("What card are you looking for?\n>"))
        player_looking = int(input("Who are you trying to steal it from?\n>"))
        if card_value_check(hand_list[player_looking], card_looking):  # if they have the card
            card_steal(hand_list, current_player, player_looking, card_looking)
            if four_of_a_kind_check(hand_list[current_player]):
                pass
            else:
                pass
        else:  # GO FISH
            print("Nope, they don't have that card. Go fish!")
            input("> ")
            go_fish(game_deck, hand_list, current_player)
            if four_of_a_kind_check(hand_list[current_player]):
                pass
            else:
                pass
            z = 2
            # draw a card from the game deck
    print("Player {}, your hand is: {}".format(current_player, hand_list[current_player]))


def card_steal(hand_list, current_player, player_looking, card_looking):
    print("You just got SNIPED for a {}".format(card_looking))
    print("Therefore have the following cards: {}"
          .format(card_index_value_convert(card_looking, False)))  # you have these card indices in your hand
    for potential_card_index in card_index_value_convert(card_looking, False):  # remove from hand
        if potential_card_index in hand_list[player_looking]:
            found_card = potential_card_index
            hand_list[player_looking].remove(found_card)
            hand_list[current_player].append(found_card)
            print(hand_list)
            break
        else:
            continue
    return hand_list


def go_fish(game_deck, hand_list, current_player):
    new_card = random.sample(game_deck, 1)[0]
    game_deck.remove(new_card)
    hand_list[current_player].append(new_card)
    print(f"You drew a {card_id(new_card)}")
    return hand_list


def four_of_a_kind_check(cardlist):
    """check if a cardlist has four of a kind"""
    card_value_list = []
    for item in cardlist:   # determine card values for cards in cardlist and put into card_value_list
        card_value_list.append(card_index_value_convert(item, True))  # convert index to value
    counter = collections.Counter(card_value_list)  # count occurrences of each key
    for key in counter.keys():
        if counter[key] == 4:  # key is the value that appears 4 times
            four_card_list = card_index_value_convert(key, False)
            print("Bitch, you got four {}'s!!".format(key))
            for card in four_card_list:
                print(card)
                print(cardlist)
                cardlist.remove(card)
            print("Done removing cards")
            print(cardlist)
            return cardlist
        else:
            pass
    return False  # four of a kind if it's true

    # print(game_deck)

#
# deck1 = make_new_deck()
# print(card_id(5))
# #
# print(deck1)
# #
# for card in deck1:
#     print("Your card is", card_id(deck1[card]))

# hand_list1 = [[None]]
# deal(deck1, hand_list1, 0, 5)
# print(hand_list1)


# hand1 = [0, 13, 26, 39]
#
# # print(hand_id(hand1))
# print(four_of_a_kind_check(hand1))


global_deck, global_player_list, global_hand_list = start_game(5)
# print(global_deck)
# # print(global_player_list)
# global_deck = [0, 4, 5, 12, 14, 17, 18, 20, 22, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 40, 42, 43, 44,
#   45, 47, 48, 49]
# global_hand_list = [[1], [15, 28, 41, 2], [25, 30, 20, 42, 34], [2, 26, 23, 50, 35], [43, 4, 8, 40, 22]]

turn(global_deck, global_player_list, global_hand_list, 0)

print("Done")
