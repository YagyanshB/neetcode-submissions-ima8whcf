class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        i = len(arr) - 1
        while i >= 0:
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)
            i -= 1
        return arr      