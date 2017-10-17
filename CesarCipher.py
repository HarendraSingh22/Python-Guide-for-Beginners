# cesar cipher

# ------- ENCRYPTION -----------------------------
def encrypt():
    lookup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    print("Please enter your plaintext: ")
    plaintext = input()
    print("Please enter your key :")
    key = int(input())
    for character in plaintext:
        if character in lookup:
            # encrypt
            position = (lookup.index(character) + key) % 26
            # swap characters
            character = lookup[position:position + 1]
        # reassemble ciphertext
        ciphertext += character
    print("Here's your ciphertext: ", ciphertext)


# ------ DECRYPTION -----------------------------
def decrypt():
    lookup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    print("Please enter your ciphertext:")
    ciphertext = input()
    print("Please enter your key: ")
    key = int(input())
    for character in ciphertext:
        if character in lookup:
            # decrypt
            position = (lookup.index(character) - key) % 26
            # swap characters
            character = lookup[position:position + 1]
        # reassemble plaintext
        plaintext += character
    print("Here's your plaintext: ", plaintext)


# ------- BRUTE-FORCE DECRYPT ---------------
def decrypt_brute_force():
    lookup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    print("Please enter your ciphertext: ")
    ciphertext = input()
    key = 0
    counter = 0
    while key < 26:
        for character in ciphertext:
            if character in lookup:
                # decrypt
                position = (lookup.index(character) - key) % 26
                # swap characters
                character = lookup[position:position + 1]
            # reassemble plaintext
            plaintext += character
        print("Here's your plaintext", counter, ": ", plaintext)
        plaintext = ''
        key += 1
        counter += 1


def main():
    key = -1
    position = -1
    choice = 'invalidchoice'
    crypt_on = 'y'

    print("Welcome to Cesar cipher!")
    while crypt_on == 'y':
        print("Would you like to encrypt, decrypt by key or decrypt by brute-force (e/dk/db)?")
        choice = input()
        if choice == 'e':
            encrypt()
        elif choice == 'dk':
            decrypt()
        elif choice == 'db':
            decrypt_brute_force()
        else:
            print("Invalid choice! Please choose e for encryption, dk for decryption with key or db for brute-force.")
        print("Would you like to continue (y/n)?")
        crypt_on = input()


if __name__ == "__main__":
    main()


