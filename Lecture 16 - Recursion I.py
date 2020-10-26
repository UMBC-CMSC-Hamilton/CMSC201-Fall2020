def pointless_recursion(x):
    if x > 0:
        return pointless_recursion(x - 1)
    else:
        return 0


def rec_fact(n):
    if n > 0:
        # recursive step has some recursion
        temp = n * rec_fact(n - 1)
        # print(temp)
        return temp
    else:
        # base step doesn't have recursion
        return 1


def infinite_recursion(n):
    print('cant stop wont stop')
    return infinite_recursion(n)


def iterative_factorial(n):
    """
        a better solution because it doesn't involve recursion.
    """
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


for k in range(10):
    print(rec_fact(k), iterative_factorial(k))


# print(infinite_recursion(10)) RecursionError

# this will go "more forever"
# while True:
#     print('cant stop wont stop')


def recursive_fibonacci(n, step=0):
    if n in [1, 2]:
        return 1
    else:
        # recursive case
        print('\t' * step, 'calling fib on', n - 1)
        a = recursive_fibonacci(n - 1, step + 1)
        print('\t' * step, 'calling fib on', n - 2)
        b = recursive_fibonacci(n - 2, step + 1)
        return a + b


def recursive_fibonacci_dynamic(n, prev_solutions):
    if n in prev_solutions:
        return prev_solutions[n]
    elif n in [1, 2]:
        return 1
    else:
        # recursive case
        b = recursive_fibonacci_dynamic(n - 2, prev_solutions)
        if n - 2 not in prev_solutions:
            prev_solutions[n - 2] = b
        a = recursive_fibonacci_dynamic(n - 1, prev_solutions)
        if n - 1 not in prev_solutions:
            prev_solutions[n - 1] = a
        print('recursive on', n)
        return a + b


def iterative_fib(n):
    fprev = 1  # F_0 = 0
    fprevprev = 1  # F_1 = 1
    current = 1

    for i in range(3, n + 1):
        current = fprev + fprevprev
        fprevprev = fprev
        fprev = current

    return current


x = int(input('What fib number do you want? '))
while x != -1:
    print(recursive_fibonacci_dynamic(x, {}), iterative_fib(x))
    x = int(input('What fib number do you want? '))

# factorial was a single branching of recursion
# fibonacci was a true "branching recursion"
# fib(n) -> fib(n - 1) + fib(n - 2)

# abcba, abcdcba, etc

# yes, slices
# check first and last characters, if they're the same, then strip off and keep going
# otherwise not a palindrome
a = "aabbaa" ""


def recursive_palindromes(a_string):
    # a_string[-1] last element in the string
    print(a_string)
    if not a_string:
        # need to check this is because a null-string is a palindrome
        # index errors will happen if you don't do this
        return True
    elif a_string[0] == a_string[-1]:
        # a slice takes the first element (1) but not the last element -1 so... strips off first and last char
        return recursive_palindromes(a_string[1: -1])
    else:
        # they weren't equal this is not a palindrome
        print(a_string, 'is not a palindrome')
        return False


def iterative_palindrome(a_string):
    for i in range(len(a_string)):
        # this isn't a slice, this is indexing
        if a_string[i] != a_string[len(a_string) - 1 - i]:
            return False
    return True
# [::-1] might be forbidden but yes


def slicy_iter_palindrome(a_string):
    # right solution in python, but most languages don't have this feature
    # [::-1] doesn't exist in a lot of languages, actually secretly:
    # it's doing something more like the above function
    if a_string == a_string[::-1]:
        # more slices you do like this in your python, the less readable your code will be overall
        # use it sparingly, don't make all your code into this.
        return True
    else:
        return False

s = input('Tell me a string: ')
while s != 'quit':
    print(recursive_palindromes(s))
    s = input('Tell me a string: ')
