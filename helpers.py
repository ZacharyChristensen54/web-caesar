def alphabet_position(letter):
    pos = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = letter.upper()
    if len(letter) == 1:
        for char in alphabet:
            if char == letter:
                return pos
            pos += 1

def rotate_character(char, rot):
    char_pos = alphabet_position(char)
    new_pos = char_pos + rot
    new_pos %= 26
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_letter = alphabet[new_pos]
    if char == char.upper():
        return new_letter
    else:
        return new_letter.lower()
