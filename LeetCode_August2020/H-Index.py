class Solution:
    def hIndex(self,citations):
        cit_val =[0]*(len(citations)+1)
        ind=0
        for i in citations:
            if i < len(cit_val):
                cit_val[i]+=1
            elif i >= len(cit_val):
                cit_val[-1]+=1
        
        for i in range(len(cit_val)-1,0,-1):
            ind+=cit_val[i]
            if ind >= i:
                return i
        return 0