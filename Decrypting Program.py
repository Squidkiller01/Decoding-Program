'''
Michael Porter 2024 senior capstone program

This program is designed to decode from a chosen decryption/encoding method
'''
# Import necessary libraries
import base64 # Import base64 module for Base64 decoding
import string # Import string module for character manipulation
import binascii # Import binascii module for handling binary-to-text encoding/decoding
from builtins import divmod # Import the divmod function from the builtins module

# Function to decrypt a Caesar cipher
def caesar_cipher_decrypt(ciphertext,shift):
    # Initialize an empty string to store the decrypted plaintext
    plaintext = ""
    # Iterate through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the ASCII offset based on the character's case
            ascii_offset = 65 if char.isupper() else 97
            # Decrypt the character using the Caesar cipher algorithm
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            decrypted_char = char
        # Append the decrypted character to the plaintext string
        plaintext += decrypted_char
    #Return the decrypted plaintext
    return plaintext

# Function to decode a Base64 encoded text
def base64_decode(ciphertext):
    try:
        # Decode the Base64 encoded text and convert it to UTF-8
        decoded_bytes = base64.b64decode(ciphertext)
        plaintext = decoded_bytes.decode('utf-8')
        # Return the decoded plaintext
        return plaintext
    except binascii.Error:
        # Handle the case of invalid Base64 encoding
        return "Invalid Base64 encoding"
    
# Function to decrypt an Atbash cipher
def atbash_cipher_decrypt(ciphertext):
    # Initialize an empty string to store the decrypted plaintext
    plaintext = ""
    # Iterate through each character in the ciphertext
    for char in ciphertext:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the ASCII offset based on the character's case
            ascii_offset = 65 if char.isupper() else 97
            # Decrypt the character using the Atbash cipher algorithm
            decrypted_char = chr(25 - (ord(char) - ascii_offset) + 2 * ascii_offset)
        else:
            #If the charater is not an alphabet letter, leave it unchanged
            decrypted_char = char
        #Append the decrypted character to the plaintext string
        plaintext += decrypted_char
    #Return the decrypted plaintext
    return plaintext

# Function to decrypt a ROT13 cipher
def rot13_cipher_decrypt(ciphertext):
    # Use the built-in translate method to perform ROT 13 decryption
    return ciphertext.translate(str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                              string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                                              string.ascii_uppercase[13:] + string.ascii_uppercase[:13]))

#Function to decrypt a keyword cipher with a specified keyword
def keyword_decrypt(ciphertext,keyword):
    #Generate the keyword cipher alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = ''.join(dict.fromkeys(keyword.upper() + alphabet))  # Remove duplicates and append remaining alphabet

    #Create the decryption table
    table = []
    for char in keyword:
        if char in alphabet:
            table.append(alphabet.replace(char,'',1)+char) # Append shifted alphabet to table

    #Decrypt the ciphertext
    plaintext = ''
    for char in ciphertext.upper():
        if char in alphabet:
            idx = table[0].index[char] # Get index of character in first row of table
            plaintext += alphabet[idx] # Append decrypted character
            table.append(table.pop(0)[1:] + table[0][0]) # Shift the table
        else:
            plaintext += char # Append non-alphabetic characters

    return plaintext

# Main function to interact with the user and execute the selected decryption method
def main():
    # Display the menu of cipher options
    print("Select the cipher to decode: \n1. Caesar Cipher \n2. Base64 \n3. Atbash Cipher \n4. ROT13 \n5. Keyword Cipher")

    #Prompt the user to choose a cipher option
    choice = input("Enter your method of decryption (1,2,3...): ")

    # Based on the user's choice, execute the corresponding decryption method
    if choice == "1": #Choice for Caesar Cypher Decoding
        ciphertext = input("Enter the ciphertext: ")
        shift = int(input("Enter the Caesar cipher shift (left = negative, right = positive): "))
        plaintext = caesar_cipher_decrypt(ciphertext, shift)
        print("Decoded plaintext", plaintext)
    elif choice == "2": #Choice for Base64 decoding
        ciphertext = input("Enter the Base64 cipher text: ")
        plaintext = base64_decode(ciphertext)
        print("Decoded plaintext:", plaintext)
    elif choice == "3": #Choice for Atbash decoding
        ciphertext = input("Enter the ciphertext: ")
        plaintext = atbash_cipher_decrypt(ciphertext)
        print("Decoded plaintext:", plaintext)
    elif choice == "4": #Choice for ROT13 deocoding
        ciphertext = input("Enter the ciphertext: ")
        plaintext = rot13_cipher_decrypt(ciphertext)
        print("Decoded plaintext:", plaintext)
    elif choice == "5": #Choice for Keyword decoding
        ciphertext = input("Enter the ciphertext: ")
        keyword = input("Enter the keyword cipher keyword: ")
        plaintext = keyword_decrypt(ciphertext, keyword)
        print("Decoded plaintext", plaintext)
    else:
        print("Invalid choice")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()