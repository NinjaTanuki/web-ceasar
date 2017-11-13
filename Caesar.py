import string

def alphabet_position(letter):
    position = 0
    for char in string.ascii_lowercase:
        if letter == char.lower():
            return position
        if letter == char.upper():
            return position
        else:
            position = position + 1
    
def rotate_character(char, rot):
    for a in string.ascii_lowercase:
        if char == a.lower():
            rot_char = alphabet_position(char)+ rot
            if rot_char < 26:
                return (string.ascii_lowercase[rot_char])
            else:
                 return (string.ascii_lowercase[rot_char % 26])
        if char == a.upper():
            rot_char = alphabet_position(char)+ rot
            if rot_char < 26:
                return (string.ascii_uppercase[rot_char])
            else:
                 return (string.ascii_uppercase[rot_char % 26])
    else:
        return char
    
def encrypt(text, rot):
    encrypted = ""
    for char in text:
        if char == ' ':
            encrypted = encrypted + " "
        else:
            encrypted = encrypted + rotate_character(char, rot)
    return encrypted
def main():
    from sys import argv
    message = input("Type a message!")
    if len(argv) > 1:
        print (encrypt(message,int(argv[1])))
    else:
        rotate = int(input("Rotate by?"))
        print(encrypt(message,rotate))

if __name__ == "__main__":
    main()