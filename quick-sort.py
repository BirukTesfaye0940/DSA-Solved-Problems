def partition(arr, low, high):
    pivot = arr[high]  # choose last element
    i = low - 1        # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # sort left part
        quicksort(arr, low, pi - 1)

        # sort right part
        quicksort(arr, pi + 1, high)
    return arr

print(quicksort([1,3,5,4,6,13,10,9,8,15,17], 0, 10))