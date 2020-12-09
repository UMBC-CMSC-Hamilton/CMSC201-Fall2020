def my_function(x: int) -> int:
    """
    type hints - truly hints, in the sense that python doesn't enforce them, your IDE
    may yell at you

    this means that we expect x to be an integer and it will return an integer
    """
    # could cause issues with inheritance.
    if type(x) == int:
        print('yep its an int')

    # more inheritance safe
    if isinstance(x, int):
        return x + 2
    else:
        return 0


print(my_function(5))

print(my_function("5"))


class Animal:
    pass


class Dog(Animal):
    pass


d = Dog()
if isinstance(d, Animal):
    print('dogs are animals')

if type(d) == Animal:
    print('dogs are animals 2')

my_list = []
# why don't we get an index error?
# because it checks the first statement in the and, which is False
# False and ANY == False
# if my_list[0] == 'happy' and my_list: will fail
if my_list and my_list[0] == 'happy':
    print('my list is good')
else:
    print('my list is bad')

# False or X is not yet done
# False or True is True False or False is False
#
#
# if my_list[0] == 'happy' or my_list:
#     print('my list is good')
# else:
#     print('my list is bad')
# if statements read from left to right, down paren levels


# for i-each loop, both the index AND the element
for i, x in enumerate(['a', 'b', 'c', 'd', 'e']):
    print(i, x)
# now that you're out of 201 almost, you're free and encouraged to use this thing.
# i fight with myself about enumerate, one of the best python features.


i = 0
while i < len(my_list):
    # do something here
    i += 1
    #

for i in range(len(my_list)):
    pass


def game_not_finished(board):
    pass


def play_game(board):
    pass


game_board = []
while game_not_finished(game_board):
    play_game(game_board)


x = 2
y = 3; z = 3

""" boolean flags are decent ways to track things
    better to keep the condition in the while loop statement if possible.  
"""

finished = False
while not finished:
    # do stuff
    if x == 2 and y == 3:
        finished = True
    # other stuff to do

# better
while not (x == 2 and y == 3):
    # do stuff
    pass

