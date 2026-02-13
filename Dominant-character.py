test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    s = input()
    ans = float("inf")
    for i in range(n):
        count_a = count_b = count_c = 0
        for j in range(i, min(i + 7, n)):
            if s[j] ==  "a":
                count_a += 1
            elif s[j] == "b":
                count_b += 1
            else:
                count_c += 1
            if j - i + 1 >= 2 and count_a > count_b and count_a > count_c:
                ans = min(ans,j-i+1)
                break
    if ans == float("inf"):
        print(-1)
    else:
        print (ans)
