n = int(input())
nums = list(map(int, input().split()))
nums.sort()
k = 0
days = 0

for num in nums:
    if num > k:
        k += 1
        days += 1

print(days)
