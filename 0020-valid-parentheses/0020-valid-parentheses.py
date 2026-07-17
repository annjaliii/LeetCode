class Solution(object):
    def isValid(self, s):
        stack=[]
        d={
            ')':'(',
            ']':'[',
            '}':'{'
         }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack.pop() != d[ch]:
                 return False
        return not stack
        