class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        nums_sorted = sorted(nums)

        result = []
        for i, num in enumerate(nums_sorted):
            l = 0
            r = len(nums) - 1
            target = -num
            while r > l:
                if i == l: 
                    l+=1
                    continue
                if i == r: 
                    r-=1
                    continue
                
                val = nums_sorted[l] + nums_sorted[r]
                if val == target:
                    array = [num, nums_sorted[l], nums_sorted[r]]
                    array = sorted(array)
                    res_tuple = (array[0], array[1], array[2])
                    res_hash = hash(res_tuple)
                    if not res_hash in seen:
                        seen[res_hash] = True;
                        result.append(array)
                    r-=1
                elif val < target:
                    l+=1
                elif val > target:
                    r-=1
        return result



            
                

