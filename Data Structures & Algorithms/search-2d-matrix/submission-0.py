class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rptr1,rptr2 = 0,len(matrix) - 1
        cptr1,cptr2 = 0,len(matrix[0]) - 1

        while rptr1 <= rptr2:
            rmid = (rptr1 + rptr2) // 2
            if target < matrix[rmid][0]:
                rptr2 = rmid - 1
            elif target > matrix[rmid][cptr2]:
                rptr1 = rmid + 1
            else:
                while cptr1 <= cptr2:
                    cmid = (cptr1 + cptr2) // 2
                    if target < matrix[rmid][cmid] :
                        cptr2 = cmid - 1
                    elif target > matrix[rmid][cmid]:
                        cptr1 = cmid + 1
                    else:
                        return True
                return False
        return False
