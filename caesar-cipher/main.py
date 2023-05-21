alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, encode_shift):
    cipher_text = ""
    for char in plain_text:
        index = alphabet.index(char)
        shifted_index = index + encode_shift
        if shifted_index > 25:
            shifted_index = shifted_index - 26
        cipher_text += alphabet[shifted_index]
    print(f"The encoded text is {cipher_text}")


# Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(encrypted_text, decode_shift):
    decrypted_text = ""
    for char in encrypted_text:
        index = alphabet.index(char)
        shifted_index = index - decode_shift
        decrypted_text += alphabet[shifted_index]
    print(f"The decoded text is {decrypted_text}")


if direction == 'decode':
    decrypt(text, shift)
elif direction == 'encode':
    encrypt(text, shift)
else:
    print("Invalid direction value")

