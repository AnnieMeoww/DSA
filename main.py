from Binary_search import binary_search
from Selection_sort import selection_sort

# test arrays for `binary_search`
print(f"Binary search: {binary_search.binarySearch([1, 2, 3, 4, 5], 2)}")

#test arrays for `selection_sort`
array = [1, 3, 2, 10, -5, -20, 100]
selection_sort.selectionSort(array)
print(f"Selection sort: {array}")