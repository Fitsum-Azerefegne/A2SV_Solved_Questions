test_case = int(input())
for _ in range(test_case):
  n = int(input())
  array = list(map(int, input().split()))
  output = []
  output.append(array[0])
  for i in range(1, n-1):
     if (array[i] - array[i - 1]) * (array[i + 1] - array[i]) < 0:
        output.append(array[i])
  output.append(array[-1])
  print(len(output))
  print(*output)
