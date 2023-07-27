def fibonacci_sequence(n):
    if n == 0:
        return []
    sequence = [0, 1]
    # initialize the first two numbers of Fibonacci series to be one.
    for i in range(2, n):
        next_fibonacci = sequence[-1] + sequence[-2]
        sequence.append(next_fibonacci)

    return sequence[:n]
  