

# def PrintNumbers(sorted_num):
#     for index, num in enumerate(sorted_num):
#         if index + 1 < len(sorted_num):
#             print(str(num) + " ", end="")
#         else:
#             print(str(num))
#
#
#
# def insertionSort(A, N):
#     sorted_num = list(A)
#     PrintNumbers(sorted_num)
#     for i in range(1, N):
#         j = i - 1
#         v = A[i]
#         while j >= 0 and sorted_num[j] > v:
#             sorted_num[j+1] = sorted_num[j]
#             j -= 1
#         sorted_num[j+1] = A[i]
#         PrintNumbers(sorted_num)
#     return sorted_num
#
# size = int(input())
# nums = [int(x) for x in input().split()]
#
# sorted_num = insertionSort(nums, size)


n = int(input())
nums = list(map(int, input().split()))

for i in range(len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key
    print(' '.join(map(str, nums)))