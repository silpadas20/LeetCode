class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root,travsum):
        count= defaultdict(int)
        
        def dfs(root,prev):
            if root is None:
                return None
            
            curr = prev+ root.val
    
            if abs(curr) > abs(travsum):
                diff = curr -travsum
				if diff in count:
                    count[diff]-=1  
                    curr=curr-diff
            if curr in count:
                count[curr]+=1
            else:
                count[curr]=1

            dfs(root.left,curr)
            dfs(root.right,curr)
            
        dfs(root,0)
        return count[travsum]