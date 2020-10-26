# here's a common practice


def do_something(a_list):
    if not a_list:
        # gets you out of the function before you do anything bad
        # accessing indices that don't exist
        # totally allowed, not discouraged at all
        return 0
        # python kind of likes this

    # nesting level 1

    if a_list:
        # do stuff to a_list
        pass
        # nesting level 2
    else:
        return 0

    # something, more code here
    # return a_list[0] + 2 * a_list[1] + a_list[2]
    # you don't actually have to this this it will just happen
    # return None


# decimal!!!!
def decimal_to_binary(number):
    """
    :param number
    :return: binary string!!
    """
    bin_string = ''
    if number == 0:
        return '0'
    # each digit to go onto the front not the back
    while number != 0:
        if number % 2 == 1:
            bin_string = '1' + bin_string
        else:  # number % 2 == 0
            bin_string = '0' + bin_string
        number //= 2

    return bin_string


def decimal_to_hex(number):
    """
    :param number
    :return: binary string!!
    """
    dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
     6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
     12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hex_string = ''
    if number == 0:
        return '0x0'
    # each digit to go onto the front not the back
    while number != 0:
        hex_string = dec_to_hex[number % 16] + hex_string
        number //= 16

    return '0x' + hex_string


def hex_to_dec(a_hex_string):
    a_hex_string = a_hex_string.lower().split('x')[1]

    dec_to_hex = {'0': 0, '1': 1, '2': 2, '3': 3,
                  '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'a': 10, 'b': 11,
                  'c': 12, 'd': 13, 'e': 14, 'f': 15}

    value = 0
    for i in range(len(a_hex_string)):
        value += dec_to_hex[a_hex_string[len(a_hex_string) - 1 - i]] * 16 ** i

    return value



# bin_string += '1'
# bin_string = bin_string + '1'
# that's not what we want, we want bigger digits to go left, not right
n = int(input('Convert number? '))
while n != -1:
    print(decimal_to_hex(n), hex(n))
    n = int(input('Convert number? '))

# floating point (scientific notation)

# 0.something
# to a power
# 100.0101
# 4.3125
# an integer is just a number, stored as binary
print(0x19, 0x57, 0xfff)
print(25, 87, 4095)


hex_string = input('hex string')
while hex_string != 'quit':
    print(hex_to_dec(hex_string))
    hex_string = input('hex string')
