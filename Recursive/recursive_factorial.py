#function compute factorial by recursive
def recursive_factorial(n):
  # base case
  if n == 0:
    return 1
  # recursive case
  return n * recursive_factorial(n - 1)
