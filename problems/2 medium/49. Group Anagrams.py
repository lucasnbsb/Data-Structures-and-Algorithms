class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]

        occurences = collections.defaultdict(list)
        for word in strs:
            srt = ''.join(sorted(word))
            occurences[srt].append(word)
        
        output = []
        for values in occurences.values():
            output.append(values)
        return output