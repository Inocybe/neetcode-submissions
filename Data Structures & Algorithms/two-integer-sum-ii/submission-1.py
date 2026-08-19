class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (val := numbers[l] + numbers[r]) != target:
            if val > target:
                r -= 1
            if val < target:
                l += 1
        
        return [l + 1, r + 1]