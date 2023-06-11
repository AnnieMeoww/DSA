# function merge 2 subarrays
# input p: start index
# input q: midpoint in array
# input r: end index
def merge(array, p, q, r):
    # copy 2 halfs of array into firstHalf and secondHalf
  firstHalf = array[p:q+1]
  secondHalf = array[q+1:r+1]

  # i: indexes in firstHalf
  # j: indexes in secondHalf
  # k: indexes in array 
  i = 0
  j = 0
  k = p
  
  # repeatedly compare two element in firstHalf and secondHalf and copy smallest element into array until one of two subarrays has fully copied element back into array
  while (i < len(firstHalf) and j < len(secondHalf)):
    if (firstHalf[i] <= secondHalf[j]):
      array[k] = firstHalf[i]
      i += 1
      k += 1
    else:
      array[k] = secondHalf[j]
      j += 1
      k += 1

  # copy the rest of the subarray which not fully copied into array
  while (i < len(firstHalf)):
    array[k] = firstHalf[i]
    i += 1
    k += 1

  while (j < len(secondHalf)):
    array[k] = secondHalf[j]
    j += 1
    k += 1
    

# function repeatedly halves array into arrays which has 1 or 0 element and merge them again
def merge_sort(array, p, r):
  if (p < r):
    q = int((p + r) / 2)  # midpoint of array
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)
    merge(array, p, q, r)