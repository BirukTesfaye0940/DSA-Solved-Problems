def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # count occurrences
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # prefix sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build output (stable)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output

def radix_sort(arr):
    max_val = max(arr)
    exp = 1  # 1, 10, 100, ...

    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


arr = [170, 45, 75, 90, 802, 24, 2, 66]

print(radix_sort(arr))