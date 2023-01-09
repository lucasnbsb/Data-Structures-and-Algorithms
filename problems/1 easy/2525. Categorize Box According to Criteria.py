class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
            tenfour = 10**4
            tennine = 10**9
            bulky = False
            heavy = False
            if ((length >= tenfour or width >= tenfour or height >= tenfour) or (length*width*height) >= tennine):
                bulky = True
            
            if mass >= 100:
                heavy = True
                
                
            if bulky and heavy:
                return "Both"
            if bulky and not heavy:
                return "Bulky"
            if heavy and not bulky:
                return "Heavy"
            else:
                return "Neither"