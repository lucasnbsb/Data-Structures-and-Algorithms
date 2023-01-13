import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        size = len(tasks)
        if n == 0: return size

        counter = collections.defaultdict(int)
        for t in tasks:
            counter[t] += 1
        
        for k in counter.keys():
            heapq.heappush(maxHeap, (-counter[k], k))

        cooldownzone = deque()
        for i in range(n):
            cooldownzone.append((0, 'idle'))

        cycles = 0
        while size > 0:
            #print(maxHeap, size, cycles, cooldownzone)
            if maxHeap:
                count, task = heapq.heappop(maxHeap)
                cool_count, cool_task = cooldownzone.popleft()
                if cool_count < 0:
                    heapq.heappush(maxHeap, (cool_count, cool_task))
                cooldownzone.append((count+1, task))
                size -= 1
            else:
                cooldownzone.append((0, 'idle'))
                count, task = cooldownzone.popleft()
                if count < 0:
                    heapq.heappush(maxHeap, (count, task))
            cycles += 1
        return cycles            
