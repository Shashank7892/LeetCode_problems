# Missing number in array
# EasyAccuracy: 29.59%Submissions: 1MPoints: 2
# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

# Example 1:

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4
# Example 2:

# Input:
# N = 10
# A[] = {6,1,2,8,3,4,7,10,5}
# Output: 9


def missingNumber(n,array):
        # code here
    total_sum = n * (n + 1) // 2
    array_sum = sum(array)
    missing_number = total_sum - array_sum
    return missing_number

N1 = 5
A1 = [1, 2, 3, 5]
print(missingNumber(N1, A1))
