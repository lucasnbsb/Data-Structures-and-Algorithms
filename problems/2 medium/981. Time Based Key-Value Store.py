class TimeMap:

    def __init__(self):
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value]) 
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap: return ""
        else:
            arr = self.timeMap[key]
            left = 0
            right = len(arr)-1
            res = ""
            while left <= right:
                mid = (left+right)//2
                if arr[mid][0] == timestamp: return arr[mid][1]
                if arr[mid][0] <= timestamp:
                    res = arr[mid][1]
                    left = mid+1
                else:
                    right = mid-1
            return res        