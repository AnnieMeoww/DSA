from Binary_search import binary_search
from Selection_sort import selection_sort
from Insertion_sort import insertion_sort
from Recursive import relative_factorial, recursive_factorial, is_palindrome, power_with_IE


# # test array for `binary_search`
# print(f"Binary search: {binary_search.binary_search([1, 2, 3, 4, 5], 2)}")

# #test array for `selection_sort`
# array = [1, 3, 2, 10, -5, -20, 100]
# selection_sort.selection_sort(array)
# print(f"Selection sort: {array}")

# # test array for `insertion_sort`
# array = [22, 11, -99, 88, 9, 9, 7, -42]
# insertion_sort.insertion_sort(array)
# print(f"Insertion sort: {array}")

# #test for `iterative_factorial`
# print(f"Iterative: 5 factorial equal {relative_factorial.iterative_factorial(5)}")

# #test for `recursive_factorial`
# print(f"Recursive: 5! is {recursive_factorial.recursive_factorial(5)}")

# # test for `is_palindrome`
# print(f"Is string a palindrome: {is_palindrome.is_palindrome('xyx')}")

# test for `power_with_IE`
print(f"3 raise to -1 equal {power_with_IE.power_with_IE(3, -1)}")
print(f"3 raise to 0 (base case) equal {power_with_IE.power_with_IE(3, 0)}")
print(f"3 raise to 1 (odd exponent) equal {power_with_IE.power_with_IE(3, 1)}")
print(f"3 raise to 2 (even exponent) equal {power_with_IE.power_with_IE(3, 2)}")