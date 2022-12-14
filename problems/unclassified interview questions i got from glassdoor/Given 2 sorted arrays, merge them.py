# Programming question - Given 2 sorted arrays, merge them. 
# Follow up, ensure only 1 of each element is saved in the merged array aka no duplicates.

class Solution:
    def merge(n1: list[int], n2: list[int]) -> list[int]:
        merged = []
        current1 = 0;
        current2 = 0;

        while current1 < len(n1) and current2 < len(n2):
            if n1[current1] < n2[current2]:
                merged.append(n1[current1])
                current1 += 1
            elif n2[current2] < n1[current1]:
                merged.append(n2[current2])
                current2 += 1
            else:
                val = n1[current1]
                merged.append(val)
                while current1 < len(n1) and n1[current1] == val:
                    current1 += 1
                while current2 < len(n2) and n2[current2] == val:
                    current2 += 1
        
        if current1 < len(n1):
            merged.extend(n1[current1:])
        if current2 < len(n2):
            merged.extend(n2[current2:])
        return merged
            
    print(merge([1,2,3,4,5,6], [3,3,3,3,3,3,3]))