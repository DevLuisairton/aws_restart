{"filter":false,"title":"sys-admin.py","tooltip":"/sys-admin.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":0,"column":0},"end":{"row":59,"column":85},"action":"insert","lines":["# Importing the os Module","import os","","# Importing the subprocess Module","import subprocess","","# Importing platform to identify the OS","import platform","","# Determine the current operating system","current_os = platform.system()","","# Define the appropriate command for listing directory contents","if current_os == \"Windows\":","    list_dir_command = [\"cmd\", \"/c\", \"dir\"]","else:","    list_dir_command = [\"ls\"]","","# Running a directory listing command using os.system()","os.system(\" \".join(list_dir_command))","","# Running a directory listing command using subprocess.run()","subprocess.run(list_dir_command)","","# Using subprocess.run() with an additional argument for long listing format","if current_os == \"Windows\":","    list_dir_long_command = [\"cmd\", \"/c\", \"dir\"]","else:","    list_dir_long_command = [\"ls\", \"-l\"]","","subprocess.run(list_dir_long_command)","","# Using subprocess.run() with two additional arguments to list a specific file","file_name = \"README.md\"","if current_os == \"Windows\":","    list_file_command = [\"cmd\", \"/c\", \"dir\", file_name]","else:","    list_file_command = [\"ls\", \"-l\", file_name]","","subprocess.run(list_file_command)","","# Running uname -a or equivalent command","if current_os == \"Windows\":","    uname_command = [\"cmd\", \"/c\", \"ver\"]","else:","    uname_command = [\"uname\", \"-a\"]","","subprocess.run(uname_command)","","# Running ps -x or equivalent command","if current_os == \"Windows\":","    ps_command = [\"cmd\", \"/c\", \"tasklist\"]","else:","    ps_command = [\"ps\", \"-x\"]","","subprocess.run(ps_command)","","# The os.system function executes the command as a string","# The subprocess.run function takes a list of command arguments","# The commands are conditionally defined to handle both Unix-like and Windows systems"],"id":1}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":25},"action":"remove","lines":["Importing the os Module"],"id":4},{"start":{"row":0,"column":2},"end":{"row":0,"column":21},"action":"insert","lines":["Importando o módulo"]}],[{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["e"],"id":5},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"remove","lines":["l"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"remove","lines":["u"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"remove","lines":["d"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"remove","lines":["o"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"remove","lines":["M"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":[" "]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["s"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["s"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["e"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["c"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["o"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["r"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["p"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"remove","lines":["b"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["u"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["s"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":[" "]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["e"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["h"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["t"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":[" "]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["g"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["n"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["i"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["t"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"remove","lines":["r"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"remove","lines":["o"]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"remove","lines":["m"],"id":6},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"remove","lines":["I"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"remove","lines":[" "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["#"]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]},{"start":{"row":1,"column":9},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":39},"action":"remove","lines":["# Importing platform to identify the OS"],"id":7},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]},{"start":{"row":2,"column":17},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":13},"end":{"row":0,"column":21},"action":"remove","lines":["o módulo"],"id":8},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["b"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["i"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["b"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["l"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["i"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["o"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["t"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["c"],"id":9},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["a"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":2},"end":{"row":5,"column":40},"action":"remove","lines":["Determine the current operating system"],"id":10},{"start":{"row":5,"column":2},"end":{"row":5,"column":39},"action":"insert","lines":["Determine o sistema operacional atual"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":63},"action":"remove","lines":[" the appropriate command for listing directory contents"],"id":11},{"start":{"row":8,"column":8},"end":{"row":8,"column":64},"action":"insert","lines":["o comando apropriado para listar o conteúdo do diretório"]}],[{"start":{"row":14,"column":2},"end":{"row":14,"column":55},"action":"remove","lines":["Running a directory listing command using os.system()"],"id":13},{"start":{"row":14,"column":2},"end":{"row":14,"column":68},"action":"insert","lines":["Executando um comando de listagem de diretórios usando os.system()"]}],[{"start":{"row":17,"column":2},"end":{"row":17,"column":60},"action":"remove","lines":["Running a directory listing command using subprocess.run()"],"id":14},{"start":{"row":17,"column":2},"end":{"row":17,"column":73},"action":"insert","lines":["Executando um comando de listagem de diretórios usando subprocess.run()"]}],[{"start":{"row":20,"column":2},"end":{"row":20,"column":76},"action":"remove","lines":["Using subprocess.run() with an additional argument for long listing format"],"id":15},{"start":{"row":20,"column":2},"end":{"row":20,"column":83},"action":"insert","lines":["Usando subprocess.run() com um argumento adicional para formato de listagem longa"]}],[{"start":{"row":28,"column":2},"end":{"row":28,"column":78},"action":"remove","lines":["Using subprocess.run() with two additional arguments to list a specific file"],"id":17},{"start":{"row":28,"column":2},"end":{"row":28,"column":90},"action":"insert","lines":["Usando subprocess.run() com dois argumentos adicionais para listar um arquivo específico"]}],[{"start":{"row":37,"column":1},"end":{"row":37,"column":40},"action":"remove","lines":[" Running uname -a or equivalent command"],"id":18},{"start":{"row":37,"column":1},"end":{"row":37,"column":43},"action":"insert","lines":["Executando uname -a ou comando equivalente"]}],[{"start":{"row":37,"column":1},"end":{"row":37,"column":2},"action":"insert","lines":[" "],"id":19}],[{"start":{"row":45,"column":2},"end":{"row":45,"column":37},"action":"remove","lines":["Running ps -x or equivalent command"],"id":20},{"start":{"row":45,"column":2},"end":{"row":45,"column":41},"action":"insert","lines":["Executando ps -x ou comando equivalente"]}],[{"start":{"row":53,"column":0},"end":{"row":55,"column":85},"action":"remove","lines":["# The os.system function executes the command as a string","# The subprocess.run function takes a list of command arguments","# The commands are conditionally defined to handle both Unix-like and Windows systems"],"id":21},{"start":{"row":53,"column":0},"end":{"row":55,"column":91},"action":"insert","lines":["# A função os.system executa o comando como uma string","# A função subprocess.run recebe uma lista de argumentos de comando","# Os comandos são definidos condicionalmente para lidar com sistemas do tipo Unix e Windows"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":55,"column":91},"end":{"row":55,"column":91},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1735257050860,"hash":"14a80f682fb4e9b7d80f8e81a9141f4c7ccdae53"}