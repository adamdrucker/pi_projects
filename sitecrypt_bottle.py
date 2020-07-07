from random import randint
from random import seed
import random
import time
import os


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHAUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNC = ",.:;!?@#$%^&*-_`~/\[]{}()<>'\""   # 29 length

# Seed to init random generator
seed(random.randint(random.randint(0, 255), (random.randint(256, 511))))

# Generate two random numbers to be used in the OTP randomization
r = random.randint(random.randint(0, 251), random.randint(257, 509))
s = random.randint(random.randint(521, 1021), random.randint(1031, 2039))

# Create one-time pad with randomized numbers
def generate_otp(length):
        with open("otp.txt", "w") as f:
            for i in range(length):
                f.write(str(random.randint(r, s)) + "\n")


# // File functions //
# ///////////////////
def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

def get_plaintext():
    plain_text = input("Please type your message: ")
    return plain_text

def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)



# // Encryption //
# ///////////////

''' This function takes in a plaintext message and an OTP sheet from 
    the ones generated in the first menu option. Any characters not in
    the ALPHABET/ALPHAUP/PUNC variables are added as is to the CIPHERTEXT variable.
    The ENCRYPTED value is derived from the index of each character in the ALPHABET
    plus the value in the 0-based corresponding position of the OTP text file.
    This is then modulus divided by the length of the string and the corresponding
    character at the index position is chosen as the ciphertext character.
'''

def encrypt(plaintext, sheet):
    ciphertext = ''
    for position, character in enumerate(plaintext):      
        if character in ALPHABET:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
        elif character in ALPHAUP:
            encrypted = (ALPHAUP.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHAUP[encrypted]
        elif character in PUNC:
            encrypted = (PUNC.index(character) + int(sheet[position])) % 29
            ciphertext += PUNC[encrypted]
        else:
            ciphertext += character
            #print("Alphabet index char is: ", ALPHABET.index(character))
            #print("Sheet pos is: ", int(sheet[position]))
            #print("Value of encrypted is: ", encrypted)
    return ciphertext


# // Decryption //
# ///////////////

''' Essentially the same operation as above, except characters in the CIPHERTEXT
    message are being applied to the PLAINTEXT variable, and index/sheet positions
    are subtracted from one another rather than added.
'''

def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character in ALPHABET:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
        elif character in ALPHAUP:
            decrypted = (ALPHAUP.index(character) - int(sheet[position])) % 26
            plaintext += ALPHAUP[decrypted]
        elif character in PUNC:
            decrypted = (PUNC.index(character) - int(sheet[position])) % 29
            plaintext += PUNC[decrypted]
        else:
            plaintext += character
    return plaintext


# --------------------------------------------------------------------------------
#generate_otp(100)                       # Creates one 100-line text file called otp.txt
#sheet = load_sheet("otp.txt")           # Loads sheet for use in encryption
#plaintext = get_plaintext()             # Asks user for input
#ciphertext = encrypt(plaintext, sheet)  # Encrypts user input
#save_file("encrypted.txt", ciphertext)  # Saves encrypted message as encrypted.txt
#print(load_file("encrypted.txt"))       # Prints ciphertext

#time.sleep(2)
#print("Decrypting previous message...")
#time.sleep(2)

#ciphertext = load_file("encrypted.txt") # Loads encrypted contents into variable
#plaintext = decrypt(ciphertext, sheet)  # Decryption assigned to plaintext variable
#print(plaintext)

#time.sleep(1)
#print("Removing One-Time Pad...")
#os.remove("otp.txt")    # Delete otp file from local directory
#time.sleep(0.5)
#print("Removing encrypted text file...")
#os.remove("encrypted.txt")  # Delete encrypted text file from local directory
# --------------------------------------------------------------------------------
# How would both of those deletes work in the context of the website? Where would they
# initially be stored?

# Turn this stuff into functions

