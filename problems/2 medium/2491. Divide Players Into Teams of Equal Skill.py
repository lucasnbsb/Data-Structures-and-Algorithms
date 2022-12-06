from collections import defaultdict
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        def def_value():
            return 0
#         find max and min, they have to be together, thats the target.
        nmin = 1000001
        nmax = -1
        count = defaultdict(def_value)
        for s in skill:
            count[s] += 1
            if s < nmin:
                nmin = s
            if s > nmax:
                nmax = s
        
        target = nmin+nmax
        runningSum = 0
        for i in range(target//2):
            maxIsIn = nmax-i in count
            minIsIn = nmin+i in count
            if maxIsIn and not minIsIn:
                return -1
            elif minIsIn and not maxIsIn:
                return -1
            elif maxIsIn and minIsIn:
                if count[nmax-i] == count[nmin+i]:
                    while count[nmax-i]:
                        count[nmax-i] -= 1
                        count[nmin+i] -= 1
                        runningSum += ((nmax-i)*(nmin+i))
                else:
                    return -1

        return runningSum