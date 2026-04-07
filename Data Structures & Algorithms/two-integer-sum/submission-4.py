class Solution:
    def twoSum(self, nums, target): 
        seen = {} # creating an empty dictionary to store number, index

        for i, num in enumerate(nums): # using enumerate to capture number and index
            complement = target - num  # determining what would be the complement to target 
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i
        return []