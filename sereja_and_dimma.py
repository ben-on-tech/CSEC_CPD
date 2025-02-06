n = int(input())
cards = input().strip().split()
cards = list(map(int, cards))
sereja=0
dima =0
turn = 0

while cards:
    if cards[0] > cards[-1]:
        chosen_card = cards.pop(0)
    else:
        chosen_card = cards.pop(-1)

    if turn % 2 == 0:
        sereja += chosen_card
    else:
        dima += chosen_card

    turn += 1

print(f"{sereja} {dima}")


