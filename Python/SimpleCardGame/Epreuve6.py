def winner(deck_Steve, deck_Josh):
    deck = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    Steve = 0
    Josh = 0
    for i in range(len(deck_Steve)):
        if deck.index(deck_Steve[i]) > deck.index(deck_Josh[i]):
            Steve += 1
        elif deck.index(deck_Steve[i]) < deck.index(deck_Josh[i]):
            Josh += 1
        else:
            continue
    if Steve > Josh:
        return f"Steve wins {Steve} to {Josh}"
    elif Josh > Steve:
        return f"Josh wins {Josh} to {Steve}"
    else:
        return "Tie"

print(winner(["A", "7", "8"], ["K", "5", "9"]))