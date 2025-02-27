import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        minStops = 0
        currentPosition = startFuel
        maxHeap = []
        i = 0
        n = len(stations)
        while currentPosition < target:
            while i < n and stations[i][0] <= currentPosition:
                heapq.heappush(maxHeap, -stations[i][1])
                i += 1
            if not maxHeap:
                return -1
            currentPosition += -heapq.heappop(maxHeap)
            minStops += 1
        return minStops
