import re
import collections
words = re.findall('\w+', open('hamlet.txt').read().lower())
print collections.Counter(words)

#this code opens hamlet.txt and prints the most commonly used words with number of used times
#hint: you need hamlet.txt
