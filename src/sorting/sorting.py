# TO-DO: complete the helper function below to merge 2 SORTED arrays
def merge(arrA, arrB):
    c = [] # final output/merged array
    ai, bi = 0, 0 # track the index of a and b
    # as long as both ai and bi are less than 
    # the length of either of the arrays
    while ai < len(arrA) and bi < len(arrB):
        # compare the two values at each index
        # in each array
        if arrA[ai] < arrB[bi]:
            # if the value at ai is less than
            # the value at bi, append the value at 
            # ai to c and add one to the index
            c.append(arrA[ai])
            ai += 1
        else:
            c.append(arrB[bi])
            bi += 1
    # when we reach the end of one of the arrays
    # we extend the output array with the remaining 
    # values from the other array
    if ai == len(arrA):
        c.extend(arrB[bi:])
    else:
        c.extend(arrA[ai:])

    return c

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # merge sort continually splits lists down
    # to one element
    
    if len(arr) > 1:
        # split the list in half and call merge sort recursively 
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        # once we have arrays of length 1
        # merge the now sorted sublists
        arr = merge(left, right)
     
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass