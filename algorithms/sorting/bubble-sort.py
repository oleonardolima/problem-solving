# Space: O(1) - Inplace Algorithm
# Time: O(n^2) - Worst and Average Case --> Best Case (already sorted array): O(n) 

def bubbleSort(array):
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		for i in range(len(array) - 1):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				is_sorted = False
	
	return array
