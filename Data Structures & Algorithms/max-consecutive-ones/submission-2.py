class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_one = 0
        
        for i in nums:
            if i == 1:
                count += 1
                max_one = max(max_one, count)
            else: # i is 0
                count = 0
        
        return max_one