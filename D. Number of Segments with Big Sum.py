n, s = map(int, input().split())
array = list(map(int, input().split()))
left = 0
curr_sum = 0
count = 0

for right in range(n):
  curr_sum += array[right]
  while curr_sum >= s:
        count += (n - right)
        curr_sum -= array[left]
        left += 1
        
print(count)
