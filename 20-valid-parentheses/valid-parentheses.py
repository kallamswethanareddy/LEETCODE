class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        map={']':'[','}':'{',')':'('}
        for i in s:
            if i in map:
                top=a.pop() if a else '#'
                if map[i]!=top:
                    return False
            else:
                a.append(i)
        return not a