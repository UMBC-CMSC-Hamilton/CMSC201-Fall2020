
# you can print
print('hello', 3, 1.2, True, False, None)
# you can input
s = input('tell me a thing: ')
print(s)
# remember we can cast into int, float, bool (don't do that)
the_integer = int(input('Tell me an integer: '))
the_float = float(input('Tell me a float: '))
print(the_integer, the_float)
# this is what we can do so far

# basically the only logical control in python
condition = False
# if condition is True, it will execute, if False it will not execute
if condition:
    print('the condition is true')

x = int(input('Enter an int: '))
if x > 0:
    print('x is positive')

# single equals sign
this_variale = 2
the_string = input('tell me a string: ')
# double equals is a comparison equals, not assignment
# double equals...
if the_string == 'hello there':
    print('General Kenobi, I\'ve been expecting you.')
# when you test for string ==, the case matters

user_input = input('What do you want to do? ')
if user_input == 'quit':
    print("Ok we are done now")

# let's test if an integer is even or odd... errrr...
# we have some extra operation to do this kind of thing...
# it's called mod, %
"""
x = 1
d = 1
while d != 0:
    print(x % d)
    x = int(input('Enter int: '))
    d = int(input('Enter divisor: '))
"""
# whenever you integer divide x / d, you're going to get a remainder
# 5 / 2 = 2 R 1, 5 = 2(2) + 1, so the remainder is 1
# mod doesn't care about the quotient, it only cares about the remainder
# 17 / 5 what is this? 3(5) + 2 <-- what  mod gives us

# what happens when we do -2 % 3? 3 = 0(3) - 2, 3 = -1(3) + 1
# your teacher should have said, R >= 0
# ask Ben's question: how do we write an if statement that checks if an integer is even/odd?
# definition of even vs odd, is:
# even n = 2k for some integer k, means, n mod 2 == 0
# odd n = 2k + 1 for some integer k, meaning that n mod 2 == 1

f = float(input('Tell me an integer: '))
# converting from a float (has decimals) -> int (without decimals)
n = int(f)
print(f, n)
if n % 2 == 0:
    # only this, when true
    print("it's even")
else:
    # jump to here and execute this code, not the if code
    print("it's odd")
# if statements don't require else, but if you want a catch-all at the end, this is how to do it

# this is works as code, it's also correct as logic

# doesn't work in other languages, python special
print(f % 3)
# computers can't store floats exactly (sometimes, most of the time)
f = 1 / 2

# elif
# september starts on a tuesday
n = int(input('Enter a day of this september: '))
# there are 7 days of the week
# else if, elif, you can have 100, 1000
# if you have 1000 of them, we will take off points
# you're doing it wrong if you have that many
# limit is ~20, even 20 is ridiculous
if n % 7 == 1:
    print('Tuesday')
elif n % 7 == 2:
    print('Wednesday')
elif n % 7 == 3:
    print('Thursday')
elif n % 7 == 4:
    print('Friday')
    # hacker bug prevented
    n = 5
elif n % 7 == 5:
    print('Saturday')
elif n % 7 == 6:
    print('Sunday')
else:  # this is what happens when n % 7 == 0
    # equivalent: elif n % 7 == 0:
    print('MONDAY!!!')

# let's say you want both blocks to be executed
x = int(input('Enter num: '))
if x > 0:
    print('x is positive')
# no elifs, no else
# two separate if statements
# then this one evaluates
if x > 1:
    print('x is bigger than 1')

# talk a little bit about logical operators
# and, or, not


s = 'hello'
x = 2
y = 5
# C++ Java people &&, || and and or, no, not in python sorry
if s == 'hello' and x == 2 and y == 5:
    print('Yep we\'re good.')
else:
    print('no good')

# double equals TESTS for equality
# single equals ASSIGNS LHS <== RHS
x = 17
s = 'blah'
# what happens if we change this to or
print(s == 'hello', x == 2, s == 'hello' or x == 2)
if s == 'hello' or x == 2:
    print('Yep we\'re good.')
else:
    print('no good')

# logical operators have low precedence, what the heck does that mean?
"""
HIGH
Arithmetic
() - first
** - exponents pow is a function in the math module, we use **
*, /, //, %
+, -
Equivalence / Comparisons
<, >, >=, <=, !=, == - same level of precedence
Logical Operators
not
and/or
LOW 
Generally, order of operations goes from L -> R
    ** -> R-> L
"""

if (x == 2) and ((x + y) > 18):
    print('hi')

