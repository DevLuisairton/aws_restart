# Imprimindo as regras do jogo
print("Welcome to Guess the Number!")  #Exibe uma mensagem de boas-vindas
print(
    "The rules are simple. I will think of a number, and you will try to guess it."
)  # Explique as regras


# Importando aleatoriamente e escrevendo um loop while:
import random  # Importe o módulo aleatório para gerar números aleatórios

# Gere um número aleatório entre 1 e 10:
number = random.randint(1, 10) 

# Rastreie se o usuário adivinhou o número corretamente:
isGuessRight = False

# Criando o loop while:
while isGuessRight != True:  
    guess = input("Guess a number between 1 and 10: ")  
    if int(guess) == number: 
        print(
            "You guessed {}. That is correct! You win!".format(guess)
        )  
        isGuessRight = True  
    else:
        print(
            "You guessed {}. Sorry, that isn’t it. Try again.".format(guess)
        )  