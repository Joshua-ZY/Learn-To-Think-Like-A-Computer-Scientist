# -*- coding: utf-8 -*-

#week2 quick sort
'''
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the ith row of the file gives you the ith entry of an input array.
Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons. (This is because the pivot element is compared to each of the other m−1 elements in the subarray in this recursive call.)
WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR PROBLEM 1:
For the first part of the programming assignment, you should always use the first element of the array as the pivot element.
HOW TO GIVE US YOUR ANSWER:
Type the numeric answer in the space provided.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.
(We do not require you to submit your code, so feel free to use the programming language of your choice, just type the numeric answer in the following space.)

DIRECTIONS FOR PROBLEM 2:
Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element. Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.
Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.

DIRECTIONS FOR PROBLEM 3:
Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule. [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).
EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.
SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements. You should NOT do this. That is, as in the previous two problems, you should simply add m−1 to your running total of comparisons every time you recurse on a subarray with length m.
'''
def quicksort(lis, l, r, counter = 0):
    if l >= r:
        return counter
        
    # comment out according to different questions
    
    #partition_pos = partition_head(lis, l, r)
    partition_pos = partition_tail(lis, l, r)
    #partition_pos = partition_median(lis, l, r)
    
    counter += (r - l)
    counter += quicksort(lis, l, partition_pos - 1)
    counter += quicksort(lis, partition_pos + 1, r)
    return counter
    
def partition_head(lis, l, r):
    pivot = lis[l]; partition_pos = l; i = l + 1
    while i <= r:
        if lis[i] < pivot:
            partition_pos += 1
            lis[i], lis[partition_pos] = lis[partition_pos], lis[i] # swap
        i += 1
    lis[l], lis[partition_pos] = lis[partition_pos], lis[l]
    return partition_pos
   
def partition_tail(lis, l, r):
    lis[l], lis[r] = lis[r], lis[l]
    pivot = lis[l]; partition_pos = l; i = l + 1
    while i <= r:
        if lis[i] < pivot:
            partition_pos += 1
            lis[i], lis[partition_pos] = lis[partition_pos], lis[i] # swap
        i += 1
    lis[l], lis[partition_pos] = lis[partition_pos], lis[l]
    return partition_pos
   
def partition_median(lis, l, r):
    # find median
    mid = l + (r - l) / 2
    if lis[l] > lis[r] and lis[mid] > lis[r]:
        pivot_pos = mid if lis[l] > lis[mid] else l
    else:
        if lis[l] > lis[mid]:
            pivot_pos = r if lis[l] > lis[r] else l
        else:
            pivot_pos = r if lis[mid] > lis[r] else mid
            
    lis[l], lis[pivot_pos] = lis[pivot_pos], lis[l]
    pivot = lis[l]; partition_pos = l; i = l + 1
    while i <= r:
        if lis[i] < pivot:
            partition_pos += 1
            lis[i], lis[partition_pos] = lis[partition_pos], lis[i] # swap
        i += 1
    lis[l], lis[partition_pos] = lis[partition_pos], lis[l]
    return partition_pos
'''
# Test
test = [11,5,2,14,20,7,6,8,13,1,12,16,15,10,18,3,19,17,4,9]
count = quicksort(test, 0, len(test) - 1)
print test, count
'''
    
# Assignment 1
f = open('sortdata.txt', 'r')
test_lis = []
for line in f:
    test_lis.append(int(line))
print quicksort(test_lis,0,len(test_lis)-1, 0)