

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_len = len(alphabet)

def print_row(a:int):
#'''A loop that returns a string containing the alphabet starting at a designated letter by the form of an index'''
    for c in range(alphabet_len):
        print (f' {alphabet[(c + a) % alphabet_len]} |', end='')
    print()


def vigenere_sq():
#''' a loop that created a table of the alphabet with each row starting with the next letter in the alphabet'''
#
    for a in range(alphabet_len):
        print(f'{alphabet[a]}||', end= '')
        print_row(a)

print(vigenere_sq())

def header():
    print(f' ||', end ='')
    for a in alphabet:
        print(f' {a} |', end = '')
    print()
    suffix = "---|" * (alphabet_len)
    print(f'  |{suffix}', end ='')


def letter_to_index(letter, alphabet):
    for i, c in enumerate(alphabet):
        if letter == c:
            return i
    return  None

def index_to_letter(index:int ,alphabet:str ):
    if 0 <= index <= alphabet_len:
        return alphabet[index]
    return None

def vigenere_index(key_letter, plaintext_letter, alphabet):
    ci = (letter_to_index(key_letter,alphabet) + letter_to_index(plaintext_letter,alphabet)) % alphabet_len
    return index_to_letter(ci,alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    for i, pt in enumerate(plaintext):
        cipher_text += vigenere_index(key[i% len(key)],pt,alphabet)
    return cipher_text



key = "MONKEY"
plaintext = 'LIGHTHOUSES ARE COOL'
#print(encrypt_vigenere(key, plaintext, alphabet))