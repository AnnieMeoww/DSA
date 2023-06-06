from Binary_search import binary_search
from Selection_sort import selection_sort
from Insertion_sort import insertion_sort

# test array for `binary_search`
print(f"Binary search: {binary_search.binary_search([1, 2, 3, 4, 5], 2)}")

#test array for `selection_sort`
array = [1, 3, 2, 10, -5, -20, 100]
selection_sort.selection_sort(array)
print(f"Selection sort: {array}")

# test array for `insertion_sort`
array = [22, 11, -99, 88, 9, 9, 7, -42]
insertion_sort.insertion_sort(array)
print(f"Insertion sort: {array}")