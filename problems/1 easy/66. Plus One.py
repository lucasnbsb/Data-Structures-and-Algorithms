class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in reversed(range(len(digits))):
            if(digits[i] == 9):
                carry = 1
                digits[i] = 0
            else:
                digits[i]+=1
                carry = 0
                break
        if carry:
            digits.append(0)
            digits[0] = 1
        return digits
