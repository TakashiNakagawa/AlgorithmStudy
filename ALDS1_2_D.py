import random

def insertion_sort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v
    return cnt

def generate_random(n):
    g = [1]
    while True:
        v = 3*g[-1] + 1
        if v > n:
            break
        g.append(v)

    return g[::-1]

def shell_sort(A, n):
    cnt = 0
    G = generate_random(n)
    m = len(G)
    # m = 2
    # G = [4, 1]
    for i in range(0, m):
        cnt += insertion_sort(A, n, G[i])
    return  m, G, cnt

n = int(input())
A = []
for val in range(0, n):
    A.append(int(input()))

m, G, cnt = shell_sort(A, n)
print(m)
print(" ".join(map(str, G)))
print(cnt)
print("\n".join(map(str, A)))
