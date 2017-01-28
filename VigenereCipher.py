def encrypt(message, key):
    counter = 0
    output=''

    for letter in message:
        ascii_letter = ((ord(letter)-97+ord(key[counter])-97) %26)+98
        counter = (counter+1)%len(key)
        output+=chr(ascii_letter)
    return output

def decrypt(message, key):
    counter = 0
    output=''

    for letter in message:
        ascii_letter = ((ord(letter)-ord(key[counter])))
        counter = (counter+1)%len(key)
        if ascii_letter < 0:
            output+=chr(ascii_letter+122)
        else:
            output+=chr(ascii_letter+96)
    return output

print(encrypt("test","as"))
print(decrypt("uxtm","as"))
