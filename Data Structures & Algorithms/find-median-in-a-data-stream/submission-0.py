class MedianFinder:

    def __init__(self):
        # need two heap have quick access to the mediam
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small)+1:
            node = heapq.heappop(self.large)
            heapq.heappush(self.small, -node)
        if len(self.small) > len(self.large)+1:
            node = -heapq.heappop(self.small)
            heapq.heappush(self.large, node)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        