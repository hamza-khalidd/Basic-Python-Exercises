def bubbleSort(array):
	n = len(array)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if array[j] > array[j+1] :
				array[j], array[j+1] = array[j+1], array[j]


array = [6,4,2,1,3,5]

bubbleSort(array)

print ("Sorted Array: ",array)
