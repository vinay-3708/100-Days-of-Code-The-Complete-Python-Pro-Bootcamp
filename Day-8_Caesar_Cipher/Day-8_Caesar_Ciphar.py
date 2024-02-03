import Caesar_Ciphar_logo
print(Caesar_Ciphar_logo.logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
# text = input("Type your message: \n").lower()
# shift = int(input("Type the shift number: \n"))


# def encrypt(msg, shift_num):
#     encrypted_msg = ""
#     for letter in msg:
#         position = alphabets.index(letter)
#         new_position = position + shift_num
#         if new_position > len(alphabets)-1:
#             new_position -= len(alphabets)
#         encrypted_msg += alphabets[new_position]
#     print(encrypted_msg)

# def decrypt(msg, shift_num):
#     decrypted_msg = ""
#     for letter in msg:
#         position = alphabets.index(letter)
#         new_position = position - shift_num
#         if new_position < 0:
#             new_position += len(alphabets)
#         decrypted_msg += alphabets[new_position]
#     print(decrypted_msg)


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Choose the direction either 'encode' or 'decode'.")


def caesar(text_direction, text, shift_num):
    end_text = ""
    shift_num %= 26
    if text_direction == "decode":
        shift_num *= -1
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_num
            if text_direction == "encode" and new_position > len(alphabets)-1:
                new_position -= len(alphabets)
            if text_direction == "decode" and new_position < 0:
                new_position += len(alphabets)
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"The {text_direction}d code is '{end_text}'")


end_conversion = False
while not end_conversion:    
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(direction, text, shift)
    usr_input = input("Type 'yes' if You want to do again, Otherwise type 'no': \n").lower()
    if usr_input == 'no':
        end_conversion = True