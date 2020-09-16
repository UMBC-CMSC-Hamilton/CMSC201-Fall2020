# want to store two things in a variable name, five things, ten things, whatever
a_list = 3
# python doesn't care that we're calling this a_list, it's just an int
a_list = 4
# but (using square brackets, separated by commas):
a_list = [3, 4]
print(a_list)

# notice that python isn't very strict about lists being all the same type.
test_list = ['hello', 3, 3.2, True, False, None, 'whatever']
print(test_list)
# generally you want lists to be of the same type.  know that you can perform operations on each element

# recall:
if 0 or '' or 0.0 or None or False:
    # nope
    print('none of this will print')

# if you just want python to evaluate a variable, just let it alone
if []:
    print('[] is true')
else:
    print('[] is false')

# what if you want to get say the "3rd element?"
a = [1, 2, 3, 4, 5]
# indexing starts at zero
# 1st element - index 0
# 2nd element - index 1
# 3rd element - index 2
# 4th element - index 3
# 5th element - index 4
print(a[2], a[3], a[0])

# to index into a list, you add the square brackets and put the index in
# print(a[17])
# gives an index error

a[4] = 31
print(a)
a[2] = 17
print(a)

my_index = 3
# some code in here that makes it seem more magical
a[my_index] = 14
print(a)

a.append(3)
a.append(17)
a.append(65537)
a.append('nope')
a.append('daffodil')
print(a)
# cool right?

# GENERALLY NOT TAUGHT, DONT USE THIS:
a.insert(3, 'now i am at index 3')
print(a)
# END OF NOT USING THIS

list_of_movies = ['The Matrix', 'Hunger Games', 'Blade Runner', 'Blade Runner 2049', 'Fight Club', 'Night.B.Christmas', 'Coraline', 'Star Trek: WOK', 'Ex Machina']
# not disappointed
# movie is a variable, and it gets reset every time you go through the for loop to the next value
# in the list...
# for takes care of making the variable, change the var to new values
for movie in list_of_movies:
    print(movie)

# does movie still exist?
print(movie)

print(type('hello'), type([]))

for c in 'hello string':
    print(c)

print('hello'[3])
# a string is TECHNICALLY not a list of characters... but really yes

s = 'this is a string not a list'
ell_of_s = list(s)
print(s)
# sometimes you might need this
print(ell_of_s)

list_of_numbers = [3.14, 1.618, 2.718, 0.577]
for num in list_of_numbers:
    print(num, type(num))

# this is fine... nothing wrong with it
list_of_digits = list(str(2017))
print(list_of_digits)

word_list = ['trap', 'squalid', 'stamp', 'injure', 'plane', 'kindhearted', 'treat', 'bomb', 'scold', 'wrap', 'preach', 'influence', 'like', 'arm', 'damaging', 'yam', 'authority', 'loud', 'present', 'wren']

for word in word_list:
    # notice that the if statement is tabbed in one
    if 'a' in word:
        # code in the if statement is tabbed in two.
        print('The word', word, 'has an a in it.')

# GIGANTIC and pointless debate about whether tab > spaces, spaces > tabs, if it should be 2, 3, 4, 5 spaces
# no... it has to be consistent...
# the reason why i think that is because modern IDEs allow you to display a tab as however many spaces you want!!!
# but the python community in general has decided on 4 spaces...

# goes up to 10, does not include 10
for i in range(10):
    print(i)

# Gauss sum, 201, 203, 341 whatever
# G_n =  1 + 2 + 3 + ... + (n - 1) + n
# 1 + 2 + 3 + 4 + 5 = 15
# 1 + 2 + 3 + 4 + ... + 50 = 1275

n = int(input('Enter n: '))
# go up to n + 1 but not include n + 1, stops at n.
the_sum = 0
# avoid using the variable names: min, sum, max
for i in range(n + 1):
    # let me tell you what += does
    # the_sum = the_sum + i
    the_sum += i
    # *=, %=, **= all of these exist.
print(the_sum)


a_list = [1, 2, 3, 4, 5]
for x in a_list:
    print(x)
    # x = x ** 2
    x **= 2
    print(x)

# the original list is unchanged!!! why!??!?!?!
print(a_list)
# mutability of the element in the list
# if the element is mutable, then it can be changed
# if not, the element is copied

# basic types, int, float, string, bool are all immutable, which means they cannot be changed
x = x + 2
# its creating a new integer, adding two to the old x, and then setting a new value

rando_list = ['hello', 'robot', 'tensor', 'sphere']
for s in rando_list:
    # does string concat
    s += ' and more'
    print(s)

# reason why this is unmodified is because strings are basic types, therefore immutable.
print(rando_list)

# is there a mutable thing in the universe? yes, lists are
list_of_lists = [[1], [2], [3], [4], [5]]
for sub_list in list_of_lists:
    # sub_list here is NOT a copy, it's actually a reference,
    print(sub_list)
    sub_list.append(1729)
    print(sub_list)

print(list_of_lists)

# what is going to happen here?
first_list = [1, 2, 3, 4, 5]
# reference (shallow copy - generally not going to say this).
# not a copy
second_list = first_list
# this is a copy
# not modified, use the list constructor, it makes a copy
third_list = list(first_list)

second_list[2] = 17
print(first_list)
print(second_list)
print(third_list)

