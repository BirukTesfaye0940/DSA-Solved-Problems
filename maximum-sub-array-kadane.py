def kadane(arr):
    max_current = arr[0]  
    max_global = arr[0]    

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global

print(kadane([-2,1,-3,4,-1,2,1,-5,4]))

def kadane_with_array(arr):
    max_current = arr[0]
    max_global = arr[0]
    start = 0
    end = 0
    s = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i] + max_current:
            max_current = arr[i]
            s = i
        else:
            max_current = arr[i] + max_current
        
        if max_current > max_global:
            max_global = max_current
            end = i
            start = s
    return max_global, arr[start:end + 1]

print(kadane_with_array([-2,1,-3,4,-1,2,1,-5,4]))