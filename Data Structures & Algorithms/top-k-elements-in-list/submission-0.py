class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {} # maps each number to its frequency
        for n in nums:
            if n in numToFreq:
                numToFreq[n] += 1
            else:
                numToFreq[n] = 1
            
        topk = []
        for i in range(k):
            top = max(numToFreq, key=numToFreq.get)
            topk.append(top)
            numToFreq.pop(top)
        return topk
        
