def read_input(input_path="input.txt"):
    f = open(input_path)
    input_cards = f.read().split('\n\n')
    player1_deck = [int(x) for x in input_cards[0].split("\n")[1:]]
    player2_deck = [int(x) for x in input_cards[1].split("\n")[1:]]
    f.close()
    return player1_deck, player2_deck


def part1(player1_deck, player2_deck):
    while player1_deck and player2_deck:
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        if player1_card > player2_card:
            player1_deck.append(player1_card)
            player1_deck.append(player2_card)
        else:
            player2_deck.append(player2_card)
            player2_deck.append(player1_card)
    return calculate_score(player1_deck) if player1_deck else calculate_score(player2_deck)


def recursive_combat(player1_deck, player2_deck):
    seen_player1 = set()
    seen_player2 = set()
    while player1_deck and player2_deck:
        if tuple(player1_deck) in seen_player1 and tuple(player2_deck) in seen_player2:
            return False
        seen_player1.add(tuple(player1_deck))
        seen_player2.add(tuple(player2_deck))
        card1 = player1_deck.pop(0)
        card2 = player2_deck.pop(0)
        if card1 <= len(player1_deck) and card2 <= len(player2_deck):
            player2_wins = recursive_combat(player1_deck[:card1], player2_deck[:card2])
        else:
            player2_wins = card1 < card2
        if player2_wins:
            player2_deck.append(card2)
            player2_deck.append(card1)
        else:
            player1_deck.append(card1)
            player1_deck.append(card2)
    return not player1_deck


def calculate_score(deck):
    score = 0
    for i, card in enumerate(reversed(deck)):
        score = score + ((i + 1) * card)
    return score


def part2(player1_deck, player2_deck):
    recursive_combat(player1_deck, player2_deck)
    winner = player1_deck or player2_deck
    return calculate_score(winner)


if __name__ == '__main__':
    player1_cards, player2_cards = read_input()
    print(part1(player1_cards.copy(), player2_cards.copy()))
    print(part2(player1_cards, player2_cards))
