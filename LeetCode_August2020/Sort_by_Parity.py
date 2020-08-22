class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return
        
        even_arr =[i for i in A if i%2==0]
        odd_arr =[i for i in A if i%2!=0]
        
        even_arr.extend(odd_arr)
        
        return even_arr