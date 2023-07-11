import random


def roll():
    mini = 1
    maxi = 6
    dice = random.randint(mini, maxi)
    return dice


def player():
    while True:
        players = input("Enter number of players (between 2 and 6): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid")
    return players


def game(player, roll):
    people = player()
    max_score = 10
    score_card = [0 for _ in range(people)]
    while max(score_card) < max_score:
        for i in range(people):
            print("Turn of player", i + 1)
            print("Your score = ", score_card[i])
            curr_score = 0
            inp = input("Roll? Y or N: ")
            if inp.lower() == "y":
                val = roll()
                if val == 1:
                    print("Rolled 1! Turn done")
                    curr_score = 0
                    break
                else:
                    print("Rolled ", val)
                    curr_score = val
                print("Current score = ", curr_score)
                score_card[i] = score_card[i] + curr_score
                print("Player score = ", score_card[i])
            if score_card[i] == max_score:
                break
            break
    max_score = max(score_card)
    win_idx = score_card.index(max_score)
    print("Player number", win_idx + 1, "is the winner with a score of:", max_score)


if __name__ == '__main__':
    game(player, roll)
