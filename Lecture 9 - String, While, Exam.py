hello_string = 'i_am_a_string'

# you can use a string as a list
print(hello_string[3])
print(hello_string[9])
# access string characters at their index
# hello_string[3] = 'a'
# basic data types are "immutable" - cannot modify a string in python
a_string = 'x'
for i in range(10):
    # in ascii / in unicode, the first 128 characters of unicode are the ascii characters... so. yes
    a_string += chr(97 + i)  # a_string = a_string + 'a'
    # each time this happens, a new string object is created
    print(a_string)
# C++, Java, etc, you can change string
# python you can't because they're immutable
# x += 1 ==> x = x + 1 shorthand for that

# print(a_string[17])  # out of bounds, right? 17 > 11
# IndexError: string index out of range

for character in a_string:
    print(character, end=" | ")

# sometimes you might need this kind of construction...

# count vowels:
vowels = ['a', 'e', 'i', 'o', 'u']
# we are not going to talk about y
# who cares
story = input('Tell me a story: ')

num_vowels = 0
for char in story:
    if char in vowels:
        num_vowels += 1

print(story, 'has', num_vowels, 'vowels.')
# the point is, we counted up the vowels in the story.

# let me show you how to replace a character in a string.
# you might think to yourself, hey:::!

#  other way to do it is this:
replace_string = 'Energize, that\'s what we do in this room.'
# convert this into a list:
listified_string = list(replace_string)
print(listified_string)
# this does what we want now...
listified_string[3] = 'a'
print(listified_string)
# that's pretty crap, we want to make a string out of it again
# the join function!
# separator.join(a_list_of_strings)
# the separator is a string
print('||'.join(listified_string))
print(''.join(listified_string))
# the string object has the method "join" not the list object
# Eventually you get used to it.
# not list.join() its str.join()
# typeerror
# join eats a list, gives you back a single string
my_strings = ['Once', 'upon', 'a', 'time', 'in', 'a', 'galaxy', '...']
print(" ".join(my_strings))
# this is pretty terrible
my_separator = "-|-"
print(my_separator.join(my_strings))

# let's talk about the opposite operation, split(str) -> list[str]
the_new_story = input('Tell me another story: ')
print(the_new_story.split())
# by default it splits on whitespace

# there is an argument in split.
abra_split = 'abracadabra'.split('a')
print('abracadabra'.split('a'))
print('a'.join(abra_split))
# ValueError: empty separator
# print('abracadabra'.split(''))
# that's what you want basically
abra_split = 'abracadabra'.split('z')
print(abra_split)

# you can split on more than one character
print('aabracadaabra'.split('aa'))
# you can split like this, but generally you should know what it is you're doing if you want this

# now let's talk about strip, it removes whitespace from both ends of the string
my_whitespace_string = '\n\na\ta\ta  a\taaa   a\t'
# >> kills off whitespace until it hits a non-whitespace character <<
print(my_whitespace_string)
print(my_whitespace_string.strip())

s = input('enter string')
new_s = ''
found_first_char = False
for c in s:
    if c not in [' ', '\t', '\n', '\r'] or found_first_char:
        new_s += c
        found_first_char = True
        # i need to take everything after the first character, including whitespace

print(new_s)


s = 'this_is_a_long_string'  # end ' not part of the string
print(len(s))
# this is not a great exam problem, slightly too tricky for me.
for i in range(1, 17, 3):
    print(s[i], end=' ')
    # SL 0          SL 1         sublist 2        sublist 3
L = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(5):
    print(L[(2 * i + 1) % 4][(5 * i + 2) % 4])

# what's going to happen here?
# i = 0, L[1][2] = 7, neat
# i = 1, L[3 % 4][7 % 4] = L[3][3] = 16
# i = 2, L[5 % 4][12 % 4] = L[1][0] = 5
#           5/4 = 1x R 1yes, 5 % 4 = 1
#           12/4 = 3no R 0yes 12 % 4 == 0
#           x/y -> (floats), x//y -> int
# i = 3, L[7 % 4][17 % 4] = L[3][1] = 14
# i = 4, L[9%4=1][22%4=2] = L[1][2] = 7

# 3d-list
another_list = [[[0, 1], [1, 0]], [[0, 1], [1, 0]], [[0, 1], [1, 0]]]
print(another_list[0][1][0])

# bad because you're redefining a keyword
min = 3
print(min)
"hello" # a literal
x = "hello"  # <=-- a literal
x  # <-- not a literal, it's a string variable with a name

# a literal is something like
# "hello" = x
# 3 = x
# True = x
# 3.141592653589793238 = x
# not a variable which contains a value, but the value itself, hard coded as a string, int, float, bool
print(27 in range(36))
s = 'xylophone zebra'
if 'x' in s and 'y' in s and 'z' in s:
    print('yep')