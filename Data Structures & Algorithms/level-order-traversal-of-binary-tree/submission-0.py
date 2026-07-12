# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}
        q = deque()

        if root:
            q.append(root)
        level = 0
        while len(q) > 0:
            levels[level]= []
            for i in range(len(q)):
                curr = q.popleft()
                levels[level].append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
        return list(levels.values())

            