# what is print?

# print is an internal python command
print('this is a string')  # these are identical from python's perspective
print("this is a string")
# in language like C++, char 'c' "for a full string with multiple characters"
# in python however, there is no difference... there is no single char in python**

# a string is a sequence of characters, list, array, anything like that

# integers, floating point numbers (a number with a decimal on it)
print(5, 4.28812, True, False)

# True, False are special keywords, not just the string "True" and "False"
print('hello')
# cast whatever is in here to a string if possible
print(str('hello'))
# print(str(hello))  # python thinks that hello is a variable
# nothing identical

# print sends data to stdout
print('this', 'is', 'a', 'way', 'to', 'print', 'things', 17)

# don't need to cast when you print
x = 5
print(x)
# what does this code do?
# it declares a variable with python "there is something now called x out there"
# we are going to assign 5 into the variable x.
# variables in python don't really have type

x = "hello there i am now a string"
print(x)
x = 3.141592653589793238
print(x)
# not like C++, Java, C#, C, Rust, tons of others - typed languages
# languages like Python, Ruby :) are non-typed

y = 2
print(y, type(y))
y = 'hello'  # not possible in C++, Java, in Python it's totally ok
print(y, type(y))
# being a non-typed language doesn't mean there isn't type, what it means is that
#   variables can change their type

# string concatenation <-- + operator is smashing these strings together
print('this' + 'is' + 'a' + 'string')
# either really...
print('this ' + 'will ' + 'be ' + 'output ' + str(17))
print('this ' + 'will ' + 'be ' + 'output ' + '17')  # <-- usually 17 will be in some variable

output = 17
print('the output that i care about is: ' + str(output))

# printf C-style
print('the output that i care about is: %d' % output)
print('the output that i care about is: {}'.format(output))
# 4-5 different ways to do the identical thing...
print("you can use double quotation marks as well")  # this is fine.

# escape sequence
print("As Shakespeare says: \"Tis nobler to endure the slings of...\"")
# \" i am not an end-string thingy, i am a quotation mark
print('\'the same thing works with single quotes\'')

print('\tThis is tab\nand this is endline')
# what if you want to type \ and be safe?
print('\q')  # ok but what if i want: python prefers \\q
print('\\t')  # escape the escape

# \n - newline, \t - tab, \\ - escape backslash, \", \'
print('\\\\\\\n\t\\\n\r\n')  # 6 backslashes, huh... does it print out 5 backslashes, or 3 backslashes?

# in python, you must start and end a string with the same quotation mark, either ' or "
print("this has a quote in it 'as the great men say'")
# \r\n - windows, \n
# good news, \n works in python all the time, never use \r - carriage return

"""
    Multi-line strings
    They can be used as comments
    This is a big comment
    We are about to start input now.
    The header is a comment, of sorts
"""


# in math y = f(x) the variable x gets eaten by f, and spat out as y.  f(x) = x^2, f(2) = 4
# tells the computer "get a line of user input, and then send it back to us"
# input is waiting for a line return (enter)
story = input('Tell me a story')
# program doesn't go on until the user hits enter, hangs (forever or enter)
print(story)

# let's say you dont' want a string as the result to your input statement, let's say you want a number
# now we have to talk about casting, input always produces strings.
# casting the result to int
# good
x_is_an_integer = int(input('Enter an integer'))

# no good
# x_is_an_integer = input(int('Enter an integer'))
# to make a multi-word variable, you have to use _'s in Python, snake-case coding standard
# camelCaseIsStandardInJavaAndJavaScriptAndSometimesInCpp

print(x_is_an_integer, type(x_is_an_integer))
# now i'm safe to do integer calculations with this new integer variable:
print(3 * x_is_an_integer + 5)
# this computes the correct output :)

# always good to put a space at the end of your input prompt
a_float = float(input('Enter a floating point number: '))
print(a_float)


# no double type C++ float 32 bits, double 64 bits.  (IIRC) python does something different for floating precision.
# that was crazy

# boolean is the last type
b = bool('True')
print(b)
b2 = bool("False")
print(b2)
print(bool(''), bool(0), bool(0.0))
# why? the answer is .. we'll talk about this later it's just basically how python determines true/false with values

# variable assignment...
x = 4
y = 5
# can i do : no, why not?
# 2 = z
# LHS = variable we're assigning to
# RHS = value, or variable or calculation, or function, or whatever that will be evaluated...
# LHS <== RHS
whatever_you_want_the_variable_to_be = 3
the_variable = whatever_you_want_the_variable_to_be
print(x + y + 2)

x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
print('the sum of the numbers is', x + y)

# you can do more complicated calculations using parentheses to enforce order of operations
z = (x - y) / (x + y)
print(z)
# the same as doing it in the print statement
# sometimes this is way better, because now you have a variable that remembers the result
# no square brackets until we do lists
# don't use ^ as power, ^ = bitwise xor
print(2 ** (1/2), 2 ** 64, 3 ** 3.2)
# ** is just power, you can use it with integers, floating point exponents
# don't import the math library unless we tell you to
print(2 ** 2 ** 4, 2 ** (2 ** 4))
# python is associating RtL here, which may cause confusion, always use parens when you think there may be an issue.
print(5 - 3 - 2, 5 - (3 - 2), (5 - 3) - 2)
# actually "standard arithmetic order of operations" Generally for arithmetic operations it goes Left to right
# math teachers generally don't teach this...
