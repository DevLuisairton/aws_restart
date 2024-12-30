# Laboratório de módulo: Bug nº 2 do programa Caesar Cipher
#
# Em um laboratório anterior, você criou um programa de cifra de César. Esta versão de
# o programa está com bugs. Use um depurador para encontrar o bug e corrigi-lo.


# Duplique o alfabeto fornecido
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


# Receba uma mensagem para criptografar
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


# Obtenha uma chave de cifra
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount


#Criptografar mensagem
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


#Descriptografar mensagem
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


# Lógica principal do programa
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"Alphabet: {myAlphabet}")
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f"Alphabet2: {myAlphabet2}")
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f"Encrypted Message: {myEncryptedMessage}")
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f"Decrypted Message: {myDecryptedMessage}")

runCaesarCipherProgram()