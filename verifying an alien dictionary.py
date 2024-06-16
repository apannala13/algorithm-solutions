

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}

        for idx, char in enumerate(order):
            hashmap[char] = idx 

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if hashmap[word1[j]] < hashmap[word2[j]]:
                    break #valid order 
                elif hashmap[word1[j]] > hashmap[word2[j]]:
                    return False 
            
            #e.g. apple, app.
            #word1 is greater and apple[app] == app, apple comes first.
            #false as app should come before.
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False 
        return True 
        
