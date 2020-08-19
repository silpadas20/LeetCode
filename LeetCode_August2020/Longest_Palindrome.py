class Solution:
    def longestPalindrome(self, word) -> int:
        arrange={}
        longest,odd=0,0
        for w in word:
            arrange[w]=word.count(w)

        for k,v in arrange.items():
            if v > 1:
                if v%2 ==0:
                    longest+=v
                else:
                    longest+=(v-1)
                    odd+=1
            else:
                odd+=1
        
        if odd > 0:
            return longest+1
        else:
            return longest