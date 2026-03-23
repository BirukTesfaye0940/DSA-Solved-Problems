def max_subarray(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_sum = max_subarray(arr, low, mid)
    right_sum = max_subarray(arr, mid + 1, high)
    cross_sum = max_crossing(arr, low, mid, high)

    return max(left_sum, right_sum, cross_sum)

def max_crossing(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0

    for i in range(mid, low - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0

    for j in range(mid + 1, high + 1):
        total += arr[j]
        right_sum = max(right_sum, total)

    return left_sum + right_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4], 0, 8))