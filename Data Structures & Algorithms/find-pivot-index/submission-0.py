class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        total = sum(nums)
        for i,n in enumerate(nums):
            rsum = total - lsum - n
            if lsum == rsum:
                return i
            lsum += n
        return -1
        