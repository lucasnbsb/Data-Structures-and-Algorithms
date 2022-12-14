class Solution:
    def howMany(meetings :list[list[int]]):
        maxMeetings = 0
        currMeetings = 0

        startTimes = sorted([i[0] for i in meetings])
        endTimes = sorted([i[1] for i in meetings])
        s, e = 0, 0

        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                s += 1
                currMeetings +=1
            else:
                e += 1
                currMeetings -=1
            maxMeetings = max(currMeetings, maxMeetings)

        return maxMeetings;
    
    
    print(howMany([[0,30], [5,10], [15,20]]))


# 0                                 30
#      5        10
#               10       15

# ligamos pra duas coisas - os tempos de inicio e os tempos de fim
# mas precisamos seguir eles ordenados no tempo