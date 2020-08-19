def distributeCandies(self, candies, num_people):
        output=[0]*num_people
        start=0
        remaining=candies
        while remaining > 0:
            output[start%num_people]+=min(start+1,remaining)
            start+=1
            remaining= candies-sum(output)
          
        return output