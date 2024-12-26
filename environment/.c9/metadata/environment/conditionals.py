{"filter":false,"title":"conditionals.py","tooltip":"/conditionals.py","undoManager":{"mark":82,"position":82,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["userReply = input(\"Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) \")","if userReply == \"stamps\":","    print(\"We have many stamp designs to choose from.\")","elif userReply == \"envelope\":","    print(\"We have many envelope sizes to choose from.\")","elif userReply == \"copy\":","    copies = input(\"How many copies would you like? (Enter a number) \")","    print(\"Here are {} copies.\".format(copies))","else:","    print(\"Thank you, please come again.\")",""],"id":34}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["print(\"Welcome to Guess the Number!\")","print(\"The rules are simple. I will think of a number, and you will try to guess it.\")",""],"id":36}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["import random",""],"id":38}],[{"start":{"row":0,"column":13},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":39}],[{"start":{"row":6,"column":56},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":33},"action":"insert","lines":["number = random.randint(1,10)"],"id":41}],[{"start":{"row":7,"column":33},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":24},"action":"insert","lines":["isGuessRight = False"],"id":43}],[{"start":{"row":8,"column":24},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":45},{"start":{"row":8,"column":24},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["while isGuessRight != True:","    guess = input(\"Guess a number between 1 and 10: \")","    if int(guess) == number:","        print(\"You guessed {}. That is correct! You win!\".format(guess))","        isGuessRight = True","    else:","        print(\"You guessed {}. Sorry, that isn’t it. Try again.\".format(guess))",""],"id":46}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":47}],[{"start":{"row":15,"column":0},"end":{"row":21,"column":79},"action":"remove","lines":["while isGuessRight != True:","    guess = input(\"Guess a number between 1 and 10: \")","    if int(guess) == number:","        print(\"You guessed {}. That is correct! You win!\".format(guess))","        isGuessRight = True","    else:","        print(\"You guessed {}. Sorry, that isn’t it. Try again.\".format(guess))"],"id":48}],[{"start":{"row":8,"column":24},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":50},{"start":{"row":8,"column":24},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":42},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":21,"column":79},"action":"insert","lines":["while isGuessRight != True:","    guess = input(\"Guess a number between 1 and 10: \")","    if int(guess) == number:","        print(\"You guessed {}. That is correct! You win!\".format(guess))","        isGuessRight = True","    else:","        print(\"You guessed {}. Sorry, that isn’t it. Try again.\".format(guess))"],"id":52}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":53}],[{"start":{"row":15,"column":0},"end":{"row":21,"column":79},"action":"remove","lines":["while isGuessRight != True:","    guess = input(\"Guess a number between 1 and 10: \")","    if int(guess) == number:","        print(\"You guessed {}. That is correct! You win!\".format(guess))","        isGuessRight = True","    else:","        print(\"You guessed {}. Sorry, that isn’t it. Try again.\".format(guess))"],"id":54}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":55},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":42},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":56}],[{"start":{"row":0,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["import random","","userReply = input(\"Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) \")","if userReply == \"stamps\":","    print(\"We have many stamp designs to choose from.\")","elif userReply == \"envelope\":","    print(\"We have many envelope sizes to choose from.\")","    number = random.randint(1,10)","    isGuessRight = False","elif userReply == \"copy\":","    copies = input(\"How many copies would you like? (Enter a number) \")","    print(\"Here are {} copies.\".format(copies))","else:","    print(\"Thank you, please come again.\")","","","","print(\"Welcome to Guess the Number!\")","print(\"The rules are simple. I will think of a number, and you will try to guess it.\")",""],"id":58},{"start":{"row":0,"column":0},"end":{"row":73,"column":52},"action":"insert","lines":["# Importing Modules","import csv  # Importing the csv module to work with CSV files","import copy  # Importing the copy module to create deep copies of objects","","# Defining the Dictionary","myVehicle = {","    \"vin\": \"<empty>\",  # Vehicle Identification Number, initially empty","    \"make\": \"<empty>\",  # Manufacturer of the vehicle, initially empty","    \"model\": \"<empty>\",  # Model of the vehicle, initially empty","    \"year\": 0,  # Year of manufacture, initially 0","    \"range\": 0,  # Range of the vehicle, initially 0","    \"topSpeed\": 0,  # Top speed of the vehicle, initially 0","    \"zeroSixty\": 0.0,  # Time to accelerate from 0 to 60 mph, initially 0.0","    \"mileage\": 0,  # Mileage of the vehicle, initially 0","}","","# Iterating Over the Dictionary","for key, value in myVehicle.items():","    print(\"{} : {}\".format(key, value))","","# Defining the List for Car Inventory","myInventoryList = []  # Creating an empty list to hold the inventory of vehicles","","# Reading and Copying Data from the CSV File","with open(\"car_fleet.csv\") as csvFile:  # Open the CSV file for reading","    csvReader = csv.reader(","        csvFile, delimiter=\",\"","    )  # Create a CSV reader object to read the file","    lineCount = 0  # Initialize a line counter","","    for row in csvReader:  # Iterate over each row in the CSV file","        if lineCount == 0:  # Check if it is the first row (header)","            print(f'Column names are: {\", \".join(row)}')  # Print the column names","            lineCount += 1  # Increment the line counter","        else:","            # Print each field in the row with its corresponding value","            print(","                f\"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}\"","            )","","            currentVehicle = copy.deepcopy(","                myVehicle","            )  # Create a deep copy of the myVehicle dictionary","","            # Assign values from the CSV row to the corresponding keys in the dictionary","            currentVehicle[\"vin\"] = row[0]","            currentVehicle[\"make\"] = row[1]","            currentVehicle[\"model\"] = row[2]","            currentVehicle[\"year\"] = row[3]","            currentVehicle[\"range\"] = row[4]","            currentVehicle[\"topSpeed\"] = row[5]","            currentVehicle[\"zeroSixty\"] = row[6]","            currentVehicle[\"mileage\"] = row[7]","","            myInventoryList.append(","                currentVehicle","            )  # Add the populated dictionary to the inventory list","","            lineCount += 1  # Increment the line counter","","    print(f\"Processed {lineCount} lines.\")  # Print the total number of lines processed","","# Printing the Car Inventory","for myCarProperties in myInventoryList:  # Iterate over each car in the inventory list","    for (","        key,","        value,","    ) in (","        myCarProperties.items()","    ):  # Iterate over each key-value pair in the car dictionary","        print(","            \"{} : {}\".format(key, value)","        )  # Print each key and its corresponding value","    print(\"-----\")  # Print a separator between cars"]}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":19},"action":"remove","lines":["Importing Modules"],"id":59},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["i"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["M"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["P"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["O"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["R"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["T"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["A"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["R"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"remove","lines":[" "],"id":61},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"remove","lines":["R"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":["A"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["T"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"remove","lines":["R"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["O"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["P"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["M"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["i"]}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["I"],"id":62},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["p"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["o"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["r"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["a"],"id":63},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[" "],"id":64},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["b"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["i"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["b"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["l"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["i"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["t"],"id":65},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["e"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["c"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["a"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":73},"action":"remove","lines":["mporting the copy module to create deep copies of objects"],"id":66},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["I"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":[" "]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["#"]}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":61},"action":"remove","lines":["# Importing the csv module to work with CSV files"],"id":67}],[{"start":{"row":4,"column":2},"end":{"row":4,"column":25},"action":"remove","lines":["Defining the Dictionary"],"id":68},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["D"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["e"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["f"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["i"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["n"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["i"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["n"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["d"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["f"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["o"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":["o"],"id":69},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["f"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"remove","lines":["d"]}],[{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["d"],"id":70},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["o"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":[" "]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["d"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["i"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["r"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["e"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["t"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["o"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["r"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["i"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":71},"action":"remove","lines":["# Vehicle Identification Number, initially empty"],"id":71},{"start":{"row":6,"column":23},"end":{"row":6,"column":79},"action":"insert","lines":["# Número de Identificação do Veículo, inicialmente vazio"]}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":70},"action":"remove","lines":["# Manufacturer of the vehicle, initially empty"],"id":72},{"start":{"row":7,"column":24},"end":{"row":7,"column":67},"action":"insert","lines":["# Fabricante do veículo, inicialmente vazio"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":64},"action":"remove","lines":["# Model of the vehicle, initially empty"],"id":73},{"start":{"row":8,"column":25},"end":{"row":8,"column":64},"action":"insert","lines":["# Modelo do veículo, inicialmente vazio"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":50},"action":"remove","lines":["# Year of manufacture, initially 0"],"id":74},{"start":{"row":9,"column":16},"end":{"row":9,"column":51},"action":"insert","lines":["# Ano de fabricação, inicialmente 0"]}],[{"start":{"row":10,"column":17},"end":{"row":10,"column":52},"action":"remove","lines":["# Range of the vehicle, initially 0"],"id":75},{"start":{"row":10,"column":17},"end":{"row":10,"column":53},"action":"insert","lines":["# Alcance do veículo, inicialmente 0"]}],[{"start":{"row":11,"column":20},"end":{"row":11,"column":59},"action":"remove","lines":["# Top speed of the vehicle, initially 0"],"id":76},{"start":{"row":11,"column":20},"end":{"row":11,"column":66},"action":"insert","lines":["# Velocidade máxima do veículo, inicialmente 0"]}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":75},"action":"remove","lines":["# Time to accelerate from 0 to 60 mph, initially 0.0"],"id":77},{"start":{"row":12,"column":23},"end":{"row":12,"column":74},"action":"insert","lines":["# Tempo para acelerar de 0 a 60 mph, inicialmente 0"]}],[{"start":{"row":12,"column":74},"end":{"row":12,"column":75},"action":"insert","lines":["."],"id":78},{"start":{"row":12,"column":75},"end":{"row":12,"column":76},"action":"insert","lines":["0"]}],[{"start":{"row":13,"column":19},"end":{"row":13,"column":56},"action":"remove","lines":["# Mileage of the vehicle, initially 0"],"id":79},{"start":{"row":13,"column":19},"end":{"row":13,"column":61},"action":"insert","lines":["# Quilometragem do veículo, inicialmente 0"]}],[{"start":{"row":16,"column":2},"end":{"row":16,"column":31},"action":"remove","lines":["Iterating Over the Dictionary"],"id":80},{"start":{"row":16,"column":2},"end":{"row":16,"column":24},"action":"insert","lines":["Iterando no Dicionário"]}],[{"start":{"row":20,"column":2},"end":{"row":20,"column":37},"action":"remove","lines":["Defining the List for Car Inventory"],"id":81},{"start":{"row":20,"column":2},"end":{"row":20,"column":45},"action":"insert","lines":["Definindo a lista para inventário de carros"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":80},"action":"remove","lines":["# Creating an empty list to hold the inventory of vehicles"],"id":82}],[{"start":{"row":23,"column":2},"end":{"row":23,"column":44},"action":"remove","lines":["Reading and Copying Data from the CSV File"],"id":83},{"start":{"row":23,"column":2},"end":{"row":23,"column":39},"action":"insert","lines":["Lendo e copiando dados do arquivo CSV"]}],[{"start":{"row":24,"column":40},"end":{"row":24,"column":71},"action":"remove","lines":["# Open the CSV file for reading"],"id":84}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":52},"action":"remove","lines":[" # Create a CSV reader object to read the file"],"id":85}],[{"start":{"row":28,"column":18},"end":{"row":28,"column":46},"action":"remove","lines":[" # Initialize a line counter"],"id":86}],[{"start":{"row":30,"column":27},"end":{"row":30,"column":66},"action":"remove","lines":["# Iterate over each row in the CSV file"],"id":87}],[{"start":{"row":31,"column":29},"end":{"row":31,"column":67},"action":"remove","lines":[" Check if it is the first row (header)"],"id":88},{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"remove","lines":["#"]}],[{"start":{"row":32,"column":57},"end":{"row":32,"column":82},"action":"remove","lines":[" # Print the column names"],"id":89}],[{"start":{"row":33,"column":28},"end":{"row":33,"column":56},"action":"remove","lines":["# Increment the line counter"],"id":90}],[{"start":{"row":35,"column":14},"end":{"row":35,"column":70},"action":"remove","lines":["Print each field in the row with its corresponding value"],"id":91},{"start":{"row":35,"column":14},"end":{"row":35,"column":70},"action":"insert","lines":["Imprima cada campo da linha com seu valor correspondente"]}],[{"start":{"row":42,"column":15},"end":{"row":42,"column":63},"action":"remove","lines":["# Create a deep copy of the myVehicle dictionary"],"id":92},{"start":{"row":42,"column":15},"end":{"row":42,"column":65},"action":"insert","lines":["# Crie uma cópia detalhada do dicionário myVehicle"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":88},"action":"remove","lines":["Assign values from the CSV row to the corresponding keys in the dictionary"],"id":93},{"start":{"row":44,"column":14},"end":{"row":44,"column":82},"action":"insert","lines":["Atribua valores da linha CSV às chaves correspondentes no dicionário"]}],[{"start":{"row":56,"column":17},"end":{"row":56,"column":67},"action":"remove","lines":["Add the populated dictionary to the inventory list"],"id":94},{"start":{"row":56,"column":17},"end":{"row":56,"column":71},"action":"insert","lines":["Adicione o dicionário preenchido à lista de inventário"]}],[{"start":{"row":58,"column":30},"end":{"row":58,"column":56},"action":"remove","lines":["Increment the line counter"],"id":95},{"start":{"row":58,"column":29},"end":{"row":58,"column":30},"action":"remove","lines":[" "]},{"start":{"row":58,"column":28},"end":{"row":58,"column":29},"action":"remove","lines":["#"]}],[{"start":{"row":60,"column":44},"end":{"row":60,"column":87},"action":"remove","lines":["# Print the total number of lines processed"],"id":96}],[{"start":{"row":62,"column":2},"end":{"row":62,"column":28},"action":"remove","lines":["Printing the Car Inventory"],"id":97},{"start":{"row":62,"column":2},"end":{"row":62,"column":35},"action":"insert","lines":["Imprimindo o Inventário de Carros"]}],[{"start":{"row":63,"column":42},"end":{"row":63,"column":86},"action":"remove","lines":[" Iterate over each car in the inventory list"],"id":98},{"start":{"row":63,"column":41},"end":{"row":63,"column":42},"action":"remove","lines":["#"]}],[{"start":{"row":69,"column":10},"end":{"row":69,"column":64},"action":"remove","lines":["Iterate over each key-value pair in the car dictionary"],"id":99},{"start":{"row":69,"column":10},"end":{"row":69,"column":71},"action":"insert","lines":["Iterar sobre cada par de valores-chave no dicionário do carro"]}],[{"start":{"row":72,"column":13},"end":{"row":72,"column":55},"action":"remove","lines":["Print each key and its corresponding value"],"id":100},{"start":{"row":72,"column":13},"end":{"row":72,"column":58},"action":"insert","lines":["Imprima cada chave e seu valor correspondente"]}],[{"start":{"row":73,"column":27},"end":{"row":73,"column":52},"action":"remove","lines":[" a separator between cars"],"id":101},{"start":{"row":73,"column":27},"end":{"row":73,"column":52},"action":"insert","lines":["um separador entre carros"]}],[{"start":{"row":73,"column":27},"end":{"row":73,"column":28},"action":"insert","lines":[" "],"id":102}],[{"start":{"row":73,"column":22},"end":{"row":73,"column":53},"action":"remove","lines":["Print um separador entre carros"],"id":103},{"start":{"row":73,"column":22},"end":{"row":73,"column":56},"action":"insert","lines":["Imprimir um separador entre carros"]}],[{"start":{"row":0,"column":0},"end":{"row":73,"column":56},"action":"remove","lines":["# Importar bibliotecas","import csv  ","import copy  ","","# Definindo diretorio","myVehicle = {","    \"vin\": \"<empty>\",  # Número de Identificação do Veículo, inicialmente vazio","    \"make\": \"<empty>\",  # Fabricante do veículo, inicialmente vazio","    \"model\": \"<empty>\",  # Modelo do veículo, inicialmente vazio","    \"year\": 0,  # Ano de fabricação, inicialmente 0","    \"range\": 0,  # Alcance do veículo, inicialmente 0","    \"topSpeed\": 0,  # Velocidade máxima do veículo, inicialmente 0","    \"zeroSixty\": 0.0,  # Tempo para acelerar de 0 a 60 mph, inicialmente 0.0","    \"mileage\": 0,  # Quilometragem do veículo, inicialmente 0","}","","# Iterando no Dicionário","for key, value in myVehicle.items():","    print(\"{} : {}\".format(key, value))","","# Definindo a lista para inventário de carros","myInventoryList = []  ","","# Lendo e copiando dados do arquivo CSV","with open(\"car_fleet.csv\") as csvFile:  ","    csvReader = csv.reader(","        csvFile, delimiter=\",\"","    ) ","    lineCount = 0 ","","    for row in csvReader:  ","        if lineCount == 0:  ","            print(f'Column names are: {\", \".join(row)}') ","            lineCount += 1  ","        else:","            # Imprima cada campo da linha com seu valor correspondente","            print(","                f\"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}\"","            )","","            currentVehicle = copy.deepcopy(","                myVehicle","            )  # Crie uma cópia detalhada do dicionário myVehicle","","            # Atribua valores da linha CSV às chaves correspondentes no dicionário","            currentVehicle[\"vin\"] = row[0]","            currentVehicle[\"make\"] = row[1]","            currentVehicle[\"model\"] = row[2]","            currentVehicle[\"year\"] = row[3]","            currentVehicle[\"range\"] = row[4]","            currentVehicle[\"topSpeed\"] = row[5]","            currentVehicle[\"zeroSixty\"] = row[6]","            currentVehicle[\"mileage\"] = row[7]","","            myInventoryList.append(","                currentVehicle","            )  # Adicione o dicionário preenchido à lista de inventário","","            lineCount += 1  ","","    print(f\"Processed {lineCount} lines.\")  ","","# Imprimindo o Inventário de Carros","for myCarProperties in myInventoryList:  ","    for (","        key,","        value,","    ) in (","        myCarProperties.items()","    ):  # Iterar sobre cada par de valores-chave no dicionário do carro","        print(","            \"{} : {}\".format(key, value)","        )  # Imprima cada chave e seu valor correspondente","    print(\"-----\")  # Imprimir um separador entre carros"],"id":104},{"start":{"row":0,"column":0},"end":{"row":35,"column":42},"action":"insert","lines":["# Edit the Python Script to Ship Packages","# Working with the else Statement","# Ask the user if they need to ship a package","userReply = input(\"Do you need to ship a package? (Enter yes or no) \")","","# Check if the user replied with 'yes'","if userReply == \"yes\":","    # If yes, print a message indicating help to ship the package","    print(\"We can help you ship that package!\")","else:","    # If no, print a message indicating to come back when they need to ship a package","    print(\"Please come back when you need to ship a package. Thank you.\")","","# Working with the elif Statement","# Ask the user if they would like to buy stamps, buy an envelope, or make a copy","userReply = input(","    \"Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) \"",")","","# Check if the user wants to buy stamps","if userReply == \"stamps\":","    # If yes, print a message indicating the availability of many stamp designs","    print(\"We have many stamp designs to choose from.\")","# Check if the user wants to buy an envelope","elif userReply == \"envelope\":","    # If yes, print a message indicating the availability of many envelope sizes","    print(\"We have many envelope sizes to choose from.\")","# Check if the user wants to make a copy","elif userReply == \"copy\":","    # If yes, ask how many copies they would like","    copies = input(\"How many copies would you like? (Enter a number) \")","    # Print the number of copies requested","    print(\"Here are {} copies.\".format(copies))","else:","    # If none of the above conditions are met, print a thank you message","    print(\"Thank you, please come again.\")"]}],[{"start":{"row":0,"column":0},"end":{"row":2,"column":45},"action":"remove","lines":["# Edit the Python Script to Ship Packages","# Working with the else Statement","# Ask the user if they need to ship a package"],"id":105},{"start":{"row":0,"column":0},"end":{"row":2,"column":53},"action":"insert","lines":["# Edite o script Python para enviar pacotes","# Trabalhando com a instrução else","# Pergunte ao usuário se ele precisa enviar um pacote"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":38},"action":"remove","lines":["# Check if the user replied with 'yes'"],"id":106},{"start":{"row":5,"column":0},"end":{"row":5,"column":43},"action":"insert","lines":["# Verifica se o usuário respondeu com 'sim'"]}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":65},"action":"remove","lines":[" # If yes, print a message indicating help to ship the package"],"id":107},{"start":{"row":7,"column":3},"end":{"row":7,"column":70},"action":"insert","lines":["# Se sim, imprima uma mensagem indicando ajuda para enviar o pacote"]}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":85},"action":"remove","lines":[" # If no, print a message indicating to come back when they need to ship a package"],"id":108},{"start":{"row":10,"column":3},"end":{"row":10,"column":88},"action":"insert","lines":["# Se não, imprima uma mensagem indicando para voltar quando precisar enviar um pacote"]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":80},"action":"remove","lines":["# Working with the elif Statement","# Ask the user if they would like to buy stamps, buy an envelope, or make a copy"],"id":109},{"start":{"row":13,"column":0},"end":{"row":14,"column":94},"action":"insert","lines":["# Trabalhando com a instrução elif","# Pergunte ao usuário se ele gostaria de comprar selos, comprar um envelope ou fazer uma cópia"]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":39},"action":"remove","lines":["# Check if the user wants to buy stamps"],"id":110},{"start":{"row":19,"column":0},"end":{"row":19,"column":45},"action":"insert","lines":["# Verifique se o usuário deseja comprar selos"]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":79},"action":"remove","lines":["# If yes, print a message indicating the availability of many stamp designs"],"id":111},{"start":{"row":21,"column":4},"end":{"row":21,"column":91},"action":"insert","lines":["# Se sim, imprima uma mensagem indicando a disponibilidade de vários designs de carimbo"]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":44},"action":"remove","lines":["# Check if the user wants to buy an envelope"],"id":112},{"start":{"row":23,"column":0},"end":{"row":23,"column":51},"action":"insert","lines":["# Verifique se o usuário deseja comprar um envelope"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":80},"action":"remove","lines":["# If yes, print a message indicating the availability of many envelope sizes"],"id":113},{"start":{"row":25,"column":4},"end":{"row":25,"column":93},"action":"insert","lines":["# Se sim, imprima uma mensagem indicando a disponibilidade de vários tamanhos de envelope"]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":40},"action":"remove","lines":["# Check if the user wants to make a copy"],"id":114},{"start":{"row":27,"column":0},"end":{"row":27,"column":47},"action":"insert","lines":["# Verifique se o usuário deseja fazer uma cópia"]}],[{"start":{"row":29,"column":3},"end":{"row":29,"column":49},"action":"remove","lines":[" # If yes, ask how many copies they would like"],"id":115},{"start":{"row":29,"column":3},"end":{"row":29,"column":51},"action":"insert","lines":["# Se sim, pergunte quantas cópias eles gostariam"]}],[{"start":{"row":31,"column":3},"end":{"row":31,"column":42},"action":"remove","lines":[" # Print the number of copies requested"],"id":116},{"start":{"row":31,"column":3},"end":{"row":31,"column":43},"action":"insert","lines":["# Imprima o número de cópias solicitadas"]}],[{"start":{"row":34,"column":3},"end":{"row":34,"column":72},"action":"remove","lines":[" # If none of the above conditions are met, print a thank you message"],"id":117},{"start":{"row":34,"column":3},"end":{"row":34,"column":87},"action":"insert","lines":["# Se nenhuma das condições acima for atendida, imprima uma mensagem de agradecimento"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":34,"column":87},"end":{"row":34,"column":87},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1735253759399,"hash":"b571b4fdc0724765c9b41bcf63f4ed0615b01663"}