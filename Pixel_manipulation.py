from PIL import Image

# Encryption Function
def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size

    # Encrypt by swapping pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (b, r, g))  # Swapping pixel values

    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    return encrypted_image_path

# Decryption Function
def decrypt_image(encrypted_image_path):
    img = Image.open(encrypted_image_path)
    width, height = img.size

    # Decrypt by swapping pixel values back
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (g, b, r))  # Swapping pixel values back

    decrypted_image_path = "decrypted_image.png"
    img.save(decrypted_image_path)
    return decrypted_image_path

# Main Program
image_path = image_path ="C:\\Users\\HP\\Pictures\\Saved Pictures\\db20a65d166dd992b28489753b3ab3e0.jpg"

# Encrypt the image
encrypted_image_path = encrypt_image(image_path)
print("Image encrypted successfully. Encrypted image saved as:", encrypted_image_path)

# Decrypt the encrypted image
decrypted_image_path = decrypt_image(encrypted_image_path)
print("Image decrypted successfully. Decrypted image saved as:", decrypted_image_path)