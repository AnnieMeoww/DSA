# function swaps two elements in array
def swap(array, firstIndex, secondIndex) :
  array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]

# function return index of smallest value in subarray starting at `startIndex`
def indexOfMinimum(array, startIndex) :
  minIndex = startIndex
  minValue = array[startIndex]

  for elem in array[startIndex+1:]:
    if elem < minValue:
      minIndex = array.index(elem)
      minValue = elem
  return minIndex

# function selection sort completely
def selectionSort(array) :
  for idx, elem in enumerate(array):
    minIndex = indexOfMinimum(array, idx)
    swap(array, idx, minIndex)

