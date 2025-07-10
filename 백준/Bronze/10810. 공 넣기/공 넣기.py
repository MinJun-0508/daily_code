N, M = map(int, input().split())
list_N = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        list_N[x] = k

print(*list_N)