# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=None, end=None):
    if start is None and end is None:
        start = 0 
        end = len(arr)-1
    # Check the base case
    # as long as the end is greater than
    # the start...
    if end >= start:
        # find the middle
        mid = (end + start) // 2

        # if the target is the middle number:
        if arr[mid] == target:
            # return the index where
            # the value is located
            return mid
        
        # if the target is less than the mid:
        elif target < arr[mid]:
            # recursively iterate with mid-1 as the new end
            return binary_search(arr, target, start, mid-1)
        # otherwise the target is greater than the mid
        else:
            # recursively iterate with mid+1 as the new start
            return binary_search(arr, target, mid+1, end)
    else:
        # if start and end have crossed each other
        # we have searched the entire array and
        # the element is not present in the array
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass