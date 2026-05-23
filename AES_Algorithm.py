from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import os


# Function to add padding
def pad(data):
    block_size = 16
    padding = block_size - len(data) % block_size
    return data + bytes([padding]) * padding


# Function to remove padding
def unpad(data):
    padding = data[-1]
    return data[:-padding]


# Encrypt Image
def encrypt_image(input_file, output_file, key):

    with open(input_file, "rb") as file:
        image_data = file.read()

    cipher = AES.new(key, AES.MODE_CBC)

    encrypted_data = cipher.encrypt(pad(image_data))

    with open(output_file, "wb") as file:
        file.write(cipher.iv)
        file.write(encrypted_data)

    print("Image Encrypted Successfully!")


# Decrypt Image
def decrypt_image(input_file, output_file, key):

    with open(input_file, "rb") as file:

        iv = file.read(16)
        encrypted_data = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    decrypted_data = unpad(cipher.decrypt(encrypted_data))

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("Image Decrypted Successfully!")


# Main Program
print("=== AES Image Encryption Tool ===")

print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice: ")

input_file = input("Enter input image file: ")
output_file = input("Enter output file name: ")

# AES key must be 16, 24, or 32 bytes
secret_key = b'1234567890abcdef'


if choice == "1":
    encrypt_image(input_file, output_file, secret_key)

elif choice == "2":
    decrypt_image(input_file, output_file, secret_key)

else:
    print("Invalid Choice")
