class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first sort the start time, then check the  end time and next start time
        intervals.sort(key=lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                if end < intervals[i][1]:
                    end = intervals[i][1]
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start, end])
        return res
        