def digit_count(n):
    counts = [0] * 10
    place = 1

    while place <= n:
        prefix, right = divmod(n, place)
        left, current = divmod(prefix, 10)
        

        full_count = left * place
        for digit in range(10):
            counts[digit] += full_count
            if digit < current:
                counts[digit] += place
            elif digit == current:
                counts[digit] += right + 1

        counts[0] -= place
        place *= 10

    return counts


print(*digit_count(int(input())))
