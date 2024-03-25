TIME_PER_NON_RED = 13
TIME_PER_RED = 16

num_test_cases = 10

for _ in range(num_test_cases):
    colors_count = {
        'orange': 0,
        'blue': 0,
        'green': 0,
        'yellow': 0,
        'pink': 0,
        'violet': 0,
        'brown': 0,
        'red': 0
    }
    
    while True:
        color = input().strip()
        if color == 'end of box':
            break
        colors_count[color] += 1
        
        total_time = 0
        for color, count in colors_count.items():
            if color == 'red':
                total_time += count * TIME_PER_RED
            else:
                num_handfuls, remainder = divmod(count, 7)
                total_time += (num_handfuls * TIME_PER_NON_RED)
                if remainder != 0:
                    total_time += (TIME_PER_NON_RED * remainder/remainder)

    print(int(total_time))
