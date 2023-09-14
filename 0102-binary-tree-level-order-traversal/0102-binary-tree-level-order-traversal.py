# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = [] 
        
        q = collections.deque([(root, 0)]) 
        
        while q:
            node, lvl = q.popleft() 
            
            if len(res) == lvl: 
                res.append([])
            res[lvl].append(node.val) 
            
            if node.left: 
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))
                
        return res
    
# Notes:
# - queue strucuture
# - keep track of the node and our current level
# - setup a results array

# - python deque
#     - collections.deque
#     - initalize the q with our root node level 0

# - while loop for while queue:
#     popleft our first node and assign the values to node an lvl
    
#     if results array length == lvl:
#         results.append([])
#     results[lvl].append(node.val)
    
#     check if node has a left child:
#         append to que (node.left, lvl + 1)
#     check if node has a right child
#      append to que (node.right, lvl + 1)
        
# return results