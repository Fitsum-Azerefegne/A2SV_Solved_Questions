test_case = int(input())
for _ in range(test_case):
  n, k = map(int, input().split())
  word = input()
  count = float("inf")
  left = 0
  blacks = 0
  whites = 0
  for right in range(n):
    if word[right] == "B":
      blacks += 1
    else:
      whites += 1
    if blacks == k:
      count = 0
      break
    elif blacks + whites == k:
      count = min(count, whites)
      if word[left] == "B":
        blacks -= 1
      else:
        whites -= 1
      left += 1
  
  print(count)
    
