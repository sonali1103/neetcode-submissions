class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        res = [1] * (len(nums))
        for i in range(len(nums)):
            res[i] = pre
            pre = nums[i] * pre
        for k in range(len(nums) - 1, -1, -1):
            res[k] *= post
            post *= nums[k]
        return res


        