def encrypt(message, key):
    output = ''
    for letter in message:

        ascii_letter = ord(letter)+key

        #lower case
        if(ascii_letter in range(97,122)):
            output += chr((ascii_letter)%122+(0 if ascii_letter>96 else 97))
        #upper case
        if (ascii_letter in range(65, 90)):
            output += chr((ascii_letter)%90+(0 if ascii_letter>64 else 65))
    print(output)

def decrypt(message, key):
    print(encrypt(message,-1*int(key)))

encrypt(input("what message would you like to encrypt?"), int(input("what is your key?")))