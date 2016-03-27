n = int(input())
nums = list(map(int, input().split()))

def BubbleSort(A):
    count = 0
    for i in range(0, len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j-1]:
                count += 1
                A[j], A[j-1] = A[j-1], A[j]
    return count

count = BubbleSort(nums)
print(" ".join(map(str, nums)))
print(count)
