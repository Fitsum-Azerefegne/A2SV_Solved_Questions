from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().strip().split()))
left = 0
dd = defaultdict(int)
max_length = 0
a = 0
b = 0
for right in range(n):
  dd[arr[right]] += 1
  while len(dd) > k:
    dd[arr[left]] -= 1
    if dd[arr[left]] == 0:
      del dd[arr[left]]
    left += 1
  if right - left + 1 > max_length:
    a = left + 1
    b = right + 1
    max_length = right - left + 1
print(a , b)