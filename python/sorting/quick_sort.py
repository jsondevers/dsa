# Implementation of QuickSort
# Time: O(n^2) our array is already sorted pick smallest/largest as pivot
# Space: O(n) we create different partitions
def quickSort(array, start, end, iteration):
    if end - start + 1 <= 1:
        return

    pivot = array[end]
    left = start  # pointer for left side

    # Partition: elements smaller than pivot on left side
    print("Iteration: ", iteration)
    print("Array before Partition: ", array)
    for i in range(start, end):
        if array[i] < pivot:
            print("Array before swap: ", array)
            tmp = array[left]
            array[left] = array[i]
            print("Swapping: ", tmp, "<->", array[left])
            array[i] = tmp
            left += 1
            print("Array after swap: ", array)

    # Move pivot in-between left & right sides
    print("Moving pivot in left side: ", array[left])
    array[end] = array[left]
    print("Moving pivot in right side: ", pivot)
    array[left] = pivot
    print("Array after partition: ", array)
    print("***Partitoning end***\n")

    # Quick sort left side
    print("Quick sort the left: ", quickSort(array, start, left - 1, iteration + 1))

    # Quick sort right side
    print("Quick sort the right: ", quickSort(array, left + 1, end, iteration + 1))
    print("End of iteration ", iteration, "\n")

    return array


def main():

    array = [3, 1, 5, 2, 4, 8, 7]
    print("Array to be sorted: ", array, "\n")
    print(quickSort(array, 0, len(array) - 1, 0))


if __name__ == "__main__":
    main()
