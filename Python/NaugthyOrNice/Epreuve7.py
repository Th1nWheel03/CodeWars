def naughty_or_nice(data):
    compteur_naughty = sum(1 for month in data.values() for value in month.values() if value == 'Naughty')
    compteur_nice = sum(1 for month in data.values() for value in month.values() if value == 'Nice')

    if compteur_naughty > compteur_nice:
        return "Naughty!"
    elif compteur_naughty < compteur_nice:
        return "Nice!"
    else:
        return "Nice!"

data = {
    "January" : {
        '1': 'Naughty', '2': 'Naughty', '3': 'Nice'
    },
    "February": {
        '1': 'Nice', '2': 'Naughty', '3': 'Nice'
    },
    "December": {
        '1': 'Nice', '2': 'Nice', '3': 'Naughty'
    }
}

print(naughty_or_nice(data))