# Implementation of InsertionSort
# Time: O(n^2) where the array is in descending order
# Space: O(1)
def insertionSort(array):
    # Traverse through 1 to len(array)
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[j + 1] < array[j]:
            # array[j] and array[j + 1] are out of order so swap them
            tmp = array[j + 1]
            array[j + 1] = array[j]
            array[j] = tmp
            j -= 1
    return array
