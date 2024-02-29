def pisano(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    pisano_period = 0
    
    while True:
        previous, current = current, (previous + current) % n
        pisano_period += 1
        
        if previous == 0 and current == 1:
            return pisano_period

print(pisano(5))