MAX = 200001  
n, k, q = map(int, input().split())
cnt = [0] * (MAX + 2)  
for _ in range(n):
    l, r = map(int, input().split())
    cnt[l] += 1
    cnt[r + 1] -= 1
for i in range(1, MAX):
    cnt[i] += cnt[i - 1]
good = [0] * (MAX + 1)
for i in range(1, MAX):
    if cnt[i] >= k:
        good[i] = 1

pref = [0] * (MAX + 1)
for i in range(1, MAX):
    pref[i] = pref[i - 1] + good[i]
for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a - 1])
