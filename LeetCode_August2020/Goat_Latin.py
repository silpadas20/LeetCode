class Solution:
    def toGoatLatin(self, s: str) -> str:
        vowels=('a','e','i','o','u')
        res1,res2=[],[]
        num=1
        phrase=s.split()
        for word in phrase:
            if word[0].lower() in vowels:
                word=word+'ma'
                res1.append(word)
            else:
                first_el=word[0]
                word=word[1:]
                word+=first_el + 'ma'
                res1.append(word)
        for word in res1:
            word=word+'a'*num
            num+=1
            res2.append(word)

        return (" ".join(res2))