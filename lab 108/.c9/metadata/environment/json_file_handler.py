{"filter":false,"title":"json_file_handler.py","tooltip":"/json_file_handler.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":19,"column":46},"action":"insert","lines":["# Import the JSON module to work with JSON data","import json","","","# Define a function to read a JSON file and return its content","def read_json_file(file_name):","    data = \"\"  # Initialize an empty string to store the data","    try:","        # Open the JSON file for reading with utf-8 encoding","        with open(file_name, \"r\", encoding=\"utf-8\") as json_file:","            # Load and parse the JSON content","            data = json.load(json_file)","            print(\"File read successfully.\")","    except IOError:","        # Print an error message if the file cannot be read","        print(f\"Could not read file: {file_name}\")","    except json.JSONDecodeError:","        # Print an error message if the file is not valid JSON","        print(f\"Error decoding JSON from file: {file_name}\")","    return data  # Return the parsed JSON data"],"id":1}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":47},"action":"remove","lines":["Import the JSON module to work with JSON data"],"id":2},{"start":{"row":0,"column":2},"end":{"row":0,"column":53},"action":"insert","lines":["Importe o módulo JSON para trabalhar com dados JSON"]}],[{"start":{"row":4,"column":2},"end":{"row":4,"column":62},"action":"remove","lines":["Define a function to read a JSON file and return its content"],"id":3},{"start":{"row":4,"column":2},"end":{"row":4,"column":68},"action":"insert","lines":["Defina uma função para ler um arquivo JSON e retornar seu conteúdo"]}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":61},"action":"remove","lines":[" Initialize an empty string to store the data"],"id":4},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["#"]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":60},"action":"remove","lines":["Open the JSON file for reading with utf-8 encoding"],"id":5},{"start":{"row":8,"column":10},"end":{"row":8,"column":64},"action":"insert","lines":["Abra o arquivo JSON para leitura com codificação utf-8"]}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":45},"action":"remove","lines":["# Load and parse the JSON content"],"id":6},{"start":{"row":10,"column":8},"end":{"row":10,"column":12},"action":"remove","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":9,"column":65},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":59},"action":"remove","lines":["# Print an error message if the file cannot be read"],"id":7},{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":19},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":62},"action":"remove","lines":["# Print an error message if the file is not valid JSON"],"id":8},{"start":{"row":15,"column":8},"end":{"row":15,"column":71},"action":"insert","lines":["# Imprime uma mensagem de erro se o arquivo não for JSON válido"]}],[{"start":{"row":17,"column":17},"end":{"row":17,"column":46},"action":"remove","lines":["# Return the parsed JSON data"],"id":9},{"start":{"row":17,"column":17},"end":{"row":17,"column":51},"action":"insert","lines":["# Retorna os dados JSON analisados"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":51},"end":{"row":17,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"timestamp":1735257651766,"hash":"31675ae762f7e1ee91a5d74c29910437c04c1f0d"}