n = int(input())
nums = list(map(int, input().split()))
nums.sort()
i = (n -1 ) // 2
print(nums[i])
