
# this local variable n is called a parameter
def fibonacci_calculator(n):

    # doesn't do anything
    pass  # this is a placeholder for this position at this tab level
    if n == 0 or n == 1:
        # return does not print
        return 1
    else:
        # fib(n) = fib(n - 1) + fib(n - 2)
        # Fibonacci numbers are numbers that start a sequence
        # 1, 1, 2, 3, 5, 8, 13, 21, ...
        # rule is that after the first two numbers 1, 1, two previous added
        previous = 1
        current = 1
        for i in range(n - 2):
            temp = current
            current = current + previous
            previous = temp

        return current
    # all the local variables in here leave "scope"
    # they are no longer defined.

"""
# totally allowed, i've taught this a few times already
for i in range(1, 17, 3):
    print(i, end=" ")
    i = 2 * i + 1
    print(i)
"""

i = 0
my_string = input('tell me string: ')
new_string = ''
while i < len(my_string):
    new_string += my_string[i]
    if my_string[i] == 'a':
        i += 2
    else:
        i += 1

print(new_string)

for t in range(4):
    f_int = int(input('Tell me an integer: '))
    # when you pass something into a function, it's called an argument
    print(fibonacci_calculator(f_int))


# C/C++, other languages which don't come with a string class or .lower()

def is_upper(my_char):
    if 65 <= ord(my_char) < 65 + 26:
        return True
    else:
        return False


def lower(the_string):
    # we want to test and see if we find an upper case letter
    new_string = ''
    for char in the_string:
        # upper case, not going to use the is_upper()
        if is_upper(char):
            # lower case and upper case differ by 32 :) 2^5, nice
            new_string += chr(ord(char) + 32)
        else:
            new_string += char

    return new_string
    # return is the only way that a function can communicate with outside code


# prime my input
s = input('Enter string to lowerify: ')
while s != 'stop':
    the_lower_string = lower(s)
    print(the_lower_string)
    s = input('Enter string to lowerify: ')

print(ord('a') - ord('A'), ord('z') - ord('Z'), )


# whenever you call this function, you know that you only have to debug this line once...
def distance(x, y, z):
    return x**2 + y**2 + z**2

# functions don't need returns, but if they don't have them, they're going to return None
"""
def init_server(server_address):
    server.connect(server_address)
    server.init(username, password)
    server.whatever()
"""

# last thing i want to talk about is mutability.
# probably going to end the lecture at about 1:50 today... i have a meeting


def change_me_int(x):
    # ints, bools, floats, and strings, the local variable x here is a copy of the global
    # immutable, they aren't changed
    # we can modify it and it won't mess with the original
    x += 5
    return x


x = 2
print(change_me_int(x), x)
x = change_me_int(x)
print(x)


def change_me_list(my_list):
    # since lists are mutable, this is actually a reference to the original object
    # dictionaries are mutable, classes are mutable, for the future
    my_list.append(3)
    my_list.append('Robot')

    return my_list

# this my list
the_global_list = ['a', 2, 'b', '3', 'destruct']
change_me_list(the_global_list)
print(the_global_list)

