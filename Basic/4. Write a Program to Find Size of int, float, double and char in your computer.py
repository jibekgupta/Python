import struct

def find_size(data_type):
    return struct.calcsize(data_type)

# Size of int
int_size = find_size('i')
print(f'Size of int: {int_size} bytes')

# Size of float
float_size = find_size('f')
print(f'Size of float: {float_size} bytes')

# Size of double
double_size = find_size('d')
print(f'Size of double: {double_size} bytes')

# Size of char
char_size = find_size('c')
print(f'Size of char: {char_size} bytes')