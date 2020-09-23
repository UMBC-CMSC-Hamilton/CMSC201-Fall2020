# agenda for today:
# bit more about for loops
#   negative step size
# 2d lists -- done with this for now (not done with 2d lists i promise)
# split(), strip() for strings
# while loops a bit

# recall from prior lectures:
the_list = ['x', 'a', 'r', 'b', 't', 'x', 'q', 'y']
# for each loop, not because the variable is each
# because its not an index into the list
# basic types are immutable, int, bool, string, floats
for each in the_list:
    # its kid of a local variable yeah
    print('The letter is', each)

# still exists out here, but little bit dangerous to use it here
print(each)
# code WILL execute, something WILL happen, is it what you expect to happen??

print(the_list)
# for i construction basically always involves range object
for index in range(len(the_list)):
    if the_list[index] == 'q':
        the_list[index] = 'qu'

print(the_list)

print(range(40000000))
# range is actually doing something different than just creating a list...
# not doing this:
# print(list(range(40000000)))

# make a list of elements starting at 17, ending at 100 or so, in increments of 12:

# range(start=0, stop, step=1)
# stop is always excluded
my_crazy_list = list(range(17, 100, 12))
print(my_crazy_list)

# 99% all loops that i ever write are for loops
# 1% are while loops
# but really this isn't a matter of preference as "which thing is better in which situation"

list_of_tens = list(range(10, 100, 10))
# does not hit 100, because it stops there
print(list_of_tens)

# step parameter can be negative...
# not going to execute
for i in range(3, 100, -3):
    # either this could be infinite loop, 3, 0, -3, -6, -9, ... -infinity whatever (x) not this one
    # range could detect that 100 - 3 > 0, step < 0 not do anything... <----
    print(i, end=" ")

for i in range(5, 0, -1):
    # 0 - 5 < 0, step < 0 ok, it'll go
    print(i, end=" ")
    # end= " " changes the endline character from \n to ... whatever you put in

print()
# if you want to get to zero, you need to have the stop = -1, not just the step
for countdown in range(10, -1, -1):
    # really an end-string
    print("T - ", countdown, end=" :: ")
    # because python doesn't really distinguish between characters and strings (95% of the time)

# range can take negative step
print()

"""
    What is a 2d-list?
        a list, where the elements are lists...
        rows and columns 
"""

the_matrix = [[3, 7],  # this is row 0
              [1, 0]]  # this is row 1
print(the_matrix)
# the matrix[0] not just an element, it's the 0th row!!
print(the_matrix[0])
# the matrix[1] is not just an element, it's the 1st row!!
print(the_matrix[1])
#         col    0  1  2
heres_a_grid = [[1, 0, 1],  # row 0
                [2, 3, 0],  # row 1
                [5, 1, 8]]  # row 2

# we access the row first because it's the outer list
# access a list within a list
print('row 1 col 2: ', heres_a_grid[1][2])

# when do you need a 2d list?

# monopoly, does not need a 2-d list for movement.
# you can just use a single list for this
# for instance, chess boards, checkers boards, maze problems, anything with a grid.  (x, y) pos
# go board... everybody loved that project
# go for instance!
# you can but don't

# creates a list of strings that is five long and then outputs the "third" character
"""
list_of_strings = []
for i in range(5):
    list_of_strings.append(input('Enter a string: '))

for string in list_of_strings:
    if len(string) > 3:
        print(string[3])
"""

checkers_board = []

for i in range(8):
    new_list = []
    for j in range(8):
        # if (i + j) % 2 == 1 then it is is True,
        if (i + j) % 2:
            new_list.append('*')
        # this is in the case where it's even/false/whatever
        else:
            new_list.append('x')

    checkers_board.append(new_list)

# i don't even know what this line does
print(' ', ' '.join(list([str(x) for x in range(8)])))
# it doesn't exist

# this is now completely legal for the course
# index is just the rows
for row in range(len(checkers_board)):  # each row, from 0 to 7
    # join will be explained next week
    print(row, end=" ")  # row number
    # checkers_board[index] is the sublist at row=index
    # not always true
    for col in range(len(checkers_board[row])):
        print(checkers_board[row][col], end=" ")
    print()

two_d_list = [
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6],
    [6, 5, 4],
    [7, 8, 9]
]

print(len(two_d_list))
# this is fine
for row in range(len(two_d_list)):
    # print(len(two_d_list[row]))
    for col in range(len(two_d_list[row])):
        print(two_d_list[row][col], end=" ")
    print()

# do 2d lists have to have the same length of each row?
wonky_list = [
    [1, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4],
    [4, 5, 6, 1, 1, 1],
    [4, 5, 6, 7, 8, 9],
    [7, 8, 9]
]
# will python explode?
# no it won't, it's fine
print()
for row in range(len(wonky_list)):
    # print(len(two_d_list[row]))
    # little bit of a warning... that's why you put in row instead of [0]
    for col in range(len(wonky_list[0])):
        print(wonky_list[row][col], end=" ")
    print()
# too short, it's going to chop something off
# too long then it's going to have IndexError / something
# exact square board 2d list, then it's ok (only ever in that scenario).

print()
for row in range(len(wonky_list)):
    # print(len(two_d_list[row]))
    # here it's working because we took the length of each list independently
    for col in range(len(wonky_list[row])):
        print(wonky_list[row][col], end=" ")
    print()

# strip and split
s = input('Enter a string: ')
print(s.strip())
# strip will strip out whitespace before and after
# only goes until the first and last non-whitespace character

t = '\t\t\t\t\t\n\n\n\n\n\nhello\t \t\n\r\n'
t_prime = t.strip()
print(t_prime)
# whitespace, i mean tabs, newlines, carriage returns, and of course ... spaces...
# takes a string, gives us back a string without any whitespace on the front or back


# the last thing i want to talk about is "split"
# takes a string gives us a list
a_string = input('tell me a story')
#  with nothing inside the string.split() function, it splits on arbitrary whitespace
split_list =a_string.split()
print(split_list, type(split_list))

if split_list[0] == 'add':
    print("i shall add")

list_of_things = ['Feed pupper', 'walk pupper', 'yell at pupper for breaking plate']

for i in range(len(list_of_things)):
    print("{}: ".format(i + 1), list_of_things[i])

# split is probably the most useful string function that there is...
# user enters a bunch of words
#
# submit script is not written in python it's perl, but who cares
s = "submit cmsc201 HW3 hw3_part1.py"
print(s.split())
if s.split()[1] in ['cmsc201', 'cmsc202', 'cmsc341']:
    print('this is a class')
else:
    print('no class')
# i don't know perl, i've written 2 lines of perl in my life
# i'm not teaching perl... not very popular language anymore

# python, Java, C++, C#, javascript, perl, whatever.. imperative
# functional languages specify relations between objects, ML, lisp, clojure, etc
# C++ - low level language, if you need access to pointers hardware
# Java - platform independent / interpreted language
# python - scientific computing, fast to program in language, trade off is speed
# general random speed assessment
# C++ - 1, Java - 1/3, Python - 1/10
# python is better for web development, friendlier intro language sometimes
# C++ angry with pointers
# java protects you from pointers as much as possible - references no access to the pointer value itself
# C++ is a compiled langauge