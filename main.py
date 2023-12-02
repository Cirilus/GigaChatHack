n, k = map(int, input().split())

left = -1
right = k + 1
middle = -1
while right - left > 1:
    middle = (left + right) // 2
    if middle * (middle - 1) / 2 > k:
        right = middle
    else:
        left = middle

if right * (right - 1) // 2 != k:
    full = left
else:
    full = right

ans = []
for t in range(full, 0, -1):
    ans.append(t)

if full == n:
    print(*ans)
else:
    t = full - k + full * (full - 1) // 2
    ans = ans[:t] + [full + 1] + ans[t:]

    for q in range(full + 2, n + 1):
        ans.append(q)

    print(*ans)

