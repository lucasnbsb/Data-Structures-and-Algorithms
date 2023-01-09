class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.lastEquals = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.lastEquals += 1
            if self.lastEquals >= self.k :
                return True
        else:
            self.lastEquals = 0
            return False