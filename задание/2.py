import sys

s = [1, 3, 6, 7, 8, 5]
xm = sys.maxsize
segment = [[0, 0] for _ in range(len(s))]

for i in range(len(s)):
    for ji in range(len(s)):
        if s[i] != -1:
            xm = min(xm, s[i])

    k = 0
    segment[i][k] = xm
    if segment[i][k] == s[i]:
        s[i] = -1

    k = 1
    segment[i][k] = xm + 1
    if segment[i][k] == s[i]:
        s[i] = -1

    xm = sys.maxsize

sorted_segment = sorted(segment, key=lambda x: x[0])

for i in range(len(s)):
    k = 0
    print(f"[{sorted_segment[i][k]}, {sorted_segment[i][k + 1]}]")