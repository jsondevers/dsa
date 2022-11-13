# Implementation of MergeSort
# Time: O(nlgn)
# Space: O(n) where n is size of original array, we have to create temp arrays
def mergeSort(array, start, end):
    if end - start + 1 <= 1:
        return array

    # The middle index of the array
    middle = (start + end) // 2

    # Sort the left half
    mergeSort(array, start, middle)

    # Sort the right half
    mergeSort(array, middle + 1, end)

    # Merge sorted halfs
    merge(array, start, middle, end)

    return array


# Merge in-place
def merge(array, start, middle, end):
    # Copy the sorted left & right halfs to temp arrays
    L = array[start : middle + 1]
    R = array[middle + 1 : end + 1]

    i = 0  # index for L
    j = 0  # index for R
    k = start  # index for array

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1
