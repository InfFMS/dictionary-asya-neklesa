# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

# шифроватор
d1 = {'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%', 'f': '^', ' ': ' '}
text1 = list(input())
code1 = list(['']*len(text1))

for i in range(0, len(text1)):
    code1[i] = d1[text1[i]]
print(code1)

#душифроватор
d2 = {'!': 'a', '@': 'b', '#': 'c', '$': 'd', '%': 'e', '^': 'f', ' ': ' '}
code2 = list(input())
text2 = list(['']*len(code2))
for i in range(0, len(code2)):
    text2[i] = d2[code2[i]]
print(text2)