# Merge Sort
'''
This file contains all of the 100,000 integers between 1 and 100,000 
(inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, 
where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast 
divide-and-conquer algorithm covered in the video lectures.
The numeric answer for the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space 
provided without any space / commas / any other punctuation marks. You 
can make up to 5 attempts, and we'll use the best one for grading.
(We do not require you to submit your code, so feel free to use any 
programming language you want --- just type the final numeric answer in 
the following space.)
[TIP: before submitting, first test the correctness of your program on 
some small test files or your own devising. Then post your best test 
cases to the discussion forums to help your fellow students!]
'''
def merge_sort(lis):
    length = len(lis)
    if length == 1:
        return lis
    mid = length / 2
    left = merge_sort(lis[0:mid])
    right = merge_sort(lis[mid:])
    sorted_lis = merge(left, right)
    return sorted_lis
    
def merge(left, right):
    i = 0; j = 0; imax = len(left); jmax = len(right)
    sorted_lis = []
    while i < imax and j < jmax:
        if left[i] <= right[j]:
            sorted_lis.append(left[i])
            i += 1
        else:
            sorted_lis.append(right[j])
            j += 1
    sorted_lis += left[i:]
    sorted_lis += right[j:]
    return sorted_lis

# Count inversion
def merge_sort_count(lis):
    length = len(lis)
    if length == 1:
        return (lis, 0)
    mid = length / 2
    (left, left_inv) = merge_sort_count(lis[0:mid])
    (right, right_inv) = merge_sort_count(lis[mid:])
    (sorted_lis, split_inv) = merge_count(left, right)
    return (sorted_lis, left_inv + right_inv + split_inv)
    
def merge_count(left, right):
    i = 0; j = 0; imax = len(left); jmax = len(right)
    sorted_lis = []; inv = 0
    while i < imax and j < jmax:
        if left[i] <= right[j]:
            sorted_lis.append(left[i])
            i += 1
        else:
            sorted_lis.append(right[j])
            inv += imax - i
            j += 1
    sorted_lis += left[i:]
    sorted_lis += right[j:]
    return (sorted_lis, inv)
    
# Assignment
f = open('DCdata.txt', 'r')
test_lis = []
for line in f:
    test_lis.append(int(line))
print merge_sort_count(test_lis)[1]