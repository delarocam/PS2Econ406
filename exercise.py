"""This Document is for completing functions to solve short exercise problems,
related to game theory, and basic computations"""

# 2:
# a.)


def prisoners_dilemma() -> int:
    """This function returns outcomes for a
    normal form game: prisoners dilemma"""
    playera = input("player A: Defect or Cooperate?")
    playerb = input("player B: Defect or Cooperate?")
    rounds = 1
    while playera != playerb:
        if playera == "Defect" and playerb == "Cooperate":
            print("A:0, B:-20")
            playera = input("player A: Defect or Cooperate?")
            playerb = input("player B: Defect or Cooperate?")
            rounds = rounds + 1
        elif playera == "Cooperate" and playerb == "Defect":
            print("A:-20, B:0")
            playera = input("player A: Defect or Cooperate?")
            playerb = input("player B: Defect or Cooperate?")
            rounds = rounds + 1
    if playera == "Defect" and playerb == "Defect":
        print("A:-10, B:-10")
    elif playera == "Cooperate" and playerb == "Cooperate":
        print("A:-3, B:-3")
    else:
        print("invalid input")
    print("Rounds:" + str(rounds))
    return rounds

# test: uncomment to run


# prisoners_dilemma()

# b.)


def factorial(n_arg: int) -> int:
    """will return n! factorial of any integer inputs"""
    factor = 1
    for i in range(1, n_arg + 1):
        factor = i * factor
    print(factor)
    return factor

# test: uncomment to run


# factorial(10)
# factorial(9)
# factorial(5)


word_list = ["sklearn", "AI", "data analysis", "Caffe", "AI", "sklearn", "AI",
             "Computational Economics", "Tensorflow", "sklearn", "Keras",
             "data science", "numpy", "amazon aws server", "AI"]

# c.)


def compute_frequency(words: str) -> dict:
    """This function returns the frequency of all words in a list"""
    dictionary = {}
    for i in words:
        tally = 0
        for j in words:
            if i == j:
                tally = tally + 1
            else:
                tally = tally + 0
        dictionary[i] = tally
    print(dictionary)    
    return dictionary

# test: uncomment to run


# compute_frequency(word_list)
