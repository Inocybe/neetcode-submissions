import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix = np.array(board)

        # check rows
        for i in range(9):
            if not self.check_duplicates(matrix[i, :]):
                return False
        # check cols
        for i in range(9):
            if not self.check_duplicates(matrix[:, i]):
                return False
        # check boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = matrix[i:i+3, j:j+3].flatten()
                if not self.check_duplicates(box):
                    return False

        return True
            

    def check_duplicates(self, lis: List[str]) -> bool:
        numbers = [val for val in lis if val != "."]
        return len(numbers) == len(set(numbers))