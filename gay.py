# requests input to "gay-ify"
word = input("please type your full name")
# make the values g, a, and y
# i honestly forgot what these index things mean so
g = word[:word.index('g') + 1]
a = word[:word.index('a') + 1]
y = word[word.index('y'):]
# sets these three values to everything except the letters g, a, and y respectively.
g_replace = "abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ"
a_replace = "bcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ"
y_replace = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ"

# replaces all characters except for g, a, or y with X respectively.

for char in g_replace:
    g = g.replace(char, 'X')
for char in a_replace:
    a = a.replace(char, 'X')
for char in y_replace:
    y = y.replace(char, 'X')

#finding length of the g string(lol), and where the a value ends,
# and making a1 idk you can figure it out better than i can explain it

g_len = len(g)
a_end = word.index('y')
a1 = word[g_len:a_end]

for char in a_replace:
    a1 = a1.replace(char, 'X')
# concatenating and printing obvi
gay = g + a1 + y
print(gay)
