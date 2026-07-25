class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        temp = sorted(set(nums))

        longest = 1
        current = 1
        for i in range(1, len(temp)):
            if temp[i] == temp[i-1] + 1:
                current += 1
            else:
                current = 1
            longest = max(current, longest)

        return longest
            
