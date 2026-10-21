class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in res:
                return [res[n2], i]
            res[n] = i
        