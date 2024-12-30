# Criando o Programa Principal
# Importe o módulo jsonFileHandler para acessar a função readJsonFile.
import json_File_Handler

# Recupere os dados JSON do arquivo insulin.json.
data = json_File_Handler.readJsonFile("files/insulin.json")

# Verifique se os dados foram recuperados com sucesso.
if data != "":
    bInsulin = data["molecules"]["bInsulin"]
    aInsulin = data["molecules"]["aInsulin"]
    insulin = bInsulin + aInsulin

    # Acessando o peso molecular real da insulina.
    molecularWeightInsulinActual = data["molecularWeightInsulinActual"]
    print("bInsulin: " + bInsulin)
    print("aInsulin: " + aInsulin)
    print("molecularWeightInsulinActual: " + str(molecularWeightInsulinActual))

    # Calculando o peso molecular da insulina.
    # Obtendo uma lista dos pesos dos aminoácidos.
    aaWeights = data["weights"]

    # Contando o número de cada aminoácido na sequência da insulina.
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}

    # Cálculo do peso molecular total da insulina com base na contagem e peso de aminoácidos.
    molecularWeightInsulin = sum(
        {x: (aaCountInsulin[x] * aaWeights[x]) for x in aaWeights.keys()}.values()
    )

    # Imprimindo o peso molecular aproximado calculado da insulina e o erro percentual.
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print(
        "Percent error: "
        + str(
            (
                (molecularWeightInsulin - molecularWeightInsulinActual)
                / molecularWeightInsulinActual
            )
            * 100
        )
    )
else:
    print("Error. Exiting program")