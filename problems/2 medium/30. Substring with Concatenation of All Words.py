class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        inputsize = len(s)
        wordlengh = len(words[0])
        numwords = len(words)
        windowsize = wordlengh * numwords
        output = []
        left = 0
        
        # setting up the hashmap of occurences to check against
        wordsDict = defaultdict(int)
        for w in words:
            wordsDict[w] += 1
        
        def checkPermutation(i):
            wordsused = 0
            remaining = wordsDict.copy()
            for j in range(i, i+windowsize, wordlengh):
                tmp = s[j: j+wordlengh]
                if remaining[tmp] > 0:
                    remaining[tmp] -= 1
                    wordsused += 1
                else:
                    break #there is an invalid word in the window
            return numwords == wordsused
        
        for i in range(inputsize - wordlengh + 1):
            if (checkPermutation(i)):
                output.append(i)
                
        return output