import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat: List[int] = [item for row in matrix for item in row]
        print(flat)
        l, r = 0, len(flat)-1

        while l<=r:
            m = (l+r) // 2
            if flat[m] > target:
                r=m-1
            elif flat[m] < target:
                l=m+1
            else:
                return True
        return False