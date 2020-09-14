# pep8 convention for spacing of things
this_is_var = 3 + 5
# spaces between operators and spaces between the equal sign and variables.
# avoid:
x = 5 + 2
# ctrl+alt+L

# 4 vs 4.4
print(22 // 5, 22 / 5)
# // -> ints rounded down 5.9 -> 5 (same as truncation)
# / -> floats, even if the thing divides evenly

# computes the largest whole number for which 15.4 = 3.2(W) + R, 0 <= R < 3.2
print(15.4 // 3.2)

print(7 // 2, 7 % 2)
# note that this spits out a float, not an int
print(15 / 3)

# in python you can do some weird stuff with mod:
print(5.3 % 1.25)
# we get round off error, 0.3 = 0.2999999....8
# finite representation in binary of 0.3 is not possible
# not going to use this feature in hws or projects (probably very unlikely)
# most programming languages do not support float-mod

print(3 < 5)
print('hello' < 'goodbye')
print("z" < "a")
# what about this one?
print("Z" < "a")
# why? based on ascii values at least for the letters/symbols with ascii values
# capital Z is a value of 90, lower case a is a value of 97
print(ord("Z"), ord("a"))
# bad:
# print(ord('hello'))

# different types, so maybe false? but they are equal as numbers, so maybe true... hmm...
print(3 == 3.0)

# chr(int ) -> char
print(chr(65), chr(97))
# not really going to use this very much this semester, it's good to know

a = 3
b = 0
if a and b:
    print('a and b are true')
else:
    print('a and b are not true')

# its not that weird... when you evaluate a variable for true/false-ness

if True and False:
    # never print sicne T and F == F
    print('happy')

# '' is False, not False == True, so... not '' == True
if not '':
    print('here we are, that is strange')

if 0.0:
    # float zero is false
    print('float zero is true')

# what is the difference?
a = b = 0
if a == b:
    print('a is equal to b')

if a and b:
    # does not print
    print('a is true and b is true')

if None:
    print('None is true')
else:
    print("None is false")

# there is exactly one NoneType object in existence... and that is None
print(type(None))

##### NESTING #####
condition = True

# need the colon at the end
# without the colon this is a compile time error.
if condition:
    # need all code in the if statement to be tabbed in one
    print('a')
    # python is NOT whitespace insensitive
    # everything must be at the same level of tabbed-ness


person = input('What is your name? ')
if person == 'Robert':
    # yes_no is just a variable
    yes_no = input('Do you golf robert? ')
    # == is case sensitive
    if yes_no.lower() == 'yes':
        # or yes_no.upper() == "YES"
        print('hello Robert the Golfer')
        print(yes_no)
    else:
        print('hello Robert, who has no opinion of golf')


x = int(input('Tell me int! '))
if x != 0:
    y = int(input('Tell me another int! '))
    if y / x == 2:
        print('Double')
    else:
        print('not double')
else:
    print('You cannot divide by zero')

s = input('Enter string: ')
if s == 'integer':
    x = int(input('enter an integer: '))
    if x % 2 == 0:
        print('even')
    else:
        print('not even == odd')
else:
    x = float(input('Enter a float: '))
    if x > 0:
        print('positive')
    else:
        print('non-positive (negative or zero)')

# common pitfall
s = input('tell me string: ')
# why!?!?!?
if s == 'hello' or s == 'goodbye':
    print('hi or bye')
else:
    print('neither')

x = 3
# broken
if x == 2 or 3:
    print('x is two or three')
# fixed
if x == 2 or x == 3:
    print('x is two or three')

