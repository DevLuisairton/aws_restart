# Criando uma lista mista
# Defina uma lista com diferentes tipos:
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Use uma instrução de loop for para percorrer a lista e imprimir o tipo de dados para cada item
# Use um loop for para iterar cada item da lista myMixedTypeList
for item in myMixedTypeList:
    # Imprima cada item e seu tipo de dados
    # {} espaços reservados são substituídos pelo item e seu tipo
    # .format(item, type(item)) método insere item e seu tipo nos espaços reservados
    print("{} is of the data type {}".format(item, type(item)))

# Defina uma lista chamada myMixedTypeList contendo elementos de diferentes tipos de dados
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]