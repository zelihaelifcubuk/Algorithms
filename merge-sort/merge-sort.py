# function to divide the array in the two subarrays
def merge_sort(array, left_index, right_index):

    # The function is called repeatedly until it is completely sorted.
	# Exit the function when completely sorted
    if left_index >= right_index:
    	return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)     # left part of array (left+middle)
    merge_sort(array, middle + 1, right_index)      # rigth part of array (element after middle+right)
    merge(array, left_index, right_index, middle)    # merge of two subarrays after being sorted


# Defining a function for merge the array
def merge(array, left_index, right_index, middle):

    # Creating subparts of an array
    left_subArray = array[left_index:middle + 1] # this array contains elements from left_subArray to middle
    right_subArray = array[middle + 1:right_index + 1] # this array contains elements from the first element after middle to right_subArray

    # Initial values for variables that we use to keep track of where we are in each array
    left_subArray_index = 0
    right_subArray_index = 0
    sorted_index = left_index

    # traverse both copies until we get run out one element
    while left_subArray_index < len(left_subArray) and right_subArray_index < len(right_subArray):

        # If our left_subArray has the smaller element, put it in the sorted
        # part and then move forward in left_subArray (by increasing the index)
        if left_subArray[left_subArray_index] <= right_subArray[right_subArray_index]:
            array[sorted_index] = left_subArray[left_subArray_index]
            left_subArray_index = left_subArray_index + 1

        # Otherwise add it into the right subarray
        else:
            array[sorted_index] = right_subArray[right_subArray_index]
            right_subArray_index = right_subArray_index + 1

        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # we will go through the remaining elements and add them
    while left_subArray_index < len(left_subArray):
        array[sorted_index] = left_subArray[left_subArray_index]
        left_subArray_index = left_subArray_index + 1
        sorted_index = sorted_index + 1

    while right_subArray_index < len(right_subArray):
        array[sorted_index] = right_subArray[right_subArray_index]
        right_subArray_index = right_subArray_index + 1
        sorted_index = sorted_index + 1


arr = [-2, 45, 0, 11, -9, 28, -35, 66, 91, 73, 100]
print('Unsorted Array: ', arr)

merge_sort(arr, 0, len(arr) - 1)
print('Sorted Array: ', arr)