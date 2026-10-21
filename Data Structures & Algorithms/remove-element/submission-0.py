class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        a = b = 0
        for i in range(len(nums)):
            if nums[i] == val:
                b += 1
            else:
                count += 1
                nums[a] = nums[i]
                a += 1
        return count

        