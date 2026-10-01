class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        res = []
        for i, c in count.items():
            res.append((i,c))
        
        res.sort(key=lambda x: x[1], reverse=True)
        r = []
        for i in range(k):
            r.append(res[i][0])
        return r
        