from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        t_counts = counts.most_common(k)
        ans = []
        for x,y in t_counts:
            ans.append(x)
        return ans