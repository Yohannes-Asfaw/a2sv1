def gradingStudents(grades):
    x = []
    y = grades[1:]
    for y in grades:
        if y < 38:
            x.append(y)
        else:
            z = (y // 5) * 5 + 5
            if z - y < 3:
                x.append(z)
            else:
                x.append(y)
    return x
