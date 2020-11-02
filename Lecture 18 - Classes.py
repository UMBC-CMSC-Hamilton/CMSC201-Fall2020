"""
    pass is a no-op its a piece of code, keyword really that does nothing.
    why do we have pass in Python?

    sometimes because python relies on tab level, code needs something to tell it that
    the tab level is valid
"""
x = 2
if x == 2:
    pass

"""
    What are classes?

    a class is a "structure" in python which can both have variables and methods (functions)
        Java = methods,
        C++ = functions, sometimes methods if they're inside of a class

    What does it mean to "have" variables inside of a class?
    What does it mean to "have" methods?
"""


# in order to declare a class, you type class <class_name>: one more indent
class Voter:
    """
        The first parameter in any method in python (in a class is "self")

        self is a reference to the class that you're in.
    """

    # class constructor for a voter.
    def __init__(self, name, location, voter_id_num, registered=False):
        """ declare all of the variables you're going to use in the constructor
            self.name is not name
            name is a local variable that exists inside this class constructor method
            self.name is a "instance variable" each class gets its own self.name
            self.name is not shared among different voter classes
        """
        print('Calling the voter constructor')
        self.name = name
        self.location = location
        self.voter_id_num = voter_id_num
        self.registered = registered
        self.ballots = []

    def get_polling_location(self):
        return self.location

    def get_voter_info(self):
        return "Name: {}, Address {}, ID: {}, Registered: {}" \
            .format(self.name, self.location, self.voter_id_num, self.registered)

    def cast_ballot(self, candidate):
        b = Ballot(candidate)
        b.count()
        self.ballots.append(b)

    def register(self):
        self.registered = True


class Ballot:
    def __init__(self, candidate):
        self.candidate = candidate
        self.counted = False

    def count(self):
        print('i am a ballot being counted')
        self.counted = True


def voter_test():
    # this is how to create a class
    eric = Voter('Eric', '123 Voter Ave.', 1729)
    # we call Voter( data in it )
    # what python does is calls __init__ <<-- two underscores before and after.
    michal = Voter('Michal', '777 Sevens Lane', 3309, True)
    print(eric.get_voter_info())
    print(michal.get_voter_info())

    # michal.Voter()

    b = Ballot('Howie Hawkins')
    # there is a secret init method that basically goes like this:
    """
        def __init__(self):
            pass
    """
    b.count()
    a_string = "hello"


"""
class str:
    def endswith(self, other_string):
        pass
    def strip(self):
        pass
    def split(self):
        pass
    def lower(self):
        pass

    # ...
    Class names should be Upper-Camel-Case
    
    RoyalGameofUr
    UrPiece
    BoardSquare
"""

# __name__ is just a variable
# __init__
# overloaded operators

"""
    The idea 
"""


class Movie:
    """
        You can declare a variable here
    """

    def __init__(self, title, director, runtime, rating):
        self.title = title
        self.director = director
        self.runtime = runtime
        self.rating = rating

    def get_director(self):
        """
            This is a getter
            :return:
        """
        return self.director

    def set_director(self, new_director):
        """
            This is a setter
            :param new_director:
        """
        self.director = new_director

    def __repr__(self):
        """
        string representation of a class
        :return: a string, representing the class
        """
        return "{}, by {}, runs {}, and has the rating {}". \
            format(self.title, self.director, self.runtime, self.rating)


def run_movies():
    movie_info = input('enter movie info')
    split_movie = movie_info.split()

    list_of_movies = []
    while len(split_movie) == 4:
        name = split_movie[0]
        director = split_movie[1]
        runtime = int(split_movie[2])
        rating = split_movie[3]
        list_of_movies.append(Movie(name, director, runtime, rating))
        movie_info = input('enter movie info')
        split_movie = movie_info.split()

    for movie in list_of_movies:
        print(movie)


class RandomClass:
    # if it's immutable, this kinda works, but it's not great to do this
    y = []
    # this is something you can do:
    SOME_CONSTANT = "this is a constant forever and won't change"
    """
        immutable class variables, what these things are called, can change per class.
        mutable lists, dictionaries, other classes, stuff like that, are the same shared
        variable, and if you change one, you change all of them in all of the RandomClasses
    """

    def __init__(self, x):
        self.x = x
        # this is totally ok
        # this is called an instance variable, instead of a class variable <---
        # class variables are shared among all of the RandomClasses
        # instance variables are created new for each class.
        # we generally think about things as instance variables, not class variables.
        #   in C++ you can declare a class variable as static, basically the same idea
        self.my_list = []
        print(self.SOME_CONSTANT)


def random_class_stuff():
    a = RandomClass(5)
    a.y.append(5)
    b = RandomClass(17)

    print(a.x, b.x, a.y, b.y)
    # what happened?

    """
        classes are like blueprints, 
        device that remembers a few things and can do a few things
        
        What you need to know:
            How to declare a class
            How to use self to get variables and other functions inside a class
            How to write a constructor __init__(self, args)
            How to create variables in a constructor
            How to access and use a class, my_class.do_something(params)
            How to write a method for a class. (setters / getters/other functions)
                Not many setters and getter in python, not nearly as much as other languages
        Do I need to know : repr? no
                            destructors? no
                            inheritance? no
                            overloading operators? no
                            @staticmethod and @classmethod? no
                            There is not really public/protected/private in Python**
                            
        In the "real programming world":
            99.99% stuff is the stuff I teach
            00.01% of the stuff is the stuff I don't teach
            Basically everything else is covered in 202.                      
    """


"""
    Break away and talk about recursion for 20 minutes
"""


def count_as_rec(a_string):
    """
    look at the first character, is it an a? or A? if it is we want to add 1 to the count
        if not go past
    """
    if not a_string:
        # None, ""
        return 0
        # base case
    elif a_string[0].lower() == 'a':
        return 1 + count_as_rec(a_string[1:])
    else:
        return count_as_rec(a_string[1:])


# no good 'abb'
# good 'aaaaaaab' 'aaaaaaaa' 'abababab' "" - good

def at_least_as_many_as_as_bs(a_string, diff=0):
    if not a_string:
        return True
    if a_string[0].lower() == 'a':
        return at_least_as_many_as_as_bs(a_string[1:], diff + 1)
    elif a_string[0].lower() == 'b':
        if diff - 1 < 0:
            print(a_string)
            return False
        else:
            return at_least_as_many_as_as_bs(a_string[1:], diff - 1)


if __name__ == "__main__":
    print(at_least_as_many_as_as_bs(input('tell me a string: ')))
