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
  
  string = [ch for substring in string for ch in substring]

  return string   



# Approach 2 
def reverse_arr(arr,start,end):
      while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end -= 1

def reverse_words(arr):
  reverse_arr(arr,0,len(arr)-1)
  start = 0
  for i in range(0,len(arr)):
    if arr[i] == ' ':
      reverse_arr(arr,start,i-1)
      start = i
      if start < len(arr) and arr[start] == ' ':
        start +=1
  if start < len(arr):
    reverse_arr(arr,start,len(arr)-1)
  
  return arr

print(reverse_words(['h','i',' ','t','h','e','r','e']))

['t', 'h', 'e', 'r', 'e', ' ', 'h', 'i']