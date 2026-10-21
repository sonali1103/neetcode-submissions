class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = []

        for st, end in intervals:
            if len(res) > 0 and res[-1][1] >= st:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([st,end])
        return res
        