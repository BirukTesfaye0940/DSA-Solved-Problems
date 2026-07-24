def counting_sort_for_radix(arr, mult):
  n = len(arr)
  count = [0] * 10
  output = [0] * n

  for num in arr:
    digit = (num // mult) % 10
    count[digit] += 1
  
  for i in range(1, 10):
    count[i] += count[i-1]
  
  for i in range(n-1, -1, -1):
    digit = (arr[i] // mult) % 10
    output[count[digit] -1] = arr[i]
    count[digit] -= 1
  return output

def radix_sort(arr):
  max_val = max(arr)
  mult = 1

  while max_val // mult > 0:
    arr = counting_sort_for_radix(arr, mult)
    mult *= 10
  return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]

print(radix_sort(arr))