# Importe o módulo personalizado para lidar com arquivos JSON
try:
    import json_file_handler  
except ModuleNotFoundError:
    # Imprime uma mensagem de erro se o módulo não for encontrado e sai do programa
    print("Error: The 'json_file_handler' module is not found.")
    exit()

# Recupera os dados JSON do arquivo insulin.json
data = json_file_handler.read_json_file(
    "insulin.json"
)  

# Verifique se os dados foram recuperados com sucesso
if data:
    # Acessando sequências específicas de moléculas de insulina
    b_insulin = data["molecules"][
        "bInsulin"
    ]  
    a_insulin = data["molecules"][
        "aInsulin"
    ]  
   # Combine as sequências de insulina b e a
    insulin = b_insulin + a_insulin  

   # Acessando o peso molecular real da insulina
    molecular_weight_insulin_actual = data[
        "molecularWeightInsulinActual"
    ]  
    print("bInsulin: " + b_insulin)  
    print("aInsulin: " + a_insulin)  
    print(
        "molecularWeightInsulinActual: " + str(molecular_weight_insulin_actual)
    )  

    # Obtendo uma lista dos pesos de aminoácidos
    aa_weights = data["weights"]  # Recupera o dicionário de pesos de aminoácidos

    # Contando o número de cada aminoácido na sequência da insulina
    aa_count_insulin = {x: float(insulin.upper().count(x)) for x in aa_weights.keys()}
    # Crie um dicionário onde as chaves são aminoácidos e os valores são suas contagens na sequência da insulina

    # Cálculo do peso molecular total da insulina com base na contagem e peso de aminoácidos
    molecular_weight_insulin = sum(
        {x: (aa_count_insulin[x] * aa_weights[x]) for x in aa_weights.keys()}.values()
    )
    # Multiplique a contagem de cada aminoácido pelo seu peso e some os resultados para obter o peso molecular total

    # Imprimindo o peso molecular aproximado calculado da insulina e o erro percentual
    print(
        "The rough molecular weight of insulin: " + str(molecular_weight_insulin)
    )  
    print(
        "Percent error: "
        + str(
            (
                (molecular_weight_insulin - molecular_weight_insulin_actual)
                / molecular_weight_insulin_actual
            )
            * 100
        )
    )
   # Calcule o erro percentual entre os pesos moleculares reais e calculados e imprima-o
else:
    # Imprime uma mensagem de erro se a recuperação de dados falhar
    print("Error. Exiting program")  