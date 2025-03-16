def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

alphabet="ABC"

print(getDoubleAlphabet(alphabet))

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

message = getMessage()
print(f"You entered: {message}")