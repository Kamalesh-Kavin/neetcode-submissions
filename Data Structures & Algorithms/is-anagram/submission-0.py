class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        else:
            for i in range(n):
                dict_s[s[i]]=dict_s.get(s[i],0)+1
                dict_t[t[i]]=dict_t.get(t[i],0)+1
        if dict_s==dict_t:
            return True
        return False
        