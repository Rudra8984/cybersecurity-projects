def encrypt(input,cipher):
    encrypttext=""
    for i in input:
        if i.isalpha():
            encrypttext+=chr((ord(i)-65+cipher)%26 +65) if i.isupper() else chr((ord(i)-97+cipher)%26 +97)
        else:
            encrypttext += i
    return encrypttext

def decrypt(input,cipher):
    decrypttext=""
    for i in input:
        if i.isalpha():
           decrypttext+=chr((ord(i)-65-cipher)%26 +65) if i.isupper() else chr((ord(i)-97-cipher)%26 +97)
        else:
            decrypttext += i
    return decrypttext


def main():
    while True:  
        choice = input("> 1. Encrypt\n> 2. Decrypt\n> 3. Exit\n> Choose an option: ")

        if choice == '1':
            text = input("> Enter your text: ")
            cipher = int(input("> Enter cipher: "))
            result = encrypt(text, cipher)
            print(">Encrypted:", result)
        elif choice == '2':
            text = input("> Enter your text: ")
            cipher = int(input("> Enter cipher: "))
            result = decrypt(text, cipher)
            print(">Decrypted:", result)
        elif choice == '3':
            print(">Thanks for using our service")
            break 
        else:
            print(">Invalid choice")


if __name__ == "__main__":
    main()
             