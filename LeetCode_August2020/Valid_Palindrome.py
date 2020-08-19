import re
class Solution:
    def isPalindrome(self, s):
        matched=re.findall("[^\s\W_]",s)
        pal_str = ''.join(matched)
        
        if pal_str == '':
            return True
            
        new_str = ''
        
        while matched != []:
            new_str+= matched.pop()
    
        return new_str.casefold() == pal_str.casefold()


s= Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))