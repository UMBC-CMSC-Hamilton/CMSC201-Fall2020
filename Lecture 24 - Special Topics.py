"""
    CTRL+ALT+S bring up settings
    Go to project interpreter.
    Install the module/package that you want.
    # these are built in to python and exist by default.
    import random
    import json, csv
"""

import requests
from requests.exceptions import ConnectionError


def do_web_stuff():
    page_data = requests.get('http://www.wikipedia.org')

    # gets the raw html page data
    print(page_data.text)
    # printed out object
    print(page_data, type(page_data))

    # what does try do?
    # try is basically a bit of scare code, it says "do this code, but maybe it will explode"
    try:
        not_found_page = requests.get('http://www.thiswebsitedoesntexistasdf.com/')
        print(not_found_page)
    # except is the path out.  In case of failure, do this instead:
    except ConnectionError as error:
        print(error)


try:
    x = int(input('Tell me an integer.'))
except ValueError:
    print('That wasnt an integer')
    # x won't be created here.
    x = 0

try:
    my_list = [1, 2, 3]
    x = int(input('Enter an integer to remove from my_list: '))
    my_list.remove(x)  # this throws an exception whenever the item doesn't exist in the list
# except without a class type, so it will catch ALL exceptions that are thrown.
# you don't know what went wrong
except:
    print('something bad happened')

"""
    when an exception is thrown it stops executing all code in the try.
    jumps to the except and never goes back to try again.
"""


def my_recursive_countdown(c):
    if c == 0:
        return 0
    return 1 + my_recursive_countdown(c - 1)


try:
    x = int(input('How many times do you want to go? '))
    print(my_recursive_countdown(x))
except ValueError as error:
    print(type(error), error)
    print('You need to be careful when inputting numbers, muh-dude')
except RecursionError as rec_error:
    print(str(rec_error) + 'some other thing')
    print('python by default only allows about 1000 recursive calls')

"""
    Exception is the parent class
    super() gets that class and says Hey parent class, execute your own constructor
    all this stuff is like week 6-8 of 202. 
"""


class NewErrorType(Exception):
    def __init__(self, message):
        super().__init__(message)


def my_function():
    x = int(input('Enter numerator: '))
    y = int(input('Enter denominator: '))
    if y == 0:
        raise NewErrorType('You shouldn\'t divide by zero.')
    z = x / y
    return z


class Animal:
    def __init__(self):
        self.avg_life = 0

    def average_lifespan(self):
        return self.avg_life


class Dog(Animal):
    def __init__(self):
        self.avg_life = 10


class Cat(Animal):
    def __init__(self):
        self.avg_life = 20


class Lemur(Animal):
    def __init__(self):
        self.avg_life = 5

def animal_things():
    L = Lemur()
    cat = Cat()
    dog = Dog()
    print(L.average_lifespan())
    print(cat.average_lifespan())
    print(dog.average_lifespan())


def catching_exceptions():
    for _ in range(5):
        try:
            print(my_function())
        # in C++ except == catch
        # raise == throw
        except NewErrorType as new_error:
            print(new_error)
    try:
        for _ in range(5):
            print(my_function())
    except NewErrorType as new_error:
        print(new_error)


