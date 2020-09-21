# review
some_letters = ['a', 'b', 'c', 'd', 'e', 'f']

# creates a letter variable, and then repeatedly takes elements out of the list
# assigns them into the variable letter, which then can be used in the loop code
# for each loop - each letter is actually the loop variable
for letter in some_letters:
    print('The letter is {}'.format(letter))

# split, strip - strings
# range, for each vs for i loops.

n = int(input('What number do you want to add up to? '))
total = 0
# wrong, why does it go from 0... 10 - 1 instead of 1 ... 10 for instance?
# 0... n + 1, 0 is ok because 0 + a = a.
# FOR I loops - loop variable is an index, integer, some kind of count
for i in range(n + 1):
    print(i)
    total += i
print(total)

# well, when you have a list, what are the indices like?
# right, they start at zero, and they go up to the len(the_list) - 1
# range is built to function with lists.

# do I care about the index more, or do I care about the element more?
# index - For i
# element = for each.

L = [7, 8, 3, 12, 1]
# for each loop, i = elements in the list L, not indices
# i is a copy of the elements in L, doesn't change the list.
for i in L:
    # i = i + 1
    i += 1
print(L)

# well ok, how do I change a list element in a for loop!?
# range gives us 0 ... a number
# len(L) = that number, the length of a list.
# accessing the element at L[index] so this will change the list
for index in range(len(L)):
    # actually changes the value
    L[index] += 1

print(L)

print(len(L))

num = int(input('How many elements? '))
the_list = []
for i in range(num):
    # this line is kinda dummy line
    the_list.append(0)

print(the_list)

stop = 17
print(list(range(stop)))
start = 3
print(list(range(start, stop)))
# what else can you do with range?
for i in range(2, 10 + 1):
    print(i)

for i in range(3, 80, 5):
    # end = ' ' instead of a newline, it's just going to do a space at the end of the print statement
    print(i, end=' ')

print()

# range(start=0, stop, step=1)
for i in range(5, 80, 5):
    # end = ' ' instead of a newline, it's just going to do a space at the end of the print statement
    print(i, end=' ')

# range must be integers ...

for i in range(11):
    f = i / 10
    print(f)

"""
    Aside from lists, for loops, etc
        if __name__ == '__main__'
        
        You probably won't understand 100% of what I am saying here, but then it doesn't matter
    
        Entry point... 
        Java
        class Myclass
        {
            public static void main(String [] argzzzz)
            {
            
            }
        }
        C++
        int main() {
            return 0;
        }
"""

# we never declared __name__, dont' mess with __name__
print(__name__)
# who cares?
# we don't really...
import L6_second_file

if __name__ == '__main__':
    # ensures that this code is run whenever this is the main file you're running
    print('I am the main file')
    # what's the point of all this?
    # sometimes you want to put some kind of testing script, other kind of code that only runs whenever you run
    # that specific file.
    # hide that code in the if n == m block, won't run that code unless someone runs that file.

    # right under your header comment, basically, all code should be indented and inside the if n == m block

# good practice, there's not a firm 100% useful reason to start doing if n == m right now...
print(L6_second_file.blah_var)
# basically all for the future, nothing useful right now

fridge = ['eggs', 'cheese', 'lunch meat', 'green peppers', 'milk', 'avocados']
for thing in fridge:
    if thing == 'milk':
        print('we have milk')

# in does test to see if a in B (that will work)
if 'milk' in fridge:
    print('we really have milk')

print('milk' in fridge)

# you always have to remember that in runs a secret for loop
# we're teaching python here... but... .not really
# we're teaching problem solving,... yess....
# why we have all this banned stuff

if 'lemon' not in fridge:
    print('something something something')

remove_list = [1, 4, 5, 5, 7, 5, 3]

# what's the point of this?
# be careful mixing remove with list iteration
for x in remove_list:  # [1, 4, 5, 6, 7, 5, 3]
    if x == 5:
        remove_list.remove(x)
    print(x, end=" :: ")  # 1 :: 4 :: 5 :: 7 :: 5

print(remove_list)
# [1, 4, 6, 7, 3]

# no while loops yet, everything in hw3 is for loops
remove_list = [1, 4, 5, 5, 7, 5, 3]
print(remove_list)
while 5 in remove_list:
    remove_list.remove(5)
print(remove_list)
# hw4 is while

# last topic for today nesting of loops

for i in range(5):
    for j in range(5):
        # unbanned all things you can stick into print
        print('({}, {})'.format(i, j), end=' ')
    # empty line
    print()

s = 'my string {}'.format(17)
print(s)

first_names = ['Adam', 'Barry', 'Charlie', 'Dahlia']
last_names = ['Aaronson', 'Benson', 'Coventry', 'Delta']

# for each loop, but it can also be nested.
for first in first_names:
    for last in last_names:
        print(first, last)

# no nested loops on hw3 are required...
# might be some nested loops on hw4...

# append adds to the end of a list, including an empty list.
my_list = []
my_list.append(5)
print(my_list)

# tuples == lists - mutability
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[3] = 5



