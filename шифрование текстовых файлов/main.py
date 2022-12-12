import pyAesCrypt

passowrd = input("Enret the passowrd: ")

# encrypt
pyAesCrypt.encryptFile("data.txt", "data_2.txt", passowrd)

#decrypt
pyAesCrypt.decryptFile("data_2.txt", "data_out.txt", passowrd)