class Solution:
    def topKFrequent(self, nums: List[int], k: int) ->List[int]:
        from collections import Counter

        counter = Counter(nums)

        sorted_numbers = sorted(counter, 
        key = counter.get, reverse = True)

        return sorted_numbers[:k]
    