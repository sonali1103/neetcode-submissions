class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            nums2 = target - n
            if (nums2 in nums_map):
                return [nums_map[nums2], i]
            nums_map[n] = i

        