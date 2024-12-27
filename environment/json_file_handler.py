# Importe o módulo JSON para trabalhar com dados JSON
import json


# Defina uma função para ler um arquivo JSON e retornar seu conteúdo
def read_json_file(file_name):
    data = ""  
    try:
        # Abra o arquivo JSON para leitura com codificação utf-8
        with open(file_name, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            print("File read successfully.")
    except IOError:
        print(f"Could not read file: {file_name}")
    except json.JSONDecodeError:
        # Imprime uma mensagem de erro se o arquivo não for JSON válido
        print(f"Error decoding JSON from file: {file_name}")
    return data  # Retorna os dados JSON analisados