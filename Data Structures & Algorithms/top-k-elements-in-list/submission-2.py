class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = defaultdict(int)

        for x in nums:
            hashMap[x] += 1
        sortedDict = dict(sorted(hashMap.items(), key=lambda item: item[1]))
        
        ans = list(sortedDict.keys())
        ans = ans[len(ans) - k: ]

        return  ans