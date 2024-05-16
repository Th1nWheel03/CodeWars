def check_freq(x):
    return {c: x.count(c) for c in set(x)}

print(check_freq(''))