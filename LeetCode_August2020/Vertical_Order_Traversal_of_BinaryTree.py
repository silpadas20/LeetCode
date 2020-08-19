class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
         	self.left = left
         	self.right = right
class Solution:
    def verticalTraversal(self, root):
        mapper=defaultdict(list)
        def dfs(x,y,node):
            if not node:
                return
            dfs(x-1,y+1,node.left)
            dfs(x+1,y+1,node.right)
            mapper[(x,y)].append(node.val)
        dfs(0,0,root)
        output=[]
        old=float('-inf')
        for k,v in sorted(mapper.items()):
            if k[0]!= old:
                output.append([])
            output[-1].extend(sorted(v))
            old=k[0]
        
        return output
        

def hIndex(self,citations):
        citations.sort()
        if not citations:
            return 0 
        for i in  range(len(citations)):
            if citations[i] != 0 :
                min_cit = i
                lesser_cits= len(citations)-citations[i]

                if lesser_cits < 0 :
                    lesser_cits = 0
                
                if min_cit == lesser_cits:
                    return len(citations[min_cit:])
                    break
        return 0

