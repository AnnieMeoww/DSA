# function describes binary search
def binarySearch(array, targetValue):
  min = 0
  max = len(array) - 1
  avg = 0

  while (min <= max):
    avg = int((min + max) / 2)
    if array[avg] == targetValue:
      return avg
    elif array[avg] > targetValue:
      max = avg - 1
    else:
      min = avg + 1
  return -1



