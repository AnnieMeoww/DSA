# function swaps two elements in array
def swap(array, firstIndex, secondIndex) :
  array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]

# function return index of smallest value in subarray starting at `startIndex`
def index_of_minimum(array, startIndex) :
  minIndex = startIndex
  minValue = array[startIndex]

  for elem in array[startIndex+1:]:
    if elem < minValue:
      minIndex = array.index(elem)
      minValue = elem
  return minIndex

# complete selection sort algorithm
def selection_sort(array) :
  for idx, elem in enumerate(array):
    minIndex = index_of_minimum(array, idx)
    swap(array, idx, minIndex)