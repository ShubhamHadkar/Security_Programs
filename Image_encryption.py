from PIL import Image


# Encrypt Image
def encrypt_image(input_image, output_image, key):

    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):

            r, g, b = pixels[x, y]

            # Apply encryption using key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Image Encrypted Successfully!")


# Decrypt Image
def decrypt_image(input_image, output_image, key):

    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse encryption
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Image Decrypted Successfully!")


# Main Program
print("=== Image Encryption Tool ===")

print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice: ")

input_image = input("Enter image file name: ")
output_image = input("Enter output image name: ")
key = int(input("Enter encryption key: "))


if choice == "1":
    encrypt_image(input_image, output_image, key)

elif choice == "2":
    decrypt_image(input_image, output_image, key)

else:
    print("Invalid Choice")
