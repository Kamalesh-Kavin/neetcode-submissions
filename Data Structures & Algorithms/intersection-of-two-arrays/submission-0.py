class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashset=set()
        for i in nums1:
            if i in nums2:
                hashset.add(i)
        return list(hashset)