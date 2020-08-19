class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        demo1= -prices[0]
        demo2=float('-inf')
        demo3=float('-inf')
        demo4=float('-inf')
        
        for p in prices:
            demo1=max(demo1, -p)
            demo2=max(demo2, demo1+p)
            demo3=max(demo3, demo2-p)
            demo4=max(demo4, demo3+p)
            
        return demo4
    
