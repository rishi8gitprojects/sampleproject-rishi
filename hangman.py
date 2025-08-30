HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def count_up_to(n):
    for i in range(n+1):
        yield i


word = "ball"
gen = count_up_to(len(HANGMAN_PICS) -1)

while True:
    guess_aplha = input(">")
    if guess_aplha in word:
        print("correct")
    else:
        try:
            stage = next(gen)
            print(HANGMAN_PICS[stage])
        except StopIteration:
            print('GAME OVER!')
            break
        

