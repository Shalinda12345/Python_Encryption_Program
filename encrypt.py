import string

def encrypt_and_decrypt():
    i = int(input("Encrypt (1) or Decrypt (2): "))
    chars = " " + string.punctuation + string.digits + string.ascii_letters + "\n"
    chars = list(chars)
    key = chars.copy()
    key.reverse()
    # print(f"chars: {chars}")
    # print(f"key : {key}")

    if i == 1:
        # Encrypt
        plain_text = input("Enter the message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        print(f"Original Message: {plain_text}")
        print(f"Encrypted Message: {cipher_text}")
    elif i == 2:
        # Decrypt
        cipher_text = input("Enter the message to decrypt: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]

        print(f"Original Message: {cipher_text}")
        print(f"Encrypted Message: {plain_text}")
    else:
        print("Exiting the Program Enter 1 or 2")
        quit()

    return encrypt_and_decrypt()

encrypt_and_decrypt()
