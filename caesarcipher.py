try: 
    import pyperclip # pyperclip is a cross-platform clipboard module for Python. It allows you to copy and paste text between different applications on your computer.
except ImportError:
    pass # Do nothing

# Every possible symbol that can be encrypted/decrypted:
# You can add numbers and special symbols to encrypt them as well
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar Cipher')
print('The Caesar cipher is a simple encryption method in which each letter of the plaintext is shifted a key number of times.')
print('For example, a key of 2 means the letter A is encrypted to C, the letter B is encrypted to D and so on.')
print()

# Let the user enter if they are encrypting or decrypting
while True: # Keep asking until user enters e or d
    print('Do you want to encrypt (e) or decrypt (d)? ')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter e or d.')

# Let the user enter the key to use for encryption/decryption
while True: # Keep asking until user enters a valid key
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
# Let the user enter the message they want to encrypt/decrypt
print('Enter the message you want to {}.'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters
message = message.upper()

# Stores the encrypted/decrypted form of the message
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) symbol for this letter
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key
        
        # Handle the wrap-around case where a number exceeds the length of SYMBOLS or is less than 0
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)
        
        # Add encrypted/decrypted number's symbol to translated
        translated += SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting
        translated += symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed