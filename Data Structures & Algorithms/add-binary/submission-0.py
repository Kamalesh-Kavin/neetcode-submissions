class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            da = int(a[i]) if i < len(a) else 0
            db = int(b[i]) if i < len(b) else 0
            total = da+db+carry
            char = str(total%2)
            res = char+res
            carry = total//2
        if carry:
            res = "1" +res
        return res