
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        # Step 1: Count frequencies
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Place numbers into frequency buckets
        for num, freq in hashmap.items():
            buckets[freq].append(num)

        # Step 4: Collect k most frequent elements
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
