'''
Michael Porter 2024 senior capstone program

This program is designed to decode from a chosen decryption/encoding method
'''
# Import necessary libraries
import base64 # Import base64 module for Base64 decoding
import string # Import string module for character manipulation
import binascii # Import binascii module for handling binary-to-text encoding/decoding
from builtins import divmod # Import the divmod function from the builtins module

def variable_initialization():
    ciphertext = None
    plaintext = None
    keyword = None
    encryption_method = None
    return ciphertext,plaintext,keyword, encryption_method


### Decryption Functions


# Function to decrypt a Caesar cipher
def caesar_cipher_decrypt(ciphertext, shift):
    # Normalize the shift value within the range of 0 to 25
    shift = shift % 26
    
    # Initialize an empty string to store the decrypted plaintext
    plaintext = ""
    
    # Iterate through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the ASCII offset based on the character's case
            ascii_offset = 65 if char.isupper() else 97
            
            # Calculate the decrypted character's ASCII code
            decrypted_ascii = ord(char) - shift
            
            # Wrap around if the decrypted ASCII code is out of range
            if char.isupper():
                decrypted_ascii = (decrypted_ascii - 65) % 26 + 65
            else:
                decrypted_ascii = (decrypted_ascii - 97) % 26 + 97
            
            # Convert the decrypted ASCII code to a character
            decrypted_char = chr(decrypted_ascii)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            decrypted_char = char
        
        # Append the decrypted character to the plaintext string
        plaintext += decrypted_char
    
    # Return the decrypted plaintext
    return plaintext

# Function to decode a Base64 encoded text
def base64_decode(character_set=None):
    if character_set is not None:
        if character_set.lower() not in ['UTF-8','ascii']:
            raise ValueError("Invalid character set. Supported character sets are 'utf-8' and 'ascii'.")
    else:
        character_set = input("\nEnter the character set to use (utf-8 or ascii, press Enter for default utf-8): ").lower().strip()
        if character_set and character_set not in ['utf-8', 'ascii']:
            raise ValueError("Invalid character set. Supported character sets are 'utf-8' and 'ascii'.")
        
    encoded_message = input("\nEnter the Base64 encoded message: ")

    #Decode the Base64 encoded message
    decoded_bytes = base64.b64decode(encoded_message)

    #Convert the decoded bytes to a string using the specified character set
    decoded_message = decoded_bytes.decode(character_set)

    return decoded_message
    
# Function to decrypt an Atbash cipher
def atbash_cipher_decrypt(ciphertext):
    # Define the normal and reversed alphabets
    normal_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    # Initialize an empty string to store the decrypted plaintext
    plaintext = ""

    #Iterate through each character in the ciphertext
    for char in ciphertext.upper():
        #Check if the character is an alphabet letter
        if char.isalpha():
            #Determine the index of the character in the normal alphabet
            idx = normal_alphabet.find(char)

            #Replace the character with its corresponding letter from the reversed alphabet
            decrypted_char=reversed_alphabet[idx]
        else:
            #If the character is not an alphabet letter, leave it unchanged
            decrypted_char = char
        
        #Append the decrypted character to the plaintext string
        plaintext += decrypted_char

    # Return the decrypted plaintext
    return plaintext
    

# Function to decrypt a ROT13 cipher
def rot13_cipher_decrypt(ciphertext):
    # Use the built-in translate method to perform ROT 13 decryption
    return ciphertext.translate(str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                              string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                                              string.ascii_uppercase[13:] + string.ascii_uppercase[:13]))


### Encryption Functions

#Function to encrypt a plaintext using the Caesar Cipher
def caesar_cipher_encrypt(plaintext,shift):
    #Normalize the shift value within the range of 0 to 25
    shift = shift % 26

    #Initialize an empty string to store the encrypted ciphertext
    ciphertext=""

    #Iterate through each character in the plaintext
    for char in plaintext:
        #Check if the character in an alphabet letter
        if char.isalpha():
            # Determine the ASCII offset based on the character's case
            ascii_offset = 65 if char.isupper() else 97

            #Calculate the encrypted character's ASCII code
            encrypted_ascii = ord(char) + shift

            #Wrap around if the encrypted ASCII code is out of range
            if char.isupper():
                encrypted_ascii = (encrypted_ascii - 65) % 26 + 65
            else:
                encrypted_ascii = (encrypted_ascii - 97) % 26 + 97

            #Convert the encrypted ASCII code to a character
            encrypted_char = chr(encrypted_ascii)
        else:
            #If the character is not an alphabet letter, leave it unchanged
            encrypted_char=char
        
        #Append the encrypted character to the ciphertext string
        ciphertext += encrypted_char
    
    #Return the encrypted ciphertext
    return ciphertext

#Function to encode a message using Base64 with the specified character set
def base64_encode(character_set=None):
    if character_set is not None:
        if character_set.lower() not in ['utf-8','ascii']:
            raise ValueError("Invalid character set. Supported character sets are 'utf-8' and 'ascii'.")
    else:
        character_set = input("\nEnter the character set to use (utf-8 or ascii, press Enter for default utf-8): ").lower().strip()
        if character_set and character_set not in ['utf-8', 'ascii']:
            raise ValueError("Invalid character set. Supported character sets are 'utf-8 and 'ascii'.")
        
    message = input("\nEnter the message to encode: ")

    #Convert the message to bytes using the specified character set
    message_bytes = message.encode(character_set)

    #Use the base64 module to encode the message
    encoded_bytes = base64.b64encode(message_bytes)

    #Convert the encoded bytes back to a string
    encoded_message = encoded_bytes.decode('ascii')

    return encoded_message

#Function to encode a message using the Atbash cipher
def atbash_cipher_encode(message):
    # Define the normal and reversed alphabets
    normal_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    #Initialize and empty string to store the encoded message
    encoded_message=""

    #Iterate through each character in the message
    for char in message.upper():
        #Check if the character is an alphabet letter
        if char.isalpha():
            #Determine the index of the character in the normal alphabet
            idx = normal_alphabet.find(char)

            #Replace the character with its corresponding letter from the reversed alphabet
            encoded_char = reversed_alphabet[idx]
        elif char == ' ': #Check if the character is a space
            #If it is a space, include it in the encoded message without modification
            encoded_char=char
        else:
            #If the character is not an alphabet letter from the reversed alphabet
            encoded_char = reversed_alphabet[idx]

        # Append the encoded character to the encoded message string
        encoded_message += encoded_char
    
    return encoded_message

#Function to encode a message using the ROT13 cipher
def rot13_cipher_encrypt(plaintext):
    #Create translation tables for lowercase and uppercase characters
    lowercase_table = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    uppercase_table = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]

    #Apply translation using the built-in translate method
    translation_table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                      lowercase_table + uppercase_table)
    return plaintext.translate(translation_table)


# Function to display list of available ciphers and/or menu options
def display():
    print("\nAvailable options: \n0. Quit Program \n1. Go Back \n2. Caesar Cipher \n3. Base64 \n4. Atbash Cipher \n5. ROT13")

# Main function to interact with the user and execute the selected decryption method
def main():
    exit_keywords = ["exit", "quit", "exit program", "quit program", "0"]
    back_keywords = ["back", "go back","1"]
    plaintext, ciphertext, keyword, encryption_method = variable_initialization()

    while encryption_method == None:
        encryption_method = input("\nWould you like to encrypt or decrypt a message? Type 'encrypt', 'decrypt', or 'quit' to exit the program: ")
        encryption_method.lower()
        
        if encryption_method == "encrypt": # Encoding a cipher
            encode = None

            #Prompt the user to choose a cipher option
            while encode == None:

                #Display available ciphers
                display()

                encode = input("\nPlease enter the chosen cipher.")
                encode.lower()

                #Based on the user's choice, execute the corresponding encryption method
                if encode in exit_keywords: #Quitting the program
                    quit
                elif encode in back_keywords: #Leaving the menu
                    encryption_method = None
                    continue
                elif encode == "caesar" or encode == "2": #Caesar Cipher Encoding
                    plaintext = input("\nEnter the plaintext: ")
                    shift = int(input("\nEnter the Caesar cipher shift (Must be an integer) \nLeft = Negative (-) Number \nRight = Positive Number \nShift: "))
                    print("Ciphertext: ", caesar_cipher_encrypt(plaintext,shift))
                elif encode == "base64" or encode == "3": #Base64 Encoding
                    print("Ciphertext: ", base64_encode())
                elif encode == "atbash" or encode == "4": #Atbash Encoding 
                    plaintext = input("\nEnter the plaintext: ")
                    print("Ciphertext:", atbash_cipher_encode(plaintext))
                elif encode =="rot13" or encode == "5": #Rot13 encoding
                    plaintext = input("\nEnter the plaintext: ")
                    print("Ciphertext: ", rot13_cipher_encrypt(plaintext))
                else:
                    print("\nInvalid choice")

                # Reset variable so the program will repeat until the user says otherwise
                encode = None
                
        elif encryption_method == "decrypt": # Decoding a cipher
            decode = None

            #Display available ciphers
            display()

            #Prompt the user to choose a cipher option
            while decode == None:
                decode = input("\nPlease enter the chosen cipher. ")
                decode.lower()

                # Based on the user's choice, execute the corresponding decryption method
                if decode in exit_keywords: #Quitting the program
                    quit
                elif decode in back_keywords: #leaving the menu
                    encryption_method == None
                    continue
                elif decode == "caesar" or decode == "2": #Caesar Cipher Decoding
                    ciphertext = input("\nEnter the ciphertext: ")
                    shift = int(input("\nEnter the Caesar cipher shift (Must be an integer) \nLeft = Negative (-) Number \nRight = Positive Number \nShift: "))
                    print("\nDecoded plaintext", caesar_cipher_decrypt(ciphertext, shift))
                elif decode == "base64" or decode == "3": #Base64 decoding
                    print("Decoded plaintext: ", base64_decode())
                elif decode == "atbash" or  decode == "4": #Atbash decoding
                    ciphertext = input("\nEnter the ciphertext: ")
                    print("\nDecoded plaintext:", atbash_cipher_decrypt(ciphertext))
                elif decode == "rot13" or  decode == "5": #ROT13 deocoding
                    ciphertext = input("\nEnter the ciphertext: ")
                    print("\nDecoded plaintext:", rot13_cipher_decrypt(ciphertext))
                else:
                    print("\nInvalid choice")
                
                # Reset variable so the program will repeat until the users says otherwise
                decode = None
        elif encryption_method in exit_keywords:
            quit
        else:
            print("Invalid choice")
            encryption_method = None

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
