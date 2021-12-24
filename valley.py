def countingValleys(steps, path):
    count = 0
    valley = 0
    for i in path:
        if i == 'D':
            count -= 1
        elif i == 'U':
            count += 1
        if count == 0 and i == 'U':
            valley += 1
    return valley
