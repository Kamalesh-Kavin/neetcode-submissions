class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap=dict()
        for i,j in enumerate(numbers):
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff],i+1]
            hashmap[j] = i+1
        return -1