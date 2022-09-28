data = [-2, 45, 0, 11, -9]

print('Unsorted Array:', data)

# loop to access each array element
for i in range(0, len(data)):

    # this loop for the next element from the first selected element
    for j in range(i+1, len(data)):
         if (j+1) != len(data) and data[i] < data[(j)]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

print('Sorted Array:', data)
