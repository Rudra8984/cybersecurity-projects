from PIL import Image

def encrypt_image(input_image, output_image, key):
    
    image = Image.open(input_image)
    width, height = image.size
 
    image = image.convert("RGB")

    encrypted_image = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            r = r ^ key
            g = g ^ key
            b = b ^ key
            encrypted_image.putpixel((x, y), (r, g, b))

    encrypted_image.save(output_image)

def decrypt_image(input_image, output_image, key):
    
    encrypted_image = Image.open(input_image)
    width, height = encrypted_image.size

    decrypted_image = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = encrypted_image.getpixel((x, y))
            r = r ^ key
            g = g ^ key
            b = b ^ key
            decrypted_image.putpixel((x, y), (r, g, b))

    decrypted_image.save(output_image)

input_image_path = "input_image.jpg"
encrypted_image_path = "encrypted_image.jpg"
decrypted_image_path = "decrypted_image.jpg"
key = 128  

t=int(input(">what do you want to do : \n>1.encrypted\n>2.decrypted\n >"))
if t==1:
    encrypt_image(input_image_path, encrypted_image_path, key)
elif t==2:
    decrypt_image(encrypted_image_path, decrypted_image_path, key)
else :
    print("invalid input!")