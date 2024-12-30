#parte 1
# Esta linha de código atribui uma string à variável myString
myString = "This is a string."

# Esta linha de código imprime o valor de myString no console
print(myString)

#parte 2
# Esta linha de código imprime o tipo de myString, que é <class 'str'>
print(type(myString))

# Esta linha de código concatena strings e imprime o resultado
# Ele usa a função str() para converter as informações do tipo em uma string para concatenação
print(myString + " is of the data type " + str(type(myString)))

#parte 3
# Esta linha de código atribui a string "water" à variável firstString
firstString = "water"

# Esta linha de código atribui a string "fall" à variável secondString
secondString = "fall"

# Esta linha de código concatena firstString e secondString e atribui o resultado a thirdString
thirdString = firstString + secondString

# Esta linha de código imprime o valor de thirdString no console
print(thirdString)

#parte 4
# Esta linha de código solicita que o usuário insira seu nome e atribui a entrada ao nome da variável
name = input("What is your name? ")

# Esta linha de código imprime o valor de name no console
print(name)

#parte 5
# Esta linha de código solicita que o usuário insira sua cor favorita e atribui a entrada à variável color
color = input("What is your favorite color? ")

# Esta linha de código solicita ao usuário que insira seu animal favorito e atribui a entrada à variável animal
animal = input("What is your favorite animal? ")

# Esta linha de código formata e imprime uma string usando o nome, a cor e as variáveis do animal
# Os espaços reservados {} na string são substituídos pelos valores de nome, cor e animal nesta ordem
print("{}, you like a {} {}!".format(name, color, animal))