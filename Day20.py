def isRotation(str1, str2):
  if len(str1) != len(str2):
    return False
  
  #concatenate str1 to str1
  temp = str1 + str1

  #We will make use of the count in python to check if str2 can be found str1
  if(temp.count(str2) > 0):
    return True

  return False

print(isRotation("waterbottle", "ewaterbotlt"))