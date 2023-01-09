class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        self.dfs(s,[],output)
        return output
        
    def isPalindrome(self,s):
            return s == s[::-1]
        
    def dfs(self, s, path, output):
        if not s:
            output.append(path)
            return
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.dfs(s[i+1:], path+[s[:i+1]], output)