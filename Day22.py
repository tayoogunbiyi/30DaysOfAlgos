def reverseSentence(arr):
  string = []
  wordEnd, wordStart = 0, 0
  for i in range(0, len(arr)):
    if arr[i] == " ":
      if wordEnd != 0:
        string.insert(0, [" "] + arr[wordStart: wordEnd + 1])
      wordStart = i + 1
      wordEnd = 0
    elif i == len(arr)-1:
      string.insert(0, arr[wordStart:])
    else:
      wordEnd = i
  
  string = [item for sublist in string for item in sublist]

  return string   