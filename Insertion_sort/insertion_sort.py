# function insert one element into sorted array
def insert(array, index, value) :
  while index >= 0 and array[index] > value:
    array[index + 1] = array[index]
    index -= 1
  array[index+1] = value

# complete insertion sort algorithm
def insertion_sort(array) :
  for i in range(1, len(array)):
    insert(array, i - 1, array[i])