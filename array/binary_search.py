# Binary search is an algorithm for finding an element in a sorted array in O(log(n)) time

def binary_search(arr, target) :
    left = 0
    right = len(arr) 

    while (left < right) :
        mid = (left + right) // 2

        if (mid == target) :
            return mid
        elif (arr[mid] > target) :
            right = mid
        else :
            left = mid + 1

    return -1