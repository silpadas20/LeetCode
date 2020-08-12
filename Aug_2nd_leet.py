---- leet1 path sum
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
   
--- leet3  Excel column number
class Solution:
    def titleToNumber(self, s: str) -> int:
        titles=list(map(chr, range(65,91)))
		titles.insert(0,0)
	
        power ,colnum=0 ,0 
        
        if s in titles:
            return titles.index(s)
            
        for ele in s[::-1]:
            colnum+=titles.index(ele)*(26**power)
            power+=1
        return colnum


		 