import random
import time
import copy

# ---------------- Sorting Algorithms ---------------- #

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def quick_sort(arr):

    def partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quick(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick(arr, low, pi - 1)
            quick(arr, pi + 1, high)

    quick(arr, 0, len(arr) - 1)

# ---------------- Input Generator ---------------- #

def generate_array(size, presortedness):
    arr = list(range(size))

    if presortedness == 1:
        return arr  # sorted

    elif presortedness == 0:
        return arr[::-1]  # reverse

    else:
        random.shuffle(arr)
        return arr

# ---------------- Experiment ---------------- #

def run_experiment(start, stop, step, presortedness_values, rep):
    algorithms = {
        "Insertion": insertion_sort,
        "Selection": selection_sort,
        "Merge": merge_sort,
        "Heap": heap_sort,
        "Quick": quick_sort
    }

    for presortedness in presortedness_values:
        print(f"\nPresortedness = {presortedness}")

        for size in range(start, stop+1, step):
            print(f"\nSize = {size}")

            original = generate_array(size, presortedness)

            for name, func in algorithms.items():
                total_time = 0

                for _ in range(rep):
                    arr = copy.deepcopy(original)

                    start_time = time.perf_counter()
                    func(arr)
                    end_time = time.perf_counter()

                    total_time += (end_time - start_time)

                avg_time = total_time / rep

                print(f"{name}: {avg_time:.6f} sec")

run_experiment(
    start=100,
    stop=1000,
    step=100,
    presortedness_values=[0, 0.5, 1],
    rep=5
)