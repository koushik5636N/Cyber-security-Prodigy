# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts the given text using the Caesar cipher.

    :param text: The text to encrypt or decrypt.
    :param shift: The number of positions to shift.
    :param mode: 'encrypt' or 'decrypt' mode.
    :return: The encrypted or decrypted text.
    """
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and handle wrapping around the alphabet
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '3':
            print("Exiting the program.")
            break

        if choice not in ['1', '2']:
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        text = input("Enter the text: ").strip()
        shift = int(input("Enter the shift value (integer): ").strip())

        if choice == '1':
            encrypted_text = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            decrypted_text = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
