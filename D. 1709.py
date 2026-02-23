test_case = int(input())
for _ in range(test_case):
  arr_len = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  minimum_op = 0
  sequence_op = []
  for i in range(arr_len):
    if a[i] > b[i]:
      a[i], b[i] = b[i], a[i]
      minimum_op += 1
      sequence_op.append([3,i+1])
         
  for i in range(arr_len):
    for j in range(arr_len-1):
      if a[j] > a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
        minimum_op += 1
        sequence_op.append([1,j+1])
        a[j], a[i] = a[j], a[i]
  for i in range(arr_len):
    for j in range(arr_len - 1):
      if b[j] > b[j + 1]:
        b[j], b[j + 1] = b[j + 1], b[j]
        sequence_op.append([2,j+1])
        minimum_op += 1
  if minimum_op == 0:
    print(minimum_op)
  else:
    print(minimum_op)
    for op in sequence_op:
        print(*op)
