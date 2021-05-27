word = input("please type your full name")
g = word[:word.index('g')+1]
a = word[:word.index('a')+1]
y = word[word.index('y'):]
g_replace = "abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ"
a_replace = "bcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ"
y_replace = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ"

for char in g_replace:
    g = g.replace(char,'X')
for char in a_replace:
    a = a.replace(char,'X')
for char in y_replace:
    y = y.replace(char,'X')

g_len = len(g)
a_end = word.index('y')
a1 = word[g_len:a_end]

for char in a_replace:
    a1 = a1.replace(char,'X')

gay = g + a1 + y
print(gay)
















