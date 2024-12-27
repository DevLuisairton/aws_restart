# Assigning Variables to the Sequence Elements of Human Insulin
# Python 3.6
# coding: utf-8
# Store the human preproinsulin sequence in a variable called preproInsulin
preproInsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr"
    "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)


# Armazene os elementos restantes da sequência da insulina humana
# Armazene os elementos restantes da sequência da insulina humana em variáveis
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Combine sequências de insulina
insulin = bInsulin + aInsulin

# Imprimindo a sequência de pré-pró-insulina humana para consolar usando comandos print() sucessivos
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Calculando o peso molecular da insulina
# Criando uma lista dos pesos de aminoácidos (AA)
# Crie um dicionário de pesos de aminoácidos
aaWeights = {
    "A": 89.09,
    "C": 121.16,
    "D": 133.10,
    "E": 147.13,
    "F": 165.19,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "K": 146.19,
    "L": 131.17,
    "M": 149.21,
    "N": 132.12,
    "P": 115.13,
    "Q": 146.15,
    "R": 174.20,
    "S": 105.09,
    "T": 119.12,
    "V": 117.15,
    "W": 204.23,
    "Y": 181.19,
}

# Conte o número de cada aminoácido na sequência de insulina
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}

# Calcule o peso molecular da insulina
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights.keys())
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Calcule a porcentagem de erro
molecularWeightInsulinActual = 5807.63
print(
    "Error percentage: "
    + str(
        (
            (molecularWeightInsulin - molecularWeightInsulinActual)
            / molecularWeightInsulinActual
        )
        * 100
    )
)