import heapq as hq 

class MedianFinder:
    def __init__(self):
        self.minhp = []
        hq.heapify(self.minhp)
        self.maxhp = []
        hq.heapify(self.maxhp)

    def addNum(self, num: int) -> None:
        if len(self.minhp) == len(self.maxhp) :
            hq.heappush(self.minhp, -hq.heappushpop(self.maxhp, num))
        else :
            hq.heappush(self.maxhp, -hq.heappushpop(self.minhp, -num))

    def findMedian(self) -> float:
        return (self.maxhp[0] - self.minhp[0]) / 2 if len(self.minhp) == len(self.maxhp) else -self.minhp[0] 