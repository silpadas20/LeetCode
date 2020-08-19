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