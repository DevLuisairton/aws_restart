# Assigning Variables, Lists, and Dictionaries
# Python3.6
# Coding: utf-8

# Armazene a sequência da pré-pró-insulina humana em uma variável chamada pré-pró-insulina:
# Esta sequência é a forma inicial da insulina antes de ser processada em sua forma ativa.
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
# These variables represent different parts of the insulin molecule.
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn" 
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

# Combine as cadeias B e A para obter a molécula completa de insulina.
insulin = bInsulin + aInsulin

# Crie um dicionário para armazenar os valores de pKa dos aminoácidos que contribuem para a carga líquida.
# Os valores de pKa indicam a força de um ácido; quanto menor o pKa, mais forte é o ácido.
pKR = {
    "y": 10.07,  
    "c": 8.18,  
    "k": 10.53,  
    "h": 6.00,
    "r": 12.48,  
    "d": 3.65,  
    "e": 4.25, 
}


# Usando count() para contar o número de cada aminoácido
# Use o método count() para contar o número de cada aminoácido na sequência da insulina.
# O método count() retorna o número de ocorrências de uma substring em uma string.

# Aqui, float() é usado para garantir que a contagem seja tratada como float para cálculos.
# Esta linha de código cria um dicionário que mapeia cada aminoácido para sua contagem na sequência da insulina.
seqCount = {x: float(insulin.count(x)) for x in ["y", "c", "k", "h", "r", "d", "e"]}
# A compreensão do dicionário percorre uma lista de aminoácidos e conta suas ocorrências na sequência da insulina.
# O dicionário resultante fica assim: {'y': count_of_y, 'c': count_of_c, ...}

# Escrevendo a fórmula da cobrança líquida
# Inicialize a variável pH para zero. A escala de pH normalmente varia de 0 a 14.
pH = 0

# Crie um loop while que funcionará enquanto o pH for menor ou igual a 14.
while pH <= 14:
    # Calcule a carga líquida da molécula de insulina no pH atual.
    # Esta fórmula soma as contribuições dos aminoácidos com carga positiva e negativa.
    netCharge = (
        +(
            sum(
                {
                    x: ((seqCount[x] * (10 ** pKR[x])) / ((10**pH) + (10 ** pKR[x])))
                    for x in ["k", "h", "r"]
                }.values()
            )
        )
        # Para aminoácidos com carga positiva (K, H, R), esta parte calcula suas contribuições para a carga líquida.
        - (
            sum(
                {
                    x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10 ** pKR[x])))
                    for x in ["y", "c", "d", "e"]
                }.values()
            )
        )
        # Para aminoácidos com carga negativa (Y, C, D, E), esta parte calcula suas contribuições para a carga líquida.
    )

    # Imprima o pH atual e a carga líquida calculada.
    # '{0:.2f}'.format(pH) formata o valor do pH com duas casas decimais para facilitar a leitura.
    print("{0:.2f}".format(pH), netCharge)
    pH += 1