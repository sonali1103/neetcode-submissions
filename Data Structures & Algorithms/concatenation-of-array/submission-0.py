class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ns = []
        for i in range(2):
            for i in nums:
                ns.append(i)
        return ns

        