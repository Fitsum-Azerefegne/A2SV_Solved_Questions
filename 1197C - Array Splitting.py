n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 1:
    print(arr[-1] - arr[0])
else:
    gaps = [arr[i+1] - arr[i] for i in range(n-1)]
    gaps.sort(reverse=True)
    print(arr[-1] - arr[0] - sum(gaps[:k-1]))
