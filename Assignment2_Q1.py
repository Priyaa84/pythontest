###############################################################################################################
# Problem 1 (25 points)
# In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# by A, E would become B, and so on.
# Encrypt an input string of lowercase letters (plaintext, first input) and prints
# the result.  The other input is the distance value (distance).
###############################################################################################################
letters_to_move = ''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_phrase = ''

word_to_encrypt = input("Enter Your Secret Phrase: ")

while letters_to_move == '':
    try:
        letters_to_move = int(input("How Many Letters Do You Want to Shift? "))
    except:
        print("\nPlease Enter a Valid Integer")


for letter in word_to_encrypt:
    if letter in letters:
        position = letters.index(letter) + letters_to_move
        if position > 26:
            new_position = position - 26
        else:
            new_position = position
        new_phrase = new_phrase + (letters[new_position])

    else:
        new_phrase = new_phrase + (letter)

print(new_phrase)

