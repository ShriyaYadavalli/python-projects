import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decrypted_text = ""
encrypted_text = ""
print(art.logo)


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    original_text = original_text.lower()

    for char in original_text:
        if char in alphabet:
            num = alphabet.index(char)
            new_char = alphabet[(num + shift_amount) % len(alphabet)]
            encrypted_text += new_char
        else:
            encrypted_text += char

    print(encrypted_text)

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    original_text = original_text.lower()

    for char in original_text:
        if char in alphabet:
            num = alphabet.index(char)
            new_char = alphabet[(num - shift_amount) % len(alphabet)]
            decrypted_text += new_char
        else:
            decrypted_text += char

    print(decrypted_text)


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode": 
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid direction")
    
    if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "yes":
        caesar()
    else:
        print("Goodbye")

caesar()