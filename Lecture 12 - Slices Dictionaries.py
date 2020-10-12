# slices.!!!
# what are slices
def slice_examples():
    #         0  1  2  3  4  5  6  7  8  9
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # a slice is a sublist
    print(a_list[3])
    b_list = a_list[3:7]
    # the notation is [start (inclusive): stop (exclusive)]
    # "like" [3, 7)
    # more like range yes
    print(b_list)

    c_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    print(c_list[0: 5])
    # notation is kind of fixed...  fifth element is a great movie....
    print(c_list[:5])
    # secret is if you omit the endpoint, it'll give you 0 by default...
    print(c_list[5: len(c_list)])
    # be careful with this one, it's not indexing, it's slicing.... ehhh
    print(c_list[5:])

    # good question... this will produce an empty slice for the same reasons as below...
    print(c_list[5: 0])
    # like this:
    for i in range(5, 0):
        # default step == +1, so goes up
        # either this is an infinite loop, or not
        # if not it shouldn't do anything....
        print(i)

    """
    if end - start > 0 and step > 0:
        go
    elif end - start < 0 and step < 0:
        go
    else:
        no go
    """

    # next example... a string slice...
    a_string = 'HelloIAmAString'
    print(a_string[6:])
    print(a_string[2:12])
    # probably takes r, does it take i? good question... (no it doesn't)
    # strings and lists both have the slice feature, which is just beautiful....

    # the next right question is what does this do?
    print('about to test')
    print(a_string[2:50], end="\nthis is the end\n")
    # sometimes slices do nothing and just give empty strings
    # didn't give an index error. it corrected itself.
    # goes to the end, and stops, Good: doesn't error, Bad: maybe now you think the string has length whatever >>

    # tricky question.
    print(a_string[:])
    # first default to zero, second default to len(a_string)
    b_string = a_string[:]
    # this may not be necessary, because of immutability
    # another way to copy strings
    # another way to copy lists
    copy_list = a_list[:]
    # sometimes see this in python code... in my opinion, i'd prefer:
    other_copy_list = list(a_list)  # list constructor
    # deep copies of the list

    # a reference
    ref_list = a_list
    print(a_list)
    ref_list[4] = 21500
    print(a_list)
    print(ref_list)
    # but if you print out for instance..
    print(copy_list, other_copy_list)

    # lab from last week was check how many rotations there are of a particular string...
    the_string = input('Enter String: ')
    for offset in range(1, len(the_string)):
        new_string = ''
        for i in range(len(the_string)):
            new_string += the_string[(offset + i) % len(the_string)]
        if new_string == the_string:
            print('The offset', offset, 'works as an invariant rotation or whatever')

    # rewrite this code to use slices...
    the_string = input('Enter String Again: ')
    for offset in range(1, len(the_string)):
        # think mega hard right now... let's do it...
        # the offset is where we start... then we need to take #offset of letters, and smash it on to the end
        # doing the inner for loop for us...
        new_string = the_string[offset:] + the_string[0: offset]
        if new_string == the_string:
            print('The offset', offset, 'works as an invariant rotation or whatever')

    for i in range(25):
        print(i % 5, end=" : ")


# why don't i teach negative indicies, step argument, all kinds of crazy slice things you can do?
# nothing more than what is here is required to do the HW...

"""
    Now it's time to talk about dictionaries. :)
    
    What is a dictionary? Kind of like a list:
        has indexing operation just like a list
        except you can use anything immutable (bool, str, int, float) "keys"

    Syntax d = {key: value, key: value, key: value, key: value...}
"""

my_first_dictionary = {'hello': 3, 'goodbye': 17, 'revolution': 5, 'dutchman': 3, 1729: 51}
print(my_first_dictionary)
# indices had to be integers!  but here, they are clearly not integers, they are strings
print(my_first_dictionary['hello'])
# that's ok for dictionaries
print(my_first_dictionary['revolution'])
# they can also be integers
print(my_first_dictionary['dutchman'])
# here's an example which looks kind of like a List, but it's just because we're using int-keys
print(my_first_dictionary[1729])

# let's do the example where we access a non-existent thing
# don't do this because it doesn't exist...
# my_first_dictionary[3]

# before you access something in the dictionary, you can always test:
m_dictionary = {'r': 17, 'q': 341, 'ell': 211, 'zed': 5, 'red': 2, 'whatever': 163}
if 'happy' in m_dictionary:
    print('Happy in there')
else:
    print('happy not in there')

# always looking for keys, NOT VALUES
double_dictionary = {'yes': 5, 'yes': 31}
print(double_dictionary)
# overwrote the first key with the second key
# moral of that story is that keys MUST be unique, can't use the same key to open "two different locks"
#       get two different data elements.

monsters = {'big snake': {'attack': 3, 'life': 3, 'first_strike': True},
            'crocodile': {'attack': 5, 'life': 39, 'first_strike': True},
            'alligator': {'attack': 1, 'life': 40, 'first_strike': True},
            'turtle': {'attack': 17, 'life': 81, 'first_strike': True, 'flying': True}
            }
# what if we want to add a new monster?
monsters['werewolf'] = 32768
monsters['bigfood'] = 301
monsters['yeti'] = 302
# shouldn't this throw an error?  no it won't... as long as the undefined thing is on the left side
#       as long as it's being assigned, it won't throw an error.
print(monsters)

# what if the keys are of different type?  generally avoid that ..

for name in monsters:
    # key values
    print(name, monsters[name], end=' \n ')

monsters['big snake']['life'] = 31
print(monsters['big snake']['life'])

# removal from dictionaries...
del monsters['turtle']['flying']
del monsters['werewolf']
del monsters['bigfood']
print(monsters)
# len(dict) = number of keys in the dictionary == number of values in the dictionary
print(len(monsters))

for v in monsters.values():
    print('generally wrong')

# don't do this, because it's not actually a dictionary, it's a set
my_new_dictionary = {'a', 'b', 'c', 'd'}
# a mathematical set
print(type(my_new_dictionary))

my_new_dictionary = {}
for c in 'abcd':
    # garbage for now    = whatever you want the value to be...
    my_new_dictionary[c] = ord(c) ** 2 + ord(c) + 1

print(my_new_dictionary)

# fundamental thing about dictionaries, you can't guarantee order to the keys...

