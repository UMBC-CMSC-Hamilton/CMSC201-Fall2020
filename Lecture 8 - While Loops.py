my_movies = []
# priming the input - take a first input
s = input('Enter a movie name: ')

# the while loop doesn't always check for s == quit, it only checks when the loop comes around again
# check to see if the input is bad, or you want to continue
while s != 'quit':
    my_movies.append(s)
    s = input('Enter a movie name: ')
    # you don't know how many movies

print(my_movies)

# first prime the input
an_int = int(input('Tell me a positive integer: '))
# check for bad input, if it's bad keep going in the loop, otherwise you can exit
while an_int <= 0:
    # you should ask for more input.
    an_int = int(input('That wasn\'t positive, tell me a positive integer: '))
    # if you don't set an_int, this results in an infinte loop...
    # you don't know how many times a person will enter a negative number ==> while

# do # not a keyword
# sorry...

a_list = [1, 2, 56, 8, 3, 9, 12, -7]

# yes, it's going to execute len(a_list) times, fixed, so... for loop
for x in a_list:
    print(x, 'is a value')

# oh wait, i know this is going to execute len(a_list) times, so... no this is bad
# let me show you an equivalent while loop
index = 0
while index < len(a_list):
    print(a_list[index], 'is a value (while)')
    # if you don't do this... .... problem
    index += 1
    # that was an infinite loop

# moral of the story: we teach for before while for a reason...
# reason 1) for loops iterate more safely... no infinite loops
# reason 2) for loops are basically 95% of the loops that you write...

# why do you ever use a while loop:
# THE REASON: I don't know how many times its going to take to go through...


for x in range(an_int):
    print('this is fine too', x)

my_string = input('Do you want to quit or exit? ')
# while my_string != 'quit' and my_string != 'exit':
# take my_string and look in this list and compare strings
while my_string not in ['quit', 'exit']:
    print('You entered', my_string)
    my_string = input('Do you want to quit or exit? ')

# do you know why we ban break (also continue)?
#   we give problems whose solutions don't need them.
#   as soon as we give people break, they immediately stick it in, instead of using the while condition
# instead of figuring out a good while condition, they just have a bunch of breaks...
# our goal: make you figure out while loops without break, so you know when you need it..

# discrete log, base 3....
# I want to know the power p, so that for an integer x, 3^p <= x < 3^(p + 1)
x = int(input('Enter the thing that you want the log of: '))
# the point of this loop is not to teach logs, the point is to teach while loops.
current_power = 0  # that is 3^0
while 3 ** current_power < x:
    current_power += 1

# print literally everything in the universe
print(current_power, x, 3 ** current_power, 3 ** (current_power - 1))

# beginning of the program, don't change it
ERROR_BOUND = 0.00005
x = float(input('Enter the value for which we shall find the square root: '))
current = 1
previous = 0
# why is this a while loop?
# because we didn't know how long it would take to get into the error bound...
ERROR_BOUND = 0.2
while abs(current - previous) > ERROR_BOUND:
    previous = current
    current = 0.5 * (current + x / current)
    print(current, previous)
print('guess=', current)
print('actual value', x ** 0.5)

START_GAME = 'New Game'
GET_HIGH_SCORES = 7

options = [START_GAME, 'Load Game', 'Save Game', 'quit']

menu_option = 5
while s != 'quit':
    s = input('What do you want to do? ')
    if s == START_GAME:
        print('new Game started')

    if menu_option == GET_HIGH_SCORES:
        pass
        # do something

# how constants are used in the class
# declare your constants at the top under imports, but over the if __name__ == '__main__' block...
#   never change them
"""
   avoid magic values:
        numbers that are like kinda random
        not all numbers are magic, 0, 1 generally not.. if you're testing divisibility
            var % 2 == 0 not magic
        menu options, choices from lists, strings to type 
        DAYS_OF_WEEK = 7
        x % DAYS_OF_WEEK (oh the variable is some kind of day)
        p, x, t not going to know what the heck that was
"""
