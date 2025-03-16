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

# Reverse the shift to decrypt the message

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)  
    return encryptMessage(message, decryptKey, alphabet)

encrypted = encryptMessage("HELLO", 3, doubleAlphabet)
print(f"Encrypted: {encrypted}")
decrypted = decryptMessage(encrypted, 3, doubleAlphabet)
print(f"Decrypted: {decrypted}")  

#Creating a main function

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(f'Original Message: {myMessage}')
    
    myCipherKey = getCipherKey()
    print(f'Cipher Key: {myCipherKey}')
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

    runCaesarCipherProgram()