
class Text:
    """
    A class to simulate T9 predictive text functionality for a traditional mobile phone keypad.
    """
    def __init__(self):
        self.t9 = "22233344455566677778889999"  # Mapping for 'a' to 'z'

    def letter_to_digit(self, x):
        assert 'a' <= x <= 'z', print(f'out of bounds :{x}') #valid letter
        # Convert letter to corresponding T9 digit based on position in the alphabet.
        return self.t9[ord(x) - ord('a')] #unicode of character minus unicode of 'a'
    
    def code_word(self, word):
         # Convert a whole word to T9 code by mapping each letter to its T9 equivalent.
        return ''.join(map(self.letter_to_digit, word))
    
    # Calculate the weight for all prefixes of each word based on their given weights.
    def predictive_weight(self, dic):
        total_weight = {}
        for word, weight in dic.items():
            prefix = ""
            for x in word:
                prefix += x
                if prefix in total_weight:
                     # Add to the existing weight if this prefix has already been encountered.
                    total_weight[prefix] += weight
                else:
                    # Initialize the weight for new prefixes.
                    total_weight[prefix] = weight
        # Determine the most predictive word for each numeric code.
        prop = {}
        for prefix in total_weight:
            code = self.code_word(prefix)
            # Keep only the most weighted word for each numeric code.
            if code not in prop or total_weight[prop[code]] < total_weight[prefix]:
                prop[code] = prefix
        return prop
   
    def propose(self, prop, seq):
        # Return the most likely word or None if the sequence does not exist in prop
        return prop.get(seq, None)
        
if __name__ == "__main__":
    t = Text()
    dic = {"hello": 10, "good": 5, "go": 15, "he": 8}
    prop = t.predictive_weight(dic)
    print(t.propose(prop, "43"))  
    print(t.propose(prop, "4663"))
