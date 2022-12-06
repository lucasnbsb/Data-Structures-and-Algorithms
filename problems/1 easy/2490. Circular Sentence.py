class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        spl = sentence.split()
        for i in range(len(spl)-1):
            if(spl[i][-1] != spl[i+1][0]):
                return False
        return spl[0][0] == spl[-1][-1]