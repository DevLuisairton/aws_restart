# Importing bibliotecas
import csv  # Importingo módulo csv para trabalhar com arquivos CSV
import copy  # Importando o módulo de cópia para criar cópias profundas de objetos

# Dados tabulares
myVehicle = {
    "vin": "<empty>",  
    "make": "<empty>", 
    "model": "<empty>",  
    "year": 0,  
    "range": 0,  
    "topSpeed": 0,  
    "zeroSixty": 0.0,  
    "mileage": 0,  
}

# Percorrer as chaves iniciais e valores do dicionário
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Defina uma lista vazia para armazenar o inventário de carros
myInventoryList = []  

# Lendo e copiando dados do arquivo CSV
with open("car_fleet.csv") as csvFile:  
    csvReader = csv.reader(
        csvFile, delimiter=","
    )  
    lineCount = 0  

    for row in csvReader: 
        if lineCount == 0:  
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:
            # Imprima cada campo da linha com seu valor correspondente
            print(
                f"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}"
            )

            currentVehicle = copy.deepcopy(
                myVehicle
            )  # Crie uma cópia detalhada do dicionário myVehicle

            # Atribui valores da linha CSV às chaves correspondentes no dicionário
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            myInventoryList.append(
                currentVehicle
            )  # Adiciona o dicionário preenchido à lista de inventário

            lineCount += 1  #Incrementa o contador de linha

    print(f"Processed {lineCount} lines.")  # Imprime o número total de linhas processadas

# Imprimindo o inventário do carro
for myCarProperties in myInventoryList:  # Iterar cada carro na lista de inventário
    for (
        key,
        value,
    ) in (
        myCarProperties.items()
    ):  # Iterar sobre cada par de valores-chave no dicionário do carro
        print(
            "{} : {}".format(key, value)
        )  # Imprime cada chave e seu valor correspondente
    print("-----")  # Imprime um separador entre carros