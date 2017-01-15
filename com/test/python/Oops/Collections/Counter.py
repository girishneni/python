from collections import Counter

# dict sub class -- count hashable objects

# counter with lists

list = [1,2,2,3,3,4,3,4,5,5,5,4,5,5,4]
print(Counter(list))

# Counter with strings

strCount = 'aabbbccccddddde'
print(Counter(strCount))

# Counter wiht sentence

sentence = 'How many times does each word show up in this sentence, word times each word each time'
words = sentence.split()
print('word counter:', Counter(words))

c = Counter(words)
print(c.most_common(3))