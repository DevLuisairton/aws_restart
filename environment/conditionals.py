# Edite o script Python para enviar pacotes
# Trabalhando com a instrução else
# Pergunte ao usuário se ele precisa enviar um pacote
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Verifica se o usuário respondeu com 'sim'
if userReply == "yes":
   # Se sim, imprima uma mensagem indicando ajuda para enviar o pacote
    print("We can help you ship that package!")
else:
   # Se não, imprima uma mensagem indicando para voltar quando precisar enviar um pacote
    print("Please come back when you need to ship a package. Thank you.")

# Trabalhando com a instrução elif
# Pergunte ao usuário se ele gostaria de comprar selos, comprar um envelope ou fazer uma cópia
userReply = input(
    "Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) "
)

# Verifique se o usuário deseja comprar selos
if userReply == "stamps":
    # Se sim, imprima uma mensagem indicando a disponibilidade de vários designs de carimbo
    print("We have many stamp designs to choose from.")
# Verifique se o usuário deseja comprar um envelope
elif userReply == "envelope":
    # Se sim, imprima uma mensagem indicando a disponibilidade de vários tamanhos de envelope
    print("We have many envelope sizes to choose from.")
# Verifique se o usuário deseja fazer uma cópia
elif userReply == "copy":
   # Se sim, pergunte quantas cópias eles gostariam
    copies = input("How many copies would you like? (Enter a number) ")
   # Imprima o número de cópias solicitadas
    print("Here are {} copies.".format(copies))
else:
   # Se nenhuma das condições acima for atendida, imprima uma mensagem de agradecimento
    print("Thank you, please come again.")