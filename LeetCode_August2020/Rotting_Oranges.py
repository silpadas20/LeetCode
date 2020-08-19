class Solution:
    def orangesRotting(self, grid) -> int:
        time=0
        rows = len(grid)
        cols=  len(grid[0])
        rotten = [(x,y) for x in range(rows) for y in range(cols) if grid[x][y] ==2]
        
        def rotting(rotten):
            temp=[]
            for x,y in rotten :
                if x > 0 and grid[x-1][y] ==1:
                    grid[x-1][y]+=1
                    temp.append((x-1,y))
                
                if x < rows-1 and grid[x+1][y] ==1 :
                    grid[x+1][y]+=1
                    temp.append((x+1,y))
                    
                if y < cols-1 and grid[x][y+1]==1:
                    grid[x][y+1]+=1
                    temp.append((x,y+1))
                    
                if y > 0 and grid[x][y-1] ==1 :
                    grid[x][y-1]+=1
                    temp.append((x,y-1))

            return temp
                    
        while rotten:
            rotten = rotting(rotten)
            if len(rotten) ==0 :
                break
            time+=1
            
        one_chk= [(x,y) for x in range(rows) for y in range(cols) if grid[x][y] ==1]
        if len(one_chk) > 0 :
            return -1
        
        return time