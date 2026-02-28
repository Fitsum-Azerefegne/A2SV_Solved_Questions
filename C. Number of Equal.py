from collections import defaultdict
n, k = map(int, input().split())
a_values = list(map(int, input().split()))
b_values = list(map(int, input().split()))
num_of_equal = 0
a_dd = defaultdict(int)
for a in a_values:
  a_dd[a] += 1
b_dd = defaultdict(int)
for b in b_values:
  b_dd[b] += 1
a_values= list(set(a_values))
for num in a_values:
  if num in b_dd:
    num_of_equal += (b_dd[num] * a_dd[num])
print(num_of_equal)
