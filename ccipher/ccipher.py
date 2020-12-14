alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Don't change the code above 👆

def encrypt(text, shift):
    ciphertext = ""  # this will hold the shifted/cipher output
    for letter in text:  # loop through each letter in text (strings are iterables)
        position = alphabet.index(letter)  # get the index of the letter in text from its position in alphabet
        new_position = position + shift  # using that index from alphabet, add the shift amount, assign as new position
        new_letter = alphabet[new_position]  # use the letter at the new/shifted index position and grab that letter
        ciphertext += new_letter  # as I loop through the text, collect the shift letters in ciphertext variable
    print(f"The Encoded ciphertext is {ciphertext}")


def decrypt(text, shift):
    plain_text = ""  # this will hold the shifted/cipher output
    for letter in text:  # loop through each letter in text (strings are iterables)
        position = alphabet.index(letter)  # get the index of the letter in text from its position in alphabet
        new_position = position - shift  # using that index from alphabet, add the shift amount, assign as new position
        plain_text += alphabet[new_position]  # use the letter at the new/shifted index position and grab that letter
    print(f"The Decoded ciphertext is {plain_text}")


if direction == 'encode':
    encrypt(text, shift)

if direction == 'decode':
    decrypt(text, shift)
