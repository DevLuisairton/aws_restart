{"changed":true,"filter":false,"title":"debug-caesar-3.py","tooltip":"/debug-caesar-3.py","value":"# Laboratório de módulo: Bug nº 3 do programa Caesar Cipher\n# Em um laboratório anterior, você criou um programa de cifra de César. Esta versão de\n# o programa está com bugs. Use um depurador para encontrar o bug e corrigi-lo.\n\n\n# Duplique o alfabeto fornecido\ndef getDoubleAlphabet(alphabet):\n    doubleAlphabet = alphabet + alphabet\n    return doubleAlphabet\n\n\n# Receba uma mensagem para criptografar\ndef getMessage():\n    stringToEncrypt = input(\"Please enter a message to encrypt: \")\n    return stringToEncrypt\n\n\n# Obtenha uma chave de cifra\ndef getCipherKey():\n    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")\n    return int(shiftAmount) \n\n\n# Criptografar mensagem\ndef encryptMessage(message, cipherKey, alphabet):\n    encryptedMessage = \"\"\n    uppercaseMessage = message.upper()  \n    for currentCharacter in uppercaseMessage:\n        position = alphabet.find(currentCharacter)\n        if position != -1:  \n            newPosition = (position + cipherKey) % len(\n                alphabet\n            )  \n            encryptedMessage = encryptedMessage + alphabet[newPosition]\n        else:\n            encryptedMessage = encryptedMessage + currentCharacter\n    return encryptedMessage\n\n\n# Descriptografar mensagem\ndef decryptMessage(message, cipherKey, alphabet):\n    decryptKey = -1 * cipherKey  \n    return encryptMessage(message, decryptKey, alphabet)\n\n\n# Lógica principal do programa\ndef runCaesarCipherProgram():\n    myAlphabet = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n    print(f\"Alphabet: {myAlphabet}\")\n    myAlphabet2 = getDoubleAlphabet(myAlphabet)\n    print(f\"Alphabet2: {myAlphabet2}\")\n    myMessage = getMessage()\n    print(myMessage)\n    myCipherKey = getCipherKey()\n    print(myCipherKey)\n    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)\n    print(f\"Encrypted Message: {myEncryptedMessage}\")\n    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)\n    print(f\"Decrypted Message: {myDecryptedMessage}\")\n\n\nrunCaesarCipherProgram()","undoManager":{"mark":16,"position":17,"stack":[[{"start":{"row":0,"column":0},"end":{"row":63,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return int(shiftAmount)  # Convert input to integer immediately","","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = message.upper()  # Convert message to uppercase","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        if position != -1:  # Check if the character is in the alphabet","            newPosition = (position + cipherKey) % len(","                alphabet","            )  # Wrap around using modulo","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * cipherKey  # cipherKey is already an integer now","    return encryptMessage(message, decryptKey, alphabet)","","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet = \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f\"Alphabet: {myAlphabet}\")","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f\"Alphabet2: {myAlphabet2}\")","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f\"Encrypted Message: {myEncryptedMessage}\")","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f\"Decrypted Message: {myDecryptedMessage}\")","","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":20},"action":"remove","lines":["# Main program logic"],"id":2},{"start":{"row":46,"column":0},"end":{"row":46,"column":30},"action":"insert","lines":["# Lógica principal do programa"]}],[{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"remove","lines":["c"],"id":3},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"remove","lines":["i"]},{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"remove","lines":["g"]},{"start":{"row":62,"column":8},"end":{"row":62,"column":9},"action":"remove","lines":["o"]},{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"remove","lines":["l"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"remove","lines":[" "]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"remove","lines":["n"]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"remove","lines":["i"]},{"start":{"row":62,"column":3},"end":{"row":62,"column":4},"action":"remove","lines":["a"]},{"start":{"row":62,"column":2},"end":{"row":62,"column":3},"action":"remove","lines":["M"]},{"start":{"row":62,"column":1},"end":{"row":62,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":62,"column":0},"end":{"row":62,"column":1},"action":"remove","lines":["#"],"id":4},{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":66},"action":"remove","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it."],"id":5},{"start":{"row":0,"column":0},"end":{"row":3,"column":79},"action":"insert","lines":["# Laboratório de módulo: Bug nº 3 do programa Caesar Cipher","#","# Em um laboratório anterior, você criou um programa de cifra de César. Esta versão de","# o programa está com bugs. Use um depurador para encontrar o bug e corrigi-lo."]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":27},"action":"remove","lines":["# Double the given alphabet"],"id":6},{"start":{"row":6,"column":0},"end":{"row":6,"column":31},"action":"insert","lines":["# Duplique o alfabeto fornecido"]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":26},"action":"remove","lines":["# Get a message to encrypt"],"id":7},{"start":{"row":12,"column":0},"end":{"row":12,"column":39},"action":"insert","lines":["# Receba uma mensagem para criptografar"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":18},"action":"remove","lines":["# Get a cipher key"],"id":8},{"start":{"row":18,"column":0},"end":{"row":18,"column":28},"action":"insert","lines":["# Obtenha uma chave de cifra"]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":17},"action":"remove","lines":["# Encrypt message"],"id":9},{"start":{"row":24,"column":0},"end":{"row":24,"column":22},"action":"insert","lines":["#Criptografar mensagem"]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":17},"action":"remove","lines":["# Decrypt message"],"id":10},{"start":{"row":40,"column":0},"end":{"row":40,"column":25},"action":"insert","lines":["#Descriptografar mensagem"]}],[{"start":{"row":40,"column":1},"end":{"row":40,"column":2},"action":"insert","lines":[" "],"id":11}],[{"start":{"row":24,"column":1},"end":{"row":24,"column":2},"action":"insert","lines":[" "],"id":12}],[{"start":{"row":42,"column":33},"end":{"row":42,"column":70},"action":"remove","lines":["# cipherKey is already an integer now"],"id":13}],[{"start":{"row":30,"column":28},"end":{"row":30,"column":71},"action":"remove","lines":["# Check if the character is in the alphabet"],"id":14}],[{"start":{"row":33,"column":15},"end":{"row":33,"column":41},"action":"remove","lines":["# Wrap around using modulo"],"id":15}],[{"start":{"row":27,"column":40},"end":{"row":27,"column":70},"action":"remove","lines":["# Convert message to uppercase"],"id":16}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":67},"action":"remove","lines":[" # Convert input to integer immediately"],"id":18}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["#"],"id":19},{"start":{"row":0,"column":59},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":59},"end":{"row":0,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1735257977691}