import string

file_name = input("Enter File Path or Name if in the Same Directory to Encrypt: ")

# print("Before: ")
x = open(file_name, 'r')
y = x.read()
# print(y)

chars = " " + string.punctuation + string.digits + string.ascii_letters + "\n"
chars = list(chars)
key = chars.copy()
key.reverse()
# print(f"chars: {chars}")
# print(f"key : {key}")

plain_text = y
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    encrypted_file = open(f'encrypted_{file_name}', 'w')
    encrypted_file.write(cipher_text)

# print(f"Original Message: {plain_text}")
# print(f"Encrypted Message: {cipher_text}")

print(f"File has been encrypted successfully in a new file as encrypted_{file_name}")

x.close()