n = int(input())
nums = list(map(int, input().split()))

def selection_sort(A):
    count = 0
    for i in range(0, len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                mini = j
        if i != mini:
            A[i], A[mini] = A[mini], A[i]
            count += 1
    return count

cnt = selection_sort(nums)
print(" ".join(map(str, nums)))
print(cnt)