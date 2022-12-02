SCORES_1 = {"A X": 1 + 3,
          "A Y": 2 + 6,
          "A Z": 3 + 0,
          "B X": 1 + 0,
          "B Y": 2 + 3,
          "B Z": 3 + 6,
          "C X": 1 + 6,
          "C Y": 2 + 0,
          "C Z": 3 + 3
          }

SCORES_2 = {"A X": 3 + 0,
          "A Y": 1 + 3,
          "A Z": 2 + 6,
          "B X": 1 + 0,
          "B Y": 2 + 3,
          "B Z": 3 + 6,
          "C X": 2 + 0,
          "C Y": 3 + 3,
          "C Z": 1 + 6
          }

with open("inputs/2.txt") as f:
    games = [i.strip() for i in f.readlines()]
    print(f"part 1: {sum((SCORES_1[game] for game in games))}")
    print(f"part 2: {sum((SCORES_2[game] for game in games))}")
