class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            elif i > 0 and nums[i-1] == nums[i]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sum = n + nums[low] + nums[high]
                if sum == 0:
                    res.append([n, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif sum > 0:
                    high -= 1
                elif sum < 0:
                    low += 1
        return res

        