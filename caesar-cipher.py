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

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

key = getCipherKey()
print(f"You entered key: {key}")

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter  
    return encryptedMessage

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
doubleAlphabet = getDoubleAlphabet(alphabet)
print(encryptMessage("HELLO", 3, doubleAlphabet)) 
