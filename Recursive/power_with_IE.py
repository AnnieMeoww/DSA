# return if a number is even
def isEven(n) :
  return n % 2 == 0

# return if a number is odd
def isOdd(n) :
  return not isEven(n)

# function compute powers of a number with integer exponent
def power_with_IE(n, exponent):
  # base case
  if(exponent == 0) :
    return 1
  # recursive case with n is negative
  if (exponent < 0):
    return 1/power_with_IE(n, -exponent)
  # recursive case with n is odd
  if (isOdd(exponent)) :
    return n * power_with_IE(n, exponent - 1)
  # recursive case with n is even
  if (isEven(exponent)):
    m = power_with_IE(n, exponent / 2)
    return m * m