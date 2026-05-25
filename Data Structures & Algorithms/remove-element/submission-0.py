class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pnt = 0

        for i, curr in enumerate(nums):
            if curr != val:
                nums[pnt] = curr
                pnt += 1
        return pnt