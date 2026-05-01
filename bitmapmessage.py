'''Bitmap Message,
Displays a text message according to the provided bitmap image'''

import sys

bitmap = """
   ....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
...................................................................."""

print('Bitmap message')
print('Enter your message: ')
message = input('> ')
if message == '':
    sys.exit()

# loop over each line in the bitmap
for line in bitmap.splitlines():
    # Loop over each character in the line
    for i, bit in enumerate(line):
        if bit == ' ':
            # If the bit is a space, print the corresponding character from the message
            print(' ', end='')
        else:
            # Print a character from the message
            print(message[i % len(message)], end='')
    print() # Print a newline
