# Anagrams (Frequency)

from collections import Counter

word1 = "silent"
word2 = "listen"

word1 = sorted(word1)
print(word1)                            # Output: ['e', 'i', 'l', 'n', 's', 't']


word2 = sorted(word2)
print(word2)                            # Output: ['e', 'i', 'l', 'n', 's', 't']

word1_counter = Counter(word1)        
print(word1_counter)                    # Output: Counter({'e': 1, 'i': 1, 'l': 1, 'n': 1, 's': 1, 't': 1})
word2_counter = Counter(word2) 
print(word2_counter)                    # Output: Counter({'e': 1, 'i': 1, 'l': 1, 'n': 1, 's': 1, 't': 1})