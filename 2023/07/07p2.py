input = []
result = 0

with open('input.txt', 'r') as file:
    for line in file:
        hand, value = line.strip().split()
        input.append([hand, int(value)])


def card_value(card):
    values = {
        'T': 10,
        'J': 1,
        'Q': 11,
        'K': 12,
        'A': 13
    }
    return int(card) if card.isnumeric() else values[card]


def with_jokers(f):
    def wrapper(hand):
        if 1 not in hand:
            return f(hand)

        result = 0
        for i in range(2, 14):
            copy = hand.copy()
            for j, card in enumerate(copy):
                if card == 1:
                    copy[j] = i
            result = max(result, f(copy))

        return result

    return wrapper


@with_jokers
def hand_value(hand):
    """
    hand is expected as list of integers
    returns 1 for high card, 2 for one pair, 3 for two pairs, and so on
    """
    ln = len(set(hand))
    if ln == 5:                          # high card
        return 1
    if ln == 4:                          # one pair
        return 2
    if ln == 3:                          # 2 pairs or 3oak
        hand.sort()
        for i in range(3):
            if hand[i] == hand[i + 2]:   # 3oak
                return 4
        return 3                         # 2 pairs
    if ln == 2:                          # full house or 4oak
        hand.sort()
        for i in range(2):
            if hand[i] == hand[i + 3]:   # 4oak
                return 6
        return 5                         # full house
    if ln == 1:                          # 5oak
        return 7
    else:
        raise ValueError('wrong hand')


def first_card_value(hand):
    """
    hand is expected as list of integers
    returns a number like 10**8 * 1st card + 10**6 * 2nd card, etc.
    """
    result = 0
    for i, card in enumerate(hand):
        result += 10 ** (-2 * i + 8) * card
    return result


for i in input:
    i.append([card_value(c) for c in list(i[0])])

input.sort(key=lambda x: first_card_value(x[2]))
input.sort(key=lambda x: hand_value(x[2]))

for i, hand in enumerate(input):
    result += (i + 1) * hand[1]

print(result)
