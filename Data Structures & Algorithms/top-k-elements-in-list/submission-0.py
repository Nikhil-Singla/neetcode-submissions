class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = defaultdict(int)

        for i in nums:
            diction[i] += 1
        
        best = sorted(list(diction.items()), key=lambda x: x[1], reverse=True)[:k]
        ret = [i for i, j in best]
        return ret