# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".

s = {}
keys = input().split()
for i in range(len(keys)):
    if (int(keys[i]))%2 == 0:
        s[keys[i]] = 'четное'
    else:
        s[keys[i]] = 'нечетное'
print(s)
