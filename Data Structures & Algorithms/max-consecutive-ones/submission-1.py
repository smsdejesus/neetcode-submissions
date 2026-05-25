class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = max_one = 0
        
        for i in nums:
            if i == 1:
                curr += 1
                max_one = max(max_one, curr)
            else: # i is 0
                curr = 0
        
        return max_one