def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Step 1: Count frequencies
    for num in arr:
        count[num] += 1

    # Step 2: Prefix sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 3: Build output
    output = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num] - 1] = num
        count[num] -= 1

    return output

print(counting_sort([1,4,1,2,7,5,2]))