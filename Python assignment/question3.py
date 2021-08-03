# Given a string of brackets as input, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
open = ["[","{","("]
close = ["]","}",")"]
def isBalanced(word):
    stack=[]
    if len(word)==0:
        return 'NO'
    for char in word:
        if char in open:
            stack.append(char)
        elif char in close:
            position = close.index(char)
            if ((len(stack) > 0) and (open[position] == stack[len(stack)-1])):
                stack.pop()
            else:
                return 'NO'
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'
        
print(isBalanced('[]{{()}}'))