alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'caesar' that takes the 'text' and 'shift' and 'direction' as inputs.
def caesar(text, shift, direction):
    caesar_text = ""
    for char in text:
        index = alphabet.index(char)
        if direction == 'encode':
            shifted_index = index + shift
            if shifted_index > 25:
                shifted_index = shifted_index - 26
        else:
            shifted_index = index - shift

        caesar_text += alphabet[shifted_index]

    if direction == 'encode':
        print(f"The encoded text is {caesar_text}")
    else:
        print(f"The decoded text is {caesar_text}")


caesar(text, shift, direction)

