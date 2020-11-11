"""
    What's going to be on the exam next week?

    Dictionaries
    Functions
    Recursion
    Classes
    File IO

    Maybe binary/hex - hard to test this
"""
import random


# start out with functions
def remove_all_as(a_string):  # function definition
    # here
    new_string = ''
    for c in a_string:
        if c not in ['A', 'a']:
            new_string += c

    return new_string  # return statement, function doesn't go on after a return statement
    # down to here, called function body


"""
    recursive function example
    recursion just means a process that calls itself. (processes = functions)  
"""


def binary_search(a_list, find_me, current_pos=-1):
    """
        you're going to start at list size / 2
        if the element we're searching for is bigger than the value at the position, we'll go right
        otherwise we'll go left
        if we find it we'll return True
        if we don't return False

        a_list must be sorted
        looking for 2
        array[2], looking for the value of 2.
        [ 1, 2, 5, 7, 8, 12] current_pos = 3
            return call on the next one
        [ 1, 2, 5, 7, .. ..] current_pos = 3 // 2 = 1
            value is 2, return True
    :param a_list:
    :param current_pos:
    :return:
    """
    if current_pos == -1:
        current_pos = len(a_list) // 2

    if a_list:
        print(a_list, a_list[current_pos])
    else:
        print('empty list')

    if not a_list:
        return False
    elif find_me == a_list[current_pos]:
        return True
    elif find_me < a_list[current_pos]:
        return binary_search(a_list[0: current_pos], find_me, current_pos // 2)
    elif find_me > a_list[current_pos]:
        return binary_search(a_list[current_pos + 1:], find_me, current_pos // 2)


def binary_search_test():
    # this piece of code is technically somewhat forbidden
    # list comprehension, i haven't really taught anything about these.
    # my_list = [random.randint(0, 100) for _ in range(100)]
    # alternative code that doesn't involve comprehensions
    my_list = []
    for i in range(10):
        my_list.append(random.randint(0, 100))

    my_list.sort()  # sort using Timsort combo(merge, insertion)
    print(my_list)
    print(binary_search(my_list, int(input('What do you want to search for? '))))
    # the number of searches is probably something on the order of log_2(len(a_list))
    # calc 1 precalc, T = log n << T = n as n -> infinity


"""
    we want to count the number of times n is divisible by 2, 
    n = 2^k * j where j is odd
"""


def count_twos(n):
    count = 0
    while n % 2 == 0 and n > 0:
        n //= 2
        count += 1
    return count


def count_twos_recursively_for_no_reason(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 1 + count_twos_recursively_for_no_reason(n // 2)
    else:
        return 0


def test_count_twos():
    for i in range(20):
        print(count_twos(i), count_twos_recursively_for_no_reason(i))


"""
    Think of a string problem where you need to slice off the first character.  
"""


def rotation_recursive(a_string, k):
    print(a_string, k)
    # if k == 0 then it's not a rotation, it's the identity
    # if a string is empty, then we don't want to do anything below.
    if k == 0 or not a_string:
        return a_string
    elif k > 0:
        return rotation_recursive(a_string[1:] + a_string[0], k - 1)
    elif k < 0:
        return rotation_recursive(a_string[len(a_string) - 1] + a_string[0:len(a_string) - 1], 1 + k)

def rotation_test():
    # defgabc
    print('The final result is: ', rotation_recursive("abcdefg", 4))
    # the reason why it's wrong is that it's not wrong, i'm wrong, humans are more wrong than code
    print('The final result is: ', rotation_recursive("rotations are made of matrices", 3))
    print('The final result is: ', rotation_recursive("rotations are made of matrices", -3))

"""
    classes first
    
    What is a class?  a class is an object type, making ourselves a blueprint, template (don't think C++), etc.  
    
    What does a class have?
        it has variables, methods (functions)
"""


class InvoluteGear:
    def __init__(self, teeth_one, teeth_two):
        self.upper_teeth = teeth_one
        self.lower_teeth = teeth_two

        self.upper_attach = None
        self.lower_attach = None


class Contraption:
    def __init__(self):
        self.gears = []

    def add_gear(self, gear):
        self.gears.append(gear)
        # might have to do more if we decide that it needs it

    def attach_gears(self, gear_one, one_ul, gear_two, two_ul):
        if one_ul == 'upper' and two_ul == 'upper':
            gear_one.upper_attach = gear_two
            gear_two.upper_attach = gear_one
        elif one_ul == 'upper' and two_ul == 'lower':
            gear_one.upper_attach = gear_two
            gear_two.lower_attach = gear_one
        elif one_ul == 'lower' and two_ul == 'upper':
            gear_one.lower_attach = gear_two
            gear_two.upper_attach = gear_one
        else:
            gear_one.lower_attach = gear_two
            gear_two.lower_attach = gear_one

    def turn_gear(self, gear, num_turns):
        print('We turn our gear ', num_turns, 'times')
        if gear.upper_attach:
            if gear.upper_attach.lower_attach == gear:
                print('The upper attached gear turns', num_turns * gear.upper_teeth / gear.upper_attach.lower_teeth, 'times')
            elif gear.upper_attach.upper_attach == gear:
                print('The upper attached gear turns', num_turns * gear.upper_teeth / gear.upper_attach.upper_teeth, 'times')
                # this is basically the solution...
                self.turn_gear(gear.upper_attach, num_turns * gear.upper_teeth / gear.upper_attach.upper_teeth)
        if gear.lower_attach:
            if gear.lower_attach.lower_attach == gear:
                print('The upper attached gear turns', num_turns * gear.lower_teeth / gear.upper_attach.lower_teeth, 'times')
            elif gear.lower_attach.upper_attach == gear:
                print('The upper attached gear turns', num_turns * gear.lower_teeth / gear.upper_attach.upper_teeth, 'times')

    def display(self):
        for gear in self.gears:
            print("gear: ", gear.teeth_one, gear.teeth_two)


def test_involute_gears():
    # never test anything /s
    gear1 = InvoluteGear(20, 50)
    gear2 = InvoluteGear(30, 47)

    contraption = Contraption()
    contraption.add_gear(gear1)
    contraption.add_gear(gear2)

    contraption.attach_gears(gear1, 'upper', gear2, 'lower')
    contraption.turn_gear(gear1, 12)
    # does that mean it works? no... it means it worked once


"""
    Not going to ask, but this is what i'm thinking because it may be silly/fun
    you could generate some kind of recursive "get number of turns" to see how many times all the gears connected to the forced gear
"""

"""
    Let's discuss file IO
"""

mode = 'r'  # read (sets the file pointer to the start of the file, does not modify the file in any way)
mode = 'w'  # write (opens, and clears the file, then sets the file pointer to the start of the file, because there isn't anything left).
mode = 'a'  # append (opens the file, allows you to write, but sets the file pointer to the end of the file)
# 'w' and 'a' will create the file if it doesn't exist
# 'r'

with open('the_file_name.txt', 'w') as the_file:
    file_text = input('What do you want to write to this great file? ')
    while file_text != 'quit':
        the_file.write(file_text + '\n')  # write doesn't put a '\n' into the file, unlike print
        file_text = input('What do you want to write to this great file? ')

    # but wait don't i have to close the file? not with with :-)
    # this with statement will run an exit method, and then the exit method closes the file handle.


print("___FOR LINE IN FILE___")
with open('the_file_name.txt', 'r') as the_file:
    for line in the_file:
        print(line)


print("___READLINE_WITH_WHILE___")
with open('the_file_name.txt', 'r') as the_file:
    the_line = the_file.readline()
    while (the_line):
        print(the_line)
        the_line = the_file.readline()
        # readline doesn't strip off the '\n'
        # if you don't want this then set end=""

print("___READLINES___")
with open('the_file_name.txt', 'r') as the_file:
    print(the_file.readlines())
    # this creates a list of strings, separated by what were the '\n' characters


print("___READ THE ENTIRE FILE___")
with open('the_file_name.txt', 'r') as the_file:
    print(the_file.read())
