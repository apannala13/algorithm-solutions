"""
Simple solution to determine anagrams - a word w is an anagram of a word v 
if a permutation of the letters transforming w into v exists.
Same counts..
"""

#returns all possible anagrams
def anagrams(S):
    d = {}
    for word in S:
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = [word]
    return [d[s] for s in d if len(d[s]) > 1] 

result = anagrams(['hello', 'olleh', 'anagram', 'agnaram'])
print(result)
        




#check is both strings are anagrams of each other...
#could use Counter  here, but I prefer hashmap implementation
#due to counter being an oversimplification 
def valid_anagram(s:str, t:str):
    if len(s) != len(t):
        return False
    
    hashS, hashT = {}, {}

    for i in range(len(s)):
        hashS[s[i]] = 1 + hashS.get(s[i], 0)
        hashT[t[i]] = 1 + hashT.get(t[i], 0)


    return True if hashS == hashT else False

res = valid_anagram('hello', 'olleh')
print(res)
