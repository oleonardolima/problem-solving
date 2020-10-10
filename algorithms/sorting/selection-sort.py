# Space: O(1) - In place
# Time: O(n^2)

def selectionSort(array):
	currIdx = 0
	while currentIx < len(array) - 1:
		smallestIdx = currIdx
		for i in range(currIdx + 1, len(array)):
			if array[smallestIdx] > array[i]:
				smallestIdx = i

		array[currIdx], array[smallestIdx] = array[smallestIdx], array[currIdx]
		currIdx += 1
	
	return array