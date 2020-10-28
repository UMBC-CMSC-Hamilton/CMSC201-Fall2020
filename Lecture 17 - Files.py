def split_into_words(a_list_of_strings):
    list_of_words = []

    for a_string in a_list_of_strings:
        for word in a_string.split():
            list_of_words.append(word)

    return list_of_words


def enter_sentences():
    sentence_list = []
    in_string = input('Enter a sentence: ')
    while in_string.lower() != 'quit':
        sentence_list.append(in_string)
        in_string = input('Enter a sentence: ')
    return sentence_list


# whatever comes out of enter_sentences function is a list of strings
# you can feed a returned value into a new function:
# print(split_into_words(enter_sentences()))


def my_function(x):
    # no y defined in this function
    # python is going to search for the global scope variable y
    return x + y
    # y is being used as a global variable... don't do this


def take_turn(player_1):
    # global keyword is forbidden in this course
    # global player_1
    # player_1 is not being defined here.
    # python is going to use this global variable
    print(player_1, 'it is your turn')
    # this is a local variable that has the same name as player_1 (the global version)
    player_1 = 'Sam'
    # so this doesn't affect anything, i.e. the global version
    print(player_1)

"""
    So many bugs can be created by having all functions modifying the same global variables.
        One function messes with the variable <-- bug was here
        the next one expects the variable to be in the prior configuration, then explodes <-- think bug is here
    
    CONSTANTS are technically global, escape the problem that this bug is talking about
        constants should be really constant, you shouldn't mess with them
        this type of bug "shouldn't" happen
    
    We will be lenient about global variables this time for project 1, not for project 2.
        If you are using global variables, and they're causing you this kind of problem, then fix that.
        
    If you declare a variable in main, send into functions as a parameter, that's ok.  main()
        Anything you declare in main IS global, pretend it's not, send it into functions as parameters.
        When i look at your function, i look at your parameters.  
        If you are using something outside of the function isn't defined in a parameter, we have to go hunting
            long time, confusing, .. bad stuff can happen.  
    
    On homeworks, almost everything was global so we dont' care.          
    
    Shadows name from outer scope == (there is a global variable with the same name as the local one)
        There's nothing "wrong" with this, as long as you know what's happening
        
    Unit testing, test components (functions first, modules, on the way up)
        Test each component of your program separately (theoretically)
"""

def odyssey_example():
    # remember that file names are strings
    # load_board(proj1_board1.csv) error
    # load_board('proj1_board1.csv') - file names are strings
    odyssey_file = open('odyssey.txt')
    # calling
    # odyssey_file.readline()
    for line in odyssey_file:
        # print(line, end='')
        print(line.strip())
        # automatically prints a newline character at the end of the string
        # each line already has a newline character

    odyssey_file.close()

    # option 1: read by line
    # option 2: read the entire file
    odyssey_file = open('odyssey.txt')
    # reads the entire file at once all the way to EOF (end of file)
    print(odyssey_file.read())

    odyssey_file.close()
    """
        What happens if you don't close a file?

        Generally in read mode, nothing.  Sometimes the file handle isn't closed.
        Biggest problem is when you are writing to a file.  Locks a file based on the write permission.
            Prevents multiple programs from opening a file with write permission.  
            Sometimes the OS forgets to unlock the file.  
    """
    odyssey_file = open('odyssey.txt')
    while input('Do you want to keep going?').lower().strip() in ['y', 'yes']:
        print(odyssey_file.readline())

    odyssey_file.close()

    odyssey_file = open('odyssey.txt')
    # what is the difference between readline() and readlines()
    print(odyssey_file.readlines())

    odyssey_file.close()

    # read() - a gigantic string
    # readline() - a single line generally with an \n (maybe not if its the last line)
    # readlines() - a list of readline

    odyssey_file = open('odyssey.txt')
    # be careful with this... not illegal just a little scary
    if 'And this difficulty attaches itself more closely to an age in which\n' in odyssey_file:
        print('yes')
    else:
        print('huh?')
    odyssey_file.close()

    odyssey_file = open('odyssey.txt')
    ody_file_contents = odyssey_file.read()
    if 'difficulty' in ody_file_contents:
        print('this will definitely work')

    print('about to read another line: ', odyssey_file.readline())
    # it comes out blank because we already read the entire file, no more data.
    odyssey_file.close()


if __name__ == '__main__':
    y = 5
    player_1 = 'Michael'
    player_2 = 'Rebecca'
    # print(my_function(3))
    take_turn(player_1)
    # the player is modified outside of the function too, which is not great
    print(player_1)

    # let's talk about writing files
    # open('newfile.txt', 'r') open('newfile.txt'), by default it is read permission
    new_file = open('newfile2.txt', 'a')

    # will 'w' option append or overwrite the entire file???
    # 'w' will blank out the entire file first, potentially very bad
    # whatever is in that file is about to die.
    # w = not just write, create and or overwrite
    s = input('Enter thingy: ')
    while s != 'quit':
        new_file.write(s + "\n")
        # write sticks the data into a buffer
        # whenever the OS feels like it, it will dump it to the file.
        s = input('Enter thingy: ')

    new_file.close()
    print('ok go again')
    new_file_again = open('newfile.txt', 'a')
    s = input('Enter thingy: ')
    while s != 'quit':
        new_file_again.write(s + "\n")
        # write sticks the data into a buffer
        # whenever the OS feels like it, it will dump it to the file.
        s = input('Enter thingy: ')
    new_file_again.close()

    """
        to recap 
        'r' - read mode
        'w' - write mode (OVERWRITE MODE/CREATE MODE)
        'a' - append mode (goes to the end and writes there) 
                append also creates the file, but doesn't overwrite
    """

    # next time we'll talk about with, more file examples, then we will do .... stuff == more recursion or classes

    # for project 1:
    # building buildings and building rent is going to be EC
    # get the of the project working before you do building stuff.
    # +15 points or so 115/100
