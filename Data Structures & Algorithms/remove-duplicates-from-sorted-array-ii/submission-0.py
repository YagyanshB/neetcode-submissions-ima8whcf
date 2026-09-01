class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0 

        for R in range(len(nums)):
            if L < 2 or nums[R] != nums[L - 2]:
                nums[L] = nums[R]
                L += 1
        return L