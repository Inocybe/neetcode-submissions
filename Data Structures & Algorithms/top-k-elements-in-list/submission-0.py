class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        top_k_pairs = sorted(seen.items(), key=lambda x: x[1])[-k:]

        return [item[0] for item in top_k_pairs]
            