message = input("what message would you like to encrypt?")

for letter in message:
    print(ord(letter))
    ascii_letter = ord(letter)
    #lower case
    if(ascii_letter in range(97,122)):
        print(chr((ascii_letter+3)%122+(0 if ascii_letter>96 else 97)))
    #upper case
    if (ascii_letter in range(65, 90)):
        print(chr((ascii_letter+3)%90+(0 if ascii_letter>64 else 65)))