"""This Document is for completing functions to solve short exercise problems,
related to game theory, and basic computations"""

# 2:
# a.)


def prisoners_dilemma() -> str:
    """This function returns outcomes for a
    normal form game: prisoners dilemma"""
    playera = input("player A: Defect or Cooperate?")
    playerb = input("player B: Defect or Cooperate?")
    while playera != playerb:
        if playera == "Defect" and playerb == "Cooperate":
            print("A:0, B:-20")
            playera = input("player A: Defect or Cooperate?")
            playerb = input("player B: Defect or Cooperate?")
        elif playera == "Cooperate" and playerb == "Defect":
            print("A:-20, B:0")
            playera = input("player A: Defect or Cooperate?")
            playerb = input("player B: Defect or Cooperate?")
    else:
        if playera == "Defect" and playerb == "Defect":
            payoff = "A:-10, B:-10"
        elif playera == "Cooperate" and playerb == "Cooperate":
            payoff = "A:-3, B:-3"
    return print(payoff)

# test: uncomment to run
# prisoners_dilemma()

# b.)


def factorial(n_arg: int) -> int:
    factorial = 1
    for i in range(1, n_arg + 1):
        factorial = i * factorial
    return print(factorial)


