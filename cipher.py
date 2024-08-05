def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            if char.islower():
                encrypted_text += chr((char_code - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((char_code - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def main():
    text = input("Please enter a sentence: ")
    shift = 5
    encrypted_text = caesar_cipher(text, shift)
    print("The encrypted sentence is:", encrypted_text)

if __name__ == "__main__":
    main()

