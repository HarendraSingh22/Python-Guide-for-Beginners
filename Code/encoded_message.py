"""Python Code For Beginners"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newmMessage = ''

message = input('Please enter a message: ')

for character in message:  # for loop
    if character in alphabet:
        position = alphabet.find(character)
        # Finds the position of the character in variable 'alphabet'
        
        newPosition = (position + key) % 26
        # Returns as new position
        
        newCharacter = alphabet[newPosition]
        # Returns a different character
        
        print('The new character is:', newCharacter)
        newmMessage += newCharacter
        # Prints out the character one at a time
        
    else:
        newmMessage += character

print('The new message is:', newmMessage)
