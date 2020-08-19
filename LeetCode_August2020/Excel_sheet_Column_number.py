class Solution:
    def titleToNumber(self, s: str) -> int:
        titles=list(map(chr,range(65,91)))
        titles.insert(0,0)
        power,colnum=0 ,0 
        if s in titles:
            return titles.index(s)
            
        for ele in s[::-1]:
            colnum+=titles.index(ele)*(26**power)
            power+=1
        return colnum