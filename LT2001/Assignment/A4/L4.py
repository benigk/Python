text = 'behalve den man die de sarphatistraat...'
ctrs = {}
for letter in text:
    if letter not in ctrs:
        ctrs[letter] = 0
    ctrs[letter] = ctrs[letter] + 1
print(ctrs.items())