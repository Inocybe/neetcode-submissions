class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        water = 0

        # build prefix array
        for i, h in enumerate(height):
            if i == 0:
                prefix[i] = h
                continue
            prefix[i] = max(prefix[i-1], h)
        
        # build suffix array
        for j, h in enumerate(reversed(height)):
            if j == 0:
                suffix[n-1-j] = h
                continue
            suffix[n-1-j] = max(suffix[n-j], h)
        
        # calcualte water
        for i, h in enumerate(height):
            water+= min(prefix[i], suffix[i]) - height[i]
        return water