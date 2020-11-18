import random
import time

"""
Sorting takes a list, and ensures that it is "in order"
[ 2 1 6 2 5]
[ 1 2 2 5 6]

There's a bunch of different ways to sort things.

Two classes of sorts: quadratic sorts, logarithmic sorts

https://visualgo.net/bn/sorting
"""

"""
do
  swapped = false
  for i = 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap(leftElement, rightElement)
      swapped = true
while swapped
"""


def is_sorted(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] > a_list[i + 1]:
            return False
    return True


def bubble_sort_simple(a_list):
    for i in range(len(a_list) - 1):
        for j in range(len(a_list) - 1):
            # if the thing is out of order
            if a_list[j] > a_list[j + 1]:
                # swap it - write a helper function to do this
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp

    return a_list


def bubble_sort_mega_complex(a_list):
    i = 0
    swapped = True  # just to go into the loop
    while swapped and i < len(a_list) - 1:
        swapped = False  # makes sure that we do a swap in the internal loop
        for j in range(len(a_list) - 1):
            # if the thing is out of order
            if a_list[j] > a_list[j + 1]:
                # swap it - write a helper function to do this
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
                swapped = True  # we did the swap in the internal loop
        i += 1  # very easy to forget this increment thing

    return a_list


def simple_bubble_test():
    my_list = [random.randint(0, 100) for _ in range(100)]
    print(my_list)
    bubble_sort_simple(my_list)
    print(my_list)
    print(is_sorted(my_list))


def complex_bubble_test():
    """
    complex is a joke, this is not really very complex
    """
    reversed_list = [5, 4, 3, 2, 1]
    bubble_sort_mega_complex(reversed_list)
    print(reversed_list, is_sorted(reversed_list))

    for i in range(10):
        print('Test', i + 1)
        my_list = [random.randint(0, 100) for _ in range(20)]
        print(my_list)
        bubble_sort_mega_complex(my_list)
        print(my_list)
        print(is_sorted(my_list))


def find_min_index(a_list, start):
    min_index = start
    for i in range(start, len(a_list)):
        if a_list[min_index] > a_list[i]:
            min_index = i

    return min_index


def swap(a_list, x, y):
    temp = a_list[x]
    a_list[x] = a_list[y]
    a_list[y] = temp


def selection_sort_way_cool(a_list):
    """
        you find min, put it in lowest spot
        advance "lowest spot"

        []
    """
    for i in range(len(a_list)):
        min_index = find_min_index(a_list, i)
        swap(a_list, min_index, i)

    return a_list


def selection_sort_test():
    for i in range(10):
        print('Test', i + 1)
        my_list = [random.randint(0, 100) for _ in range(20)]
        print(my_list)
        selection_sort_way_cool(my_list)
        print(my_list)
        print(is_sorted(my_list))

    new_list = [random.randint(0, 100) for _ in range(20)]
    selection_sort_way_cool(new_list)
    print(new_list)


def insertion_sort_way_cool(a_list):
    """
    pull back sort!
    :param a_list:
    :return:
    """
    for i in range(1, len(a_list)):
        j = i
        # swap element at a_list[i] back until it's in the "right" position
        while j > 0 and a_list[j] < a_list[j - 1]:
            swap(a_list, j, j - 1)
            # I WILL FORGET THIS, DON'T TYPE IN ALL CAPS
            j -= 1

    return a_list


def insertion_sort_test():
    for i in range(10):
        print('Test', i + 1)
        my_list = [random.randint(0, 100) for _ in range(20)]
        print(my_list)
        insertion_sort_way_cool(my_list)
        print(my_list)
        print(is_sorted(my_list))

    if False:
        new_list = [random.randint(0, 100) for _ in range(20)]
        selection_sort_way_cool(new_list)
        print(new_list)


def quick_sort(a_list):
    """
    :param a_list:
    :return:
    """

    # you have two buckets
    # special element its name is pivot, who knows, fulcrum in a lever
    # all elements that are less than the pivot go into bucket A
    # all elements that are greater than the pivot go into bucket B
    # then you have to decide what to do with elements equal to the pivot, create bucket C add them.

    # base case:
    if len(a_list) <= 1:
        return a_list

    pivot = a_list[0]
    bucket_less = []
    bucket_greater = []
    bucket_equal = []

    for x in a_list:
        if x < pivot:
            bucket_less.append(x)
        elif x == pivot:
            bucket_equal.append(x)
        else:
            bucket_greater.append(x)

    return quick_sort(bucket_less) + bucket_equal + quick_sort(bucket_greater)


def quick_sort_test():
    for i in range(10):
        print('Test', i + 1)
        my_list = [random.randint(0, 100) for _ in range(20)]
        print(my_list)
        my_list = quick_sort(my_list)
        print(my_list)
        print(is_sorted(my_list))


# simple_bubble_test()
# complex_bubble_test()
# selection_sort_test()
# insertion_sort_test()
# quick_sort_test()

def sort_time_test(sorting, n):
    for i in range(5):
        my_list = [random.randint(0, 100) for _ in range(n)]
        start = time.time()
        sorting(my_list)
        end = time.time()
        # ns is 10^(-9) seconds
        print('The time was', end - start)


def merge(a_list, b_list):
    """
    Assume that a_list and b_list are sorted
    """
    merged_list = []
    a_index = 0
    b_index = 0
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            merged_list.append(a_list[a_index])
            a_index += 1
        else:
            merged_list.append(b_list[b_index])
            b_index += 1

    while a_index < len(a_list):
        merged_list.append(a_list[a_index])
        a_index += 1
    while b_index < len(b_list):
        merged_list.append(b_list[b_index])
        b_index += 1

    return merged_list


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        merge_a = merge_sort(a_list[: len(a_list) // 2])
        merge_b = merge_sort(a_list[len(a_list) // 2:])
        full_merge = merge(merge_a, merge_b)
        # print(merge_a, merge_b, full_merge)
        return full_merge


def merge_sort_test():
    for i in range(10):
        print('Test', i + 1)
        my_list = [random.randint(0, 100) for _ in range(20)]
        print(my_list)
        my_list = merge_sort(my_list)
        print(my_list)
        print(is_sorted(my_list))


def time_test():
    print('size 1000')
    sort_time_test(merge_sort, 1000)
    print('size 10000')
    sort_time_test(merge_sort, 10000)
    print('size 100000')
    sort_time_test(merge_sort, 100000)
    print('size 1000000')
    sort_time_test(merge_sort, 1000000)
    print('size 10000000')
    sort_time_test(merge_sort, 10000000)


# print(merge([1, 2, 3, 6, 8, 9, 11], [2, 3, 5, 7, 8, 9, 10]))
# merge_sort_test()
time_test()
"""
    We learned to test our code, sometimes.
    We learned bubble sort, selection sort, insertion sort, quick sort
    We did not learn merge sort :( we'll do that wednesday.
    
    Project 3 is going to be recursion, as is the ancient tradition.  
"""
