def bucket_sort(arr):
  n = len(arr)
  buckets = [[] for _ in range(n)]

  for num in arr:
    index = int (n * num)
    buckets[index].append(num)
  
  for bucket in buckets:
    bucket.sort()
  
  result = []
  for bucket in buckets:
    result.extend(bucket)
  return result

print(bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.124, 0.999, 0.850, 0.001]))