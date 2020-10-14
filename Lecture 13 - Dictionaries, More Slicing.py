def dictionaries():
    # let's get started...
    # what is a dictionary?
    """# A dictionary in python is a (mutable) object that is like a list, but instead of using in-order
        ints,

        In java, dictionaries HashMap?
        In ruby they're called Hash
        In general these are called "Hash Tables" - In 341 you'll learn more about how they work.

        It takes keys as indices and assigns them to values.
    """

    star_wars = {'A New Hope': 4, 'Empire': 5, 'Return': 6, 'Menace': 1, 'Clones': 2, 'Revenge': 3}
    # dictionaries are not guaranteed to have any particular order to the keys...
    for movie in star_wars:
        print(star_wars[movie], movie)
    # remember that if you do a for loop through a dictionary, you're going to get the KEYS!!!!
    # NOT THE VALUES
    # a dictionary is more about the fact that a key -> value rather than just having a value in a dictionary

    print(star_wars['Menace'], star_wars['Clones'])

    # Last Jedi isn't a star wars movie
    # print(star_wars['Last Jedi']) # ???
    # throw a key error if you put in a bad key....
    # remember how to prevent this:
    if 'Last Jedi' in star_wars:
        print('Last Jedi is a Star Wars movie')
    else:
        print('Last Jedi is NOT a Star Wars movie')

    # keys can be bools, ints, floats, strings (anything immutable) NO LISTS, DICTS (they are mutable)
    weird_dictionary = {True: 17, 'the number three': 5, 3: 4, 'help': 'what is this?'}
    # is this "ok?" - will this explode? SyntaxError, KeyError, HorribleError?
    for key in weird_dictionary:
        # key , value
        print(key, type(key), weird_dictionary[key])
    """
        What's bad about this?
        
        all keys should be the same type (not a rule, just good practice)
        if you use weird dictionaries with different types of keys, loops likely to break
        You don't really know what kind of thing is popping out of the loop variable:
            for key in weird_dictionary:
                you don't really know what the heck key is. 
    """
    # all names extremely invented
    students = {'Sam': 'great student', 'Jill': 'sits up front', 'Ryan': 'talks too much in class',
                'Samantha': 'understands recursion', 'Billy': 'likes binary'}

    # you know that the keys are strs, and the values are strings
    for person in students:
        print('{} is a student and our comment about them is: {}'.format(person, students[person]))

    students_grades = {'Sam': [4, 5, 6, 7, 8],
                       'Jill': [1, 5, 7, 9, 11],
                       'Ryan': [1, 5, 12, 9, 11],
                       'Samantha': [1, 14, 7, 9, 11],
                       'Billy': [1, 5, 7, 9, 87]}
    # keys have to be immutable, never said that about the values... values can be anything
    # they can even be dictionaries

    for student in students_grades:
        grade = int(input('What did the student get on Assignment 6? '))
        # accessing the list calls append on that list inside the dictionary...
        students_grades[student].append(grade)
        print(student, students_grades[student])

    # adding values to a dictionary involves just accessing the element in an assignment like this:
    students_grades['Ursa'] = [1, 7, 4, 8, 1, 2]
    print(students_grades)

    del students_grades['Ursa']
    print(students_grades)

    students_grades['Ezra'] = [1, 7, 4, 15, 1, 2]
    print(students_grades)

    # list -> dict (ehh... not really) (just values, you don't really have keys)
    #       you can if you just want 0 -> array[0], 1-> array[1], etc
    # dict -> list ?
    student_list = []
    for student in students_grades:
        student_list.append([student, students_grades[student]])

    print(student_list)

    # the right answer is always try it out for yourself, play around until you break things
    # you can convert this specific weird 2d list thing into a dictionary where element[0] : element[1]
    print(dict([('a', 1), ('b', 2), ('c', 3)]))
    # i think this might be the first time i've ever done that
    # is there an immutable version of a list? yes, it's a tuple, tuples are denoted with (a, b, c) rather than
    # [1, 2, 3]

    """
        Three more things I'm going to teach 
        
        dict.get(key , default_value=None)
        # my_dict[key]
        if key not in my_dict:
            default_value
        else:
            my_dict[key]
    """

    print(students_grades.get('Samantha', []))
    print(students_grades.get('Archibald'))
    print(students_grades.get('Archibald', 'Archibald is not in the dict'))

    students_grades['Archibald'] = [3]

    if students_grades.get('Archibald'):
        # if Archibald in dict, then yep, when the value is non-zero, non-null
        print('Yep')
    else:
        # Nope if Archi not in students_grades
        # if Archi's grades are []
        print('Nope')

    # None evaluates to False
    blah_var = 5

    if blah_var != None:
        # blah_var is not None
        # don't do this because "is" is forbidden in 201
        # is != ==
        print('it\'s good')

    a_list = [1, 2, 3, 4, 5]
    b_list = [1, 2, 3, 4, 5]
    if a_list == b_list:
        print('They are equal')

    # what the heck!??!?!
    if a_list is b_list:
        print('They is equal')
    # this is why we don't teach is

    # b_list is now a reference for the a_list object!
    b_list = a_list
    if a_list is b_list:
        print('They is now equal')
    # generally forbid it because I promise you that you almost never mean this.
    # == not is

    """
    The last two things about dictionaries
    """

    # python decided that it's not good enough to just be a list, it has to be some kind of weird list...
    print(students_grades.keys())
    # probably the single really useful thing you can do with students_grades.keys()
    print(list(students_grades.keys()))
    """
     avoid using this function, not forbidden, but because you don't care what the grades are, unless they're
     attached to a person. 
    """
    print(students_grades.values())
    print(list(students_grades.values()))
    # this tells you just about nothing, values are garbage unless you know what key they came from!
    print(list(star_wars.values()))
    # this isn't helpful usually...

    # the same as just saying key in students_grades
    for key in students_grades.keys():
        # this came from the internet, from a programmer who doesn't really know python well enough
        # might be a decent/good programmer
        print(key)

"""
 About 15 minutes on slices :) 

You can slice strings, lists
"""
a_slice = "hello_world"[3:8]  # r is at position 8, but remember that slice is [includes, excludes)
# a bit like range
print(a_slice)

# step argument is "generally forbidden in 201"
# I don't really care so much
# allowed for range, not for slices (inconsistent, that bothers me too, I'll think about it).
s = input("enter a date-format; YYYY/MM/DD")

YEAR_START = 0
YEAR_END = 4
year = int(s[YEAR_START: YEAR_END])
# regular variables as well.
month = int(s[5:7])  # i tried to convert "/1" into an int
day = int(s[8:10])

print(year, month, day)

# users will disobey everything you ask them to do
s = input("enter a date-format; YYYY/MM/DD")
split_date = s.split('/')
year = int(split_date[0])
month = int(split_date[1])
day = int(split_date[2])
print(year, month, day)


# don't use the slice keyword

# slices are kinda forgiving about IndexErrors... eh...
print('hello there'[0: 1000])
# disobeys the general python philosophy which is "always throw errors"

def funct():
    import random
    return random.choice(['a', 'b', 'c']) + str(random.randint(10, 99))


# negative slices exist, and they count backwards
print('hello there'[-1: -5])
# i'm not gonna
# we're done
# maybe if i'm nice, i'll make a video on negative slices (separate thing).
print('hello there'[-5:])
print('hello there'[-5:0])
# counting from the back end of the string.
blah = funct()
print(int(blah[-2:]))
# you're allowed to use negative slices
# negative slices will never be the trick answer
# no problem will exist where everything you know makes it mega hard, but negative slices makes it 2 lines

