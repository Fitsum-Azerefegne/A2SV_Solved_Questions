test_case = int(input())
for _ in range(test_case):
  written = input()
  if len(written) == 1:
    print(written)
  else:
    output = ""
    point_1 = 0
    point_2 = 1
    while point_2 < len(written):
            if written[point_1] == written[point_2]:
                point_1 += 2
                point_2 += 2
            else:
                output += written[point_1]
                point_1 += 1
                point_2 += 1
    if point_1 < len(written):
      output += written[point_1]        
    output = sorted(output)
    output = list(set(output))
    print("".join(output))
