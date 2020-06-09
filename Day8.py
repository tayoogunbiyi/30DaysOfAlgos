def is_at_origin(moves):
    x, y = 0, 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        else:
            x -= 1

    return x == 0 and y == 0
