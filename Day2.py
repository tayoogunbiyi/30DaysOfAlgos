'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 

An input string is valid if:
  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''

#using stack 


def validParenthesis(str):
  dict = {")":"(","]":"[","}":"{"}
  stack = []
  for bracket in str:
    if bracket in dict:
      top = stack.pop() if stack else -1
      if dict[bracket] != top:
        return False
    else:
      stack.append(bracket)
  return not stack