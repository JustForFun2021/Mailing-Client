from os import read
from cryptography.fernet import Fernet
 #create a key
# key = Fernet.generate_key()

#When every we run this code we will create a new key 
# with open('mykey.key','wb') as mykey:
#     mykey.write(key)

#To avoid create a new key and reuse the same key

with open('mykey.key','rb') as mykey:
    key = mykey.read()

#print(key)

# f = Fernet(key)

# with open('Mailing Client/password.txt','rb') as original_file:
#     original = original_file.read()

# #encrypt the data

# encrypted = f.encrypt(original)

# with open('encryptedpassword.txt','wb') as encrypted_password_file:
#     encrypted_file = encrypted_password_file.write(encrypted)

#Decrypt Part

f = Fernet(key)

with open('encryptedpassword.txt','rb') as encrypted_password_file:
    encrypte_file = encrypted_password_file.read()

decrypt = f.decrypt(encrypte_file)

with open('decryptedpassword.txt','wb') as decrypted_password_file:
    decrypted_file = decrypted_password_file.write(decrypt)


