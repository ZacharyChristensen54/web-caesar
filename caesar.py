from helpers import alphabet_position, rotate_character
from sys import argv, exit

def encrypt(text, rot):
    encrypted_msg = ""
    for char in text:
        if char.isalpha():
            encrypted_msg += rotate_character(char, rot)
        else:
            encrypted_msg += char
    return encrypted_msg

def user_input_is_valid(cl_args):
    try:
        cl_args[1]
    except IndexError:
        print('Need rot argument')
        return False
    test_var = cl_args[1]
    try:
        test_var = int(test_var)
    except ValueError:
        print('Enter only integers')
        return False
    return True

def main():
    message = input("Type a message:\n")
    if user_input_is_valid(argv):
         print(encrypt(message, argv))
    exit()

if __name__ == '__main__':
    main()
