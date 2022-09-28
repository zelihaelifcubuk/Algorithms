def insertion_sort(array):

    # Loop from the second element of the array until the last element
    for i in range(1, len(array)):

        # This is the element we want to position in its correct place
        key_item = array[i]

        # j is the element to which the current element will be compared with the previous element.
        j = i - 1

        # Run through the list of items (the left portion of the array) and
        # find the correct position of the element referenced by `key_item`.
        # Do this only if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:

            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When finished shifting the elements, `key_item` is positioned in its correct location
        array[j + 1] = key_item

    return array

arr = [-2, 45, 0, 11, -9]
print('Unsorted Array:', arr)

insertion_sort(arr)
print('Sorted Array:', arr)