import random

# Função para verificar se um número é primo


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Função para encontrar o maior divisor comum de dois números


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para gerar um número primo aleatório dentro de um intervalo


def generate_prime(start, end):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# Função para gerar as chaves pública e privada do RSA


def generate_rsa_keys():
    # Selecionar dois números primos grandes p e q
    p = generate_prime(1000, 10000)
    q = generate_prime(1000, 10000)

    # Calcular n = p * q
    n = p * q

    # Calcular a função totiente de Euler phi(n)
    phi = (p - 1) * (q - 1)

    # Selecionar um número inteiro e tal que 1 < e < phi e gcd(e, phi) = 1
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Calcular o inverso multiplicativo de e módulo phi
    d = pow(e, -1, phi)

    # Retornar as chaves pública e privada
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Função para criptografar uma mensagem utilizando a chave pública


def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Função para descriptografar uma mensagem utilizando a chave privada


def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)


# Gerar as chaves pública e privada
public_key, private_key = generate_rsa_keys()

print("CHAVE PÚBLICA:", public_key)
print("CHAVE PRIVADA:", private_key)


# Exemplo de mensagem a ser criptografada
message = "Ronaldo Toshiaki Oikawa"

# Criptografar a mensagem utilizando a chave pública
encrypted_message = encrypt(message, public_key)

# Descriptografar a mensagem utilizando a chave privada
decrypted_message = decrypt(encrypted_message, private_key)

# Imprimir a mensagem original, a mensagem criptografada e a mensagem descriptografada
print("Mensagem original:", message)
print("Mensagem criptografada:", encrypted_message)
print("Mensagem descriptografada:", decrypted_message)
