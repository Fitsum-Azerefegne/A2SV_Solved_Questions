matrix = []
for i in range(5):
    row =list(map(int, input().split()))
    matrix.append(row)
column = 1
row = 1
found = False
for r in range(5):
    for c in range(5):
      if matrix[r][c]  == 1:
         column += c
         row += r
         found = True
         break
    if found:
       break
output = abs(column -3) + abs(row - 3)
print(output)
