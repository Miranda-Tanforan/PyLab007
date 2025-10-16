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
    cipher_text = []
    for i, pt in enumerate(plaintext):
        cipher_text.append(vigenere_index(key[i% len(key)], pt, alphabet))
    return ''.join(cipher_text)


def display_menu():
    option = ['Encrypt', 'Decrypt']
    for i,option in enumerate(option):
        print( f'{i + 1}. {option}')

def choice():
    input("Choice: ")
    if choice == 1:
       print("hello")
    return none
#print(display_menu())
#print(choice())
key = "monkey"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
alphabet_len = len(alphabet)
choice = 0
while True:
    choice = int(input("select option[1,2,3]:  "))
    if not (1<= choice <= 3):
        continue
    if choice == 1:
        plaintext = input("what is your message: ")
        encrypt_vigenere(key, plaintext, alphabet)
