from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Create a function called 'caesar' that takes the 'text' and 'shift' and 'direction' as inputs.
def caesar(input_text, shift_value, shift_direction):
    caesar_text = ""
    if shift_direction == 'decode':
        shift_value *= -1
    for char in input_text:
        index = alphabet.index(char)
        shifted_index = index + shift_value
        if shifted_index > 25:
            shifted_index = shifted_index - 26
        caesar_text += alphabet[shifted_index]

    if shift_direction == 'encode':
        print(f"The encoded text is {caesar_text}")
    else:
        print(f"The decoded text is {caesar_text}")


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(text, shift, direction)
