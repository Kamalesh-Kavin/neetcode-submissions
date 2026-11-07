class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s)!=len(t):
            return False
        length = len(s)
        for i in range(length):
            hashmap[s[i]] = hashmap.get(s[i],0)+1
            hashmap[t[i]] = hashmap.get(t[i],0)-1
        print(hashmap)
        return all(v == 0 for v in hashmap.values())
            
        