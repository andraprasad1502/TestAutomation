######################################################################
"""
1.)even or odd
"""
print('*' * 100)
number = 5
if number % 2 == 0:
    print("1. Even Number")
else:
    print("1. Odd Number")

######################################################################
"""
2.)arm strong number(153)
"""
print('*' * 100)
number = 153
list_a = str(number)
number2 = 0
for i in list_a:
    number2 += int(i) ** 3

if number == number2:
    print("2. Arm strong number")
else:
    print("2. Not an arm strong number")


######################################################################
"""
3.)fibinbocci series up to 100
ex: 1, 1, 2, 3, 5, 8, 13, 21. .... 
"""
print('*' * 100)
number = 100
num1 = 0
num2 = 1
list_a = []
while num1 + num2 < number:
    list_a.append(num1+num2)
    num1, num2 = num2, num1+num2
print("3. ", list_a)


######################################################################
"""
4.)prime number or not
"""
print('*' * 100)
number = 43
for i in range(2, number // 2 + 1):
    if number % i == 0:
        print("4. Not a Prime Number")
        break
else:
    print("4.Prime Number")


######################################################################
"""
5.)vowel or consonant
"""
print('*' * 100)
c = 'h'
if c.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("5. Vowel")
else:
    print("5. consonant")


######################################################################
"""
6.)sum of digits in given number
"""
print('*' * 100)
number = 1256
tot = 0
for i in str(number):
    tot += int(i)
print("6. ", tot)


######################################################################
"""
7.)sum of given ten numbers or numbers in the list
"""
print('*' * 100)
number = 10
tot = 0
for i in range(1, number+1):
    tot += int(i)
print("7. ", tot)

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tot = 0
for i in list_a:
    tot += int(i)
print("7. ", tot)


######################################################################
"""
8.)reverse number
"""
print('*' * 100)
number = 123
number = str(number)[::-1]
number = int(number)
print("8. ", number)


######################################################################
"""
9.) swapping
"""
print('*' * 100)
a = 2
b = 3
a, b = b, a
print("9. ", a, b)


######################################################################
"""
10.)searching element in given string or list
"""
print('*' * 100)
string = "helloworld"
c = 'd'
if c in string:
    print("10. ", c, " found in the string ", string)
else:
    print("10. ", c, " not found in the string ", string)


######################################################################
"""
11.)sorting
"""
print('*' * 100)
list_a = [2, 4, 5, 1, 3, 8]
print(sorted(list_a))
print(sorted(list_a, reverse=True))

for i in range(0, len(list_a)):
    for j in range(i, len(list_a)):
        if list_a[i] > list_a[j]:
            list_a[i], list_a[j] = list_a[j], list_a[i]
print("11. ", list_a)


######################################################################
"""
12.)palindrome
"""
print('*' * 100)
string = "Helloworld"
if string == string[::-1]:
    print("12. Palindrome")
else:
    print("12. Not a Palindrome")


######################################################################
"""
13.) reverse a string
"""
print('*' * 100)
string = "Helloworld"
print(string[::-1])
i = 0
j = len(string) - 1
string = list(string)
while j > i:
    string[i], string[j] = string[j], string[i]
    i += 1
    j -= 1
print("13.", "".join(string))


######################################################################
"""
14.) remove duplicate in list and string
"""
print('*' * 100)
string = "helloworld"
string2 = []
for c in string:
    if c not in string2:
        string2.append(c)
string = "".join(string2)
print("14.", string)

list_a = [1, 2, 3, 4, 2, 4, 6]
list_b = []
for i in list_a:
    if i not in list_b:
        list_b.append(i)
print(list_b)


######################################################################
"""
15.) list comprehension example
"""
print('*' * 100)
list_a = [1, 2, 3, 5, 4, 6, 7, 8]
list_even = [i for i in list_a if i % 2 == 0]
print("15.", list_even)


######################################################################
"""
16. Dictionary comprehension example
"""
print('*' * 100)
string = "helloworld"
dict_a = {c: string.count(c) for c in string}
print("16. ", dict_a)


######################################################################
"""
17. count occurrence of each character in string
"""
print('*' * 100)
string = "pythonlanguage"
dict_a = {c: string.count(c) for c in string}
print("17. ", dict_a)
dict_b = {}
for c in string:
    if c in dict_b.keys():
        dict_b[c] += 1
    else:
        dict_b[c] = 1
print("17. ", dict_b)


######################################################################
"""
18. find count of given character in string
"""
print('*' * 100)
string = "helloworld"
c = 'o'
count = 0
for ch in string:
    if c == ch:
        count += 1
print("18. ", count)


######################################################################
"""
19. Tuple Unpacking
"""
print('*' * 100)
a, b, c = (1, 4, 5)
print("19.", a, b, c)
# a, b, c = (1, 4)   # error
# a, b = (1, 5, 6)   # error


######################################################################
"""
20. shallow copy and deep copy list
"""
print('*' * 100)
list_a = [1, 2, 3, 4, 5, 6]
list_b = list_a
list_b[0] = 10
print("20.", list_a, list_b)

list_a = [1, 2, 3, 4, 5, 6]
list_c = list_a[:]
list_c[0] = 20
print("20.", list_a, list_c)



