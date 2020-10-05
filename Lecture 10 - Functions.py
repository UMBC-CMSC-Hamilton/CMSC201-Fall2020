"""
def test_x_even():
    x = int(input('Tell me x: '))
    if x % 2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')


for i in range(10):
    print('about to call my_function')
    test_x_even()
    print('my_function has returned')

# you have used a ton of functions before...
print('hello')
s = input('Tell me a story: ')
# two built in functions
print(s.lower())
print(s.upper())
"""


def square_me(x):
    print(x ** 2)


square_me(5)
square_me(17)
square_me(21)


# python doesn't actually know what types we expect.
def my_function(x, f, s):
    print(x + 3, 'is an int')
    print(f + 0.21, 'is a float')
    print(s + ' hello', 'is a string')


my_function(3, 6.3, 'whatever')
# this will cause a TypeError my_function(2, 4.1)
# number of arguments must match the number of parameters in the function's declaration

MAGIC_STR = 'magic'


def magic_function(the_string):
    if MAGIC_STR in the_string:
        # don't need to make anything in a print/input prompt as constants
        print('Magic is in the string')
    if '2' in the_string or 'two' in the_string:
        print("There's no such thing as two")


magic_function("Do you believe in magic?")
my_function(3, 5, 'hello')
square_me(21)

something = input('some string')


# something isn't the prompt... it's the "result" of the function

def happy_function(the_string):
    the_string += ' :) \u263a'
    return the_string
    # secret return
    # return None


new_string = happy_function('am i happy? ')
print(new_string)
print(happy_function('happiness is understand that the universe is truly meaningless'))


# the result is lost... :(
# sometimes that's fine, all you care about is printing the result, who cares after that
# but if you need that value, make sure you save that value in a variable, otherwise it vanishes into the abyss

# instead of scope, which is very important...


# this x is a copy of the global x
def change_me(local_x):
    # temporary x called local variables
    # they only exist when the function exists/is being run
    # local variables have a lifespan (scope) as long as the function runs
    # this x is not the global x, it's a local copy with the same name
    local_x += 1
    print('in the function x = ', local_x)
    return local_x


# global variables live as long as the program lives, as soon as they're declared they have no set lifespan until the program ends.
x = 5
change_me(x)
print('outside of the function x = ', x)


# what happens in this case?
# mutability!!!!!!
# int, str, bool, float are all "immutable" in python
# can't change their values


def new_function(x, y):
    if abs(x - y) > 50:
        return 'x and y are far apart'
        print('hi')
    else:
        return 'x and y are close together'


result = new_function(50, 1000)
print(result)

"""
    does not actually change the original string
"""
def change_me_string(the_string):
    # strings are immutable, so this is a copy not the original
    the_string += ' and this too'
    print(the_string)
    return the_string


my_string = 'something something something turtles'
print(change_me_string(my_string))  # this will print out None
# never got reassigned to my_string, so my_string is the same as the original
print(my_string)

"""
    BIG EXCEPTION: lists <--, dictionaries, classes
"""


def change_me_list(a_list):
    # a_list is a secret alias for my_list now
    a_list.append(3)
    print(a_list)
    # we have created a new list, and told a_list now to be an alias for that list
    # we lost track of the old list, and now we have this new thing.
    a_list = ['a', 'b', 'c']
    print(a_list)
    # return a_list


my_list = [1, 2, 3, 4, 5]
# didn't get assigned back to my_list, so how did that happen?
change_me_list(my_list)
# getting dropped, secret is that because the list passed by reference, it is actually a renaming
# mutable things (lists, dictionaries, classes) pass by reference,
# immutables (int, bool, float, str) pass by value (copy of the original)
print(my_list)
# if this makes a copy, then what happens?
# if it uses the original list somehow, it should be [1, 2, 3, 4, 5, 3]

