{"changed":true,"filter":false,"title":"debug-caesar-1.py","tooltip":"/debug-caesar-1.py","value":"# Laboratório de módulo: Bug nº 1 do programa Caesar Cipher\n# Em um laboratório anterior, você criou um programa de cifra de César. Esta versão de\n# o programa está com bugs. Use um depurador para encontrar o bug e corrigi-lo.\n\n\n# Duplique o alfabeto fornecido\ndef getDoubleAlphabet(alphabet):\n    doubleAlphabet = alphabet + alphabet\n    return doubleAlphabet\n\n\n# Receba uma mensagem para criptografar\ndef getMessage():\n    stringToEncrypt = input(\"Please enter a message to encrypt: \")\n    return stringToEncrypt\n\n\n# Obtenha uma chave de cifra\ndef getCipherKey():\n    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")\n    return int(shiftAmount)  \n\n\n#Criptografar mensagem\ndef encryptMessage(message, cipherKey, alphabet):\n    encryptedMessage = \"\"\n    uppercaseMessage = message.upper()\n    for currentCharacter in uppercaseMessage:\n        position = alphabet.find(currentCharacter)\n        newPosition = position + cipherKey\n        if currentCharacter in alphabet:\n            encryptedMessage = encryptedMessage + alphabet[newPosition]\n        else:\n            encryptedMessage = encryptedMessage + currentCharacter\n    return encryptedMessage\n\n\n# Explicação do erro:O TypeError ocorre porque cipherKey é uma string retornada de getCipherKey, mas as operações aritméticas esperam um número inteiro.\n# Correção: Converta cipherKey em um número inteiro dentro da função encryptMessage.\n\n\n#Descriptografar mensagem\ndef decryptMessage(message, cipherKey, alphabet):\n    decryptKey = -1 * cipherKey \n    return encryptMessage(message, decryptKey, alphabet)\n\n\n# Lógica principal do programa\ndef runCaesarCipherProgram():\n    myAlphabet = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n    print(f\"Alphabet: {myAlphabet}\")\n    myAlphabet2 = getDoubleAlphabet(myAlphabet)\n    print(f\"Alphabet2: {myAlphabet2}\")\n    myMessage = getMessage()\n    print(myMessage)\n    myCipherKey = getCipherKey()\n    print(myCipherKey)\n    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)\n    print(f\"Encrypted Message: {myEncryptedMessage}\")\n    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)\n    print(f\"Decrypted Message: {myDecryptedMessage}\")\n\nrunCaesarCipherProgram()","undoManager":{"mark":11,"position":12,"stack":[[{"start":{"row":0,"column":0},"end":{"row":65,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return int(shiftAmount)  # Convert the input to an integer immediately","","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + cipherKey","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","","# Error Explanation:The TypeError occurs because cipherKey is a string returned from getCipherKey, but arithmetic operations expect an integer.","# Fix:Convert cipherKey to an integer inside the encryptMessage function.","","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * cipherKey  # cipherKey is already an integer now","    return encryptMessage(message, decryptKey, alphabet)","","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f\"Alphabet: {myAlphabet}\")","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f\"Alphabet2: {myAlphabet2}\")","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f\"Encrypted Message: {myEncryptedMessage}\")","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f\"Decrypted Message: {myDecryptedMessage}\")","","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":66},"action":"remove","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it."],"id":2},{"start":{"row":0,"column":0},"end":{"row":3,"column":79},"action":"insert","lines":["# Laboratório de módulo: Bug nº 1 do programa Caesar Cipher","#","# Em um laboratório anterior, você criou um programa de cifra de César. Esta versão de","# o programa está com bugs. Use um depurador para encontrar o bug e corrigi-lo."]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":27},"action":"remove","lines":["# Double the given alphabet"],"id":3},{"start":{"row":6,"column":0},"end":{"row":6,"column":31},"action":"insert","lines":["# Duplique o alfabeto fornecido"]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":26},"action":"remove","lines":["# Get a message to encrypt"],"id":4},{"start":{"row":12,"column":0},"end":{"row":12,"column":39},"action":"insert","lines":["# Receba uma mensagem para criptografar"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":18},"action":"remove","lines":["# Get a cipher key"],"id":5},{"start":{"row":18,"column":0},"end":{"row":18,"column":28},"action":"insert","lines":["# Obtenha uma chave de cifra"]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":17},"action":"remove","lines":["# Encrypt message"],"id":6},{"start":{"row":24,"column":0},"end":{"row":24,"column":22},"action":"insert","lines":["#Criptografar mensagem"]}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":73},"action":"remove","lines":["# Error Explanation:The TypeError occurs because cipherKey is a string returned from getCipherKey, but arithmetic operations expect an integer.","# Fix:Convert cipherKey to an integer inside the encryptMessage function."],"id":7},{"start":{"row":38,"column":0},"end":{"row":39,"column":84},"action":"insert","lines":["# Explicação do erro:O TypeError ocorre porque cipherKey é uma string retornada de getCipherKey, mas as operações aritméticas esperam um número inteiro.","# Correção: Converta cipherKey em um número inteiro dentro da função encryptMessage."]}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":17},"action":"remove","lines":["# Decrypt message"],"id":8},{"start":{"row":42,"column":0},"end":{"row":42,"column":25},"action":"insert","lines":["#Descriptografar mensagem"]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":20},"action":"remove","lines":["# Main program logic"],"id":9},{"start":{"row":48,"column":0},"end":{"row":48,"column":30},"action":"insert","lines":["# Lógica principal do programa"]}],[{"start":{"row":64,"column":0},"end":{"row":64,"column":12},"action":"remove","lines":["# Main logic"],"id":10},{"start":{"row":63,"column":0},"end":{"row":64,"column":0},"action":"remove","lines":["",""]},{"start":{"row":62,"column":0},"end":{"row":63,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":44,"column":36},"end":{"row":44,"column":70},"action":"remove","lines":["ipherKey is already an integer now"],"id":11},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"remove","lines":["c"]},{"start":{"row":44,"column":34},"end":{"row":44,"column":35},"action":"remove","lines":[" "]},{"start":{"row":44,"column":33},"end":{"row":44,"column":34},"action":"remove","lines":["#"]},{"start":{"row":44,"column":32},"end":{"row":44,"column":33},"action":"remove","lines":[" "]}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":74},"action":"remove","lines":["# Convert the input to an integer immediately"],"id":12}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["#"],"id":13},{"start":{"row":0,"column":59},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":59},"end":{"row":0,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1735258101555}