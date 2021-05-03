from collections import Counter


a = 'Today is a great day to learn Python! A very good day!'
b = a.lower().replace('!', '').split()
c = Counter(b)

print(c)