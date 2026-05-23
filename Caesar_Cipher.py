# Write down the plaintext message: HELLO
# Choose a shift value. In this case, we will use a shift of 3.
# Replace each letter in the plaintext message with the letter that is three positions to the right in the alphabet.
#  H becomes K (shift 3 from H)       
#  E becomes H (shift 3 from E)    
#  L becomes O (shift 3 from L)       
#  L becomes O (shift 3 from L)         
#  O becomes R (shift 3 from O)


# Caesar Cipher Program

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Check if character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result += encrypted_char
        else:
            # Keep spaces and special characters unchanged
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted_text = encrypt(message, shift)
print("\nEncrypted Message:", encrypted_text)

# Decryption
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Message:", decrypted_text)