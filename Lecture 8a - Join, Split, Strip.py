s = ''
while s != 'quit':
    print(s.split())
    s = input(': ')

# let's talk about join for 30 seconds!!
# if you start with a list of words:
list_of_words = ['robot', 'nexus', 'github', 'plenary', 'subaltern']
# join is weird in this language
my_string = "\t::\t".join(list_of_words)
print(my_string)
# separator.join(a list of words)
# split, strip, join are allowed on HW4...
# hw3_part3 needs split (don't need split, but it's awful without it)
# HW3 - all for loops
# end="" in hw4, want to on the circle problem, it says to use it there... probably want it on the checkerboard
# yeah definitely 100%  use print(something, end="")

# del deletes an object from a list

b_list = [1, 2, 3, 4, 5]
# removes by index
del b_list[2]
print(b_list)
s.split()  # nothing in it

name_list = []
s = input()
split_string = s.split()
# you don't have to check len(s) >= 2...
# split_string[0] could also not exist
#
if len(split_string) >= 2 and split_string[0] == 'add':
    print('we got add')
    # this may not exist...
    name_list.append(split_string[1])

