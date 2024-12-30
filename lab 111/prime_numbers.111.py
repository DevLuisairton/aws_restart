# Conecte-se à instância EC2 do host Linux
# Crie e navegue até seu diretório de trabalho
#cd~
# Escreva o script Python
#números_primos.py


#Função para verificar se um número é primo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Lista para armazenar números primos
prime_numbers = []

# Percorra os números de 1 a 250 e verifique se há números primos
for num in range(1, 251):
    if is_prime(num):
        prime_numbers.append(num)

# Caminho do arquivo para armazenar os resultados
file_path = "D:\AWS reStart Python\AWS reStrart Python Labs\results.txt"

# Grava números primos no arquivo de resultados
with open(file_path, "w") as file:
    for prime in prime_numbers:
        file.write(str(prime) + "\n")

print(f"Prime numbers between 1 and 250 written to {file_path}")


# Salve o script prime_numbers.py e torne-o executável:
# chmod +x números_primos.py
# Execute o script usando Python 3:
# python3 números primos.py
