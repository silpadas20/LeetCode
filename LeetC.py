--- leet1 # detect capital
import unittest
class Solution(unittest.TestCase):
    
    def detectCapitalUse(self,word):
        return word.islower() or word.isupper() or word.capitalize() == word
            
    def test_values(self):
        self.assertEqual(self.detectCapitalUse('Flag'),True)
        self.assertEqual(self.detectCapitalUse('FlaG'),False)
        self.assertEqual(self.detectCapitalUse('flag'),True)
        self.assertEqual(self.detectCapitalUse('FLAG'),True)
        self.assertEqual(self.detectCapitalUse('FLag'),False)
    
          
if __name__ == '__main__':
    unittest.main()
    
---- leet2 #design hashset    

class MyHashSet:

    def __init__(self):
        self.size= 10000
        self.hash_set = [None]*self.size

    def add(self, key) :
        hashval= self.hashing(key)
        
        if self.hash_set[hashval] != None:
            self.hash_set[hashval].append(key)
        else:   
            self.hash_set[hashval] = [key]
            
    def hashing(self,key):
        return key % self.size
        
    def remove(self, key):
        hashval= self.hashing(key)
        
        if self.hash_set[hashval] != None:
            while key in self.hash_set[hashval]:
                self.hash_set[hashval].remove(key)

    def contains(self, key):
        hashval= self.hashing(key)
        
        if self.hash_set[hashval] != None:
            return key in self.hash_set[hashval]

---- leet3 valid palindrome
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

-----leet4 Power of Four
import math
class Solution:
    def isPowerOfFour(self,num):
        self.num=num
        if num > 0:
            return num == 1 or num == 4 or (math.log(num,4))-int(math.log(num,4))==0
			
-----leet5 Add & Search in DS [CHECK]
import re
class WordDictionary:

    def __init__(self):
        self.arr=[]
        
    def addWord(self, word):
        self.arr.append(word)
        
    def search(self, word):
		for i in self.arr :
			val=re.fullmatch(word,i)
            if val != None:
                return True
                break
        return False
        
		
----- leet6 Find duplicates in array
class Solution:
    def findDuplicates(self,nums):
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and nums[i] not in res:
                res.append(nums[i])
        return res
		
		
----- leet7 Vertical traversal of Binary Tree [CHECK]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

