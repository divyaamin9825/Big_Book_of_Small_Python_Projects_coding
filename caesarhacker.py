print("Caesar Cipher Hacker")

# Let the user specify the message to hack
print("Enter the encrypted Caesar cipher message to hack:")
message = input('> ')

# Every possible symbol that can be encrypted/decrypted
# This must match the SYMBOLS used when encyrpting the message
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possible key
    translated = ''

    # Decrypt each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the symbol
            num -= key # Decrypt the number

        # Handle the wrap-around if num is less than 0
            if num < 0:
                num += len(SYMBOLS)
            
            translated += symbol # Add the decrypted symbol to translated

        else:
            # Just add the symbol without decrypting
            translated += symbol
    
    # Display the key being tested, along with its decrypted text
    print(f'Key #{key}: {translated}')
