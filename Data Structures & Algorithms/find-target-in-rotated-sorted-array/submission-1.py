class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r) // 2
            v_l = nums[l]
            v_r = nums[r]
            v_m = nums[m]
            if v_m == target: return m
            if v_l == target: return l
            if v_r == target: return r

            if v_l < v_m:
                if v_l < target < v_m:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if v_m < target < v_r:
                    l = m + 1
                else:
                    r = m - 1
                
        return -1
