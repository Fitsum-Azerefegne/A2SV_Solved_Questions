t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    command = input()
    
   
    pos = x
    time_to_first_zero = -1
    
    for i in range(min(k, n)):  
        if command[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            time_to_first_zero = i + 1
            break
    
    if time_to_first_zero == -1 or time_to_first_zero > k:
        print(0)
        continue
    
    
    zeroes = 1
    
    
    remaining_time = k - time_to_first_zero
    
    if remaining_time == 0:
        print(zeroes)
        continue
    
    # Find the next zero position
    pos = 0
    cycle_length = -1
    
    for i in range(n):
        if command[i % n] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            cycle_length = i + 1
            break
    
    if cycle_length == -1:
        
        print(zeroes)
    else:
        
        zeroes += remaining_time // cycle_length
        print(zeroes)
