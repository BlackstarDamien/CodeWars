from cryptography.fernet import Fernet

text = input(" Please type text you want to ciphered")
text_to_cipher = str.encode(text)
key = Fernet.generate_key()
cipher = Fernet(key)
ciphered_text = cipher.encrypt(text_to_cipher)
deciphered_text = cipher.decrypt(ciphered_text)

print("Text you ciphered is: " + text)
print("Text after using this script is: " + str(ciphered_text))
