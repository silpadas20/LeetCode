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