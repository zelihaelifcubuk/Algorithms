def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            if array[j] > array[j + 1]:
                # swapping elements
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = [-2, 45, 0, 11, -9]
print('Unsorted Array:', data)

bubbleSort(data)
print('Sorted Array:', data)


