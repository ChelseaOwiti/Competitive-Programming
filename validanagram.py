class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #checking the length of the strings first
        if len(s) != len(t):
            return False
        #hashmaps to store the strings
        countS, countT = {}, {}
        for i in range(len(s)):
            
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            #checking if the values in both hashmaps are equal
            if countS[c] != countT.get(c, 0):
                return False
    
        return True


       
       