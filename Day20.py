def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    #concatenate str1 to str1
    temp = str1 + str1

    #to check if str2 can be found str1+str1
    if str2 in temp:
        return True

    return False

print(isRotation("waterbottle", "ewaterbottl"))
