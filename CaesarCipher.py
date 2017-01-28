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
    return output

def decrypt(message, key):
    output = ''
    for letter in message:

        ascii_letter = ord(letter)

        #lower case
        if(ascii_letter in range(97,122)):
            ascii_letter-=key
            if(ascii_letter<97):
                ascii_letter+=26
            output += chr((ascii_letter)%122+(0 if ascii_letter>96 else 97))
        #upper case
        if (ascii_letter in range(65, 90)):
            ascii_letter -= key
            if (ascii_letter < 65):
                ascii_letter += 26
            output += chr((ascii_letter)%90+(0 if ascii_letter>64 else 65))
    return output

decrypt(encrypt(input("what message would you like to encrypt?"), int(input("what is your key?"))),int(input("what is your key?")))
