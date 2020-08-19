class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
                return 0
            
        intervals=sorted(intervals,key=lambda x: x[1])
        start,overlap=0,0
        
        while start < len(intervals)-1:
            close= intervals[start][1]
            if intervals[start+1][0] >= close:
                start+=1
            else:
                overlap+=1
                intervals.remove(intervals[start+1]) 
        return overlap
    
        
        
        