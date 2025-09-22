class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        top = -1
        for i in s:
            if i in ['(', '{', '[']: l.append(i); top +=1
            else:
                if top == -1: return False
                if i == ')':
                    if l[top] != '(': return False
                    l.pop()
                    top -= 1
                if i == '}':
                    if l[top] != '{': return False
                    l.pop()
                    top -= 1
                if i == ']':
                    if l[top] != '[': return False
                    l.pop()
                    top -= 1
        if top > -1: return False
        return True
