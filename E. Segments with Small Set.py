from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))
sets = 0
left = 0 
unique_count = 0
dd = defaultdict(int)
for right in range(n):
  dd[nums[right]] += 1
  if dd[nums[right]] == 1:
        unique_count += 1
  while unique_count > k:
    dd[nums[left]] -= 1
    if dd[nums[left]] == 0:
            unique_count -= 1
    left += 1
  sets += right-left+1
print(sets)
