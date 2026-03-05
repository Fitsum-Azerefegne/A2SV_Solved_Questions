test_case = int(input())
for _ in range(test_case):
  n = int(input())
  a = input()
  b = input()
  equal_a_b = [False] * n
  zeros = 0
  ones = 0
  
  for i in range(n):
    if a[i] == "1":
      ones += 1
    else:
      zeros += 1
    if zeros == ones:
      equal_a_b[i] = True
    else:
      equal_a_b[i] = False

  flip = 0
  possible = True

  for i in range(n-1,-1,-1):
    current = a[i]
    if flip == 1:
      if current == "0":
        current = "1"
      else:
        current = "0"
    if current == b[i]: 
      continue 
    if equal_a_b[i] == False: 
      possible = False 
      break 
    flip = 1 - flip 
  if possible: 
    print ("YES" )
  else: 
    print ("NO")