from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        all_counts = Counter(nums)
        return [item[0] for item in all_counts.most_common(k)]