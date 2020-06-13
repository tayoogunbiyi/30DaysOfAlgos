def moveZeros(arr):
  #instantiate the count
  count = 0

  #tranverse through the array
  for i in arr:
    #check if its a non-zero value
    if i > 0:
      arr[count] = i
      count += 1
  
  while count < len(arr):
    arr[count] = 0
    count += 1
  
  return arr

print(moveZeros([0,1,0,2,3,4,0]))

    