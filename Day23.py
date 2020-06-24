
def longestValidParentheses(s):
  if len(s) <= 1:
      return 0

  #using the stack data structure
  stack = [-1]
  maxnumber = 0
  for i in range(len(s)):
      if s[i] == '(':
          stack.append(i)
      elif s[i] == ')':
          if stack[-1] != -1 and s[stack[-1]] == '(':
              stack.pop()
              maxnumber = max(i - stack[-1],maxnumber)
          else:
              stack.append(i)


  #Using the left and right pointer
  left, right = 0,0
  maxnumber = 0

  #starting from the left
  for i in range(len(s)):
      if s[i] == '(':
          left +=1
      else:
          right +=1
      if left == right:
          maxnumber = max(maxnumber, 2 * right)
      else:
          if right >= left:
              left = right = 0

  left,right = 0,0

  #starting from the right
  for i in range(len(s)-1,-1,-1):
      if s[i] == '(':
          left += 1
      else:
          right += 1
      if left == right:
          maxnumber = max(maxnumber, 2 * left)
      else:
          if left >= right:
              left = right = 0

  return maxnumber
