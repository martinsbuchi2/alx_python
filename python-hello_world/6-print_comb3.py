for num in range(10):
    for next_num in range(num + 1, 10):
        if num != next_num:
            print("{:d}{:d}".format(num, next_num), end=", " if num < 8 else "\n")
