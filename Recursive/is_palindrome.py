# check whether a string is a palindrome or not
def is_palindrome(chars) :
  # base case 1
  if len(chars) in [0, 1]:
    return True
  # base case 2
  if chars[0] != chars[-1]:
    return False
  # recursive case
  return is_palindrome(chars[1:-1])