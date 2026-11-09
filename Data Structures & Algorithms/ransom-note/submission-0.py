class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alp = [0]*26
        for i in magazine:
            alp[ord(i)-ord('a')]+=1
        for i in ransomNote:
            alp[ord(i)-ord('a')]-=1
            if alp[ord(i)-ord('a')]<0:
                return False
        return True
        