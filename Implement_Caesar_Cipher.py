def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
      
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
      
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  

    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))

    if shift < 0 or shift > 25:
        print("Shift value must be between 0 and 25.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
