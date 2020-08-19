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