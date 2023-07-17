import hashlib

# Função de substituição simples


def substituicao(texto, chave_substituicao):
    texto_criptografado = ''
    tamanho_chave = len(chave_substituicao)

    for caractere in texto:
        if caractere.isalpha():
            indice = ord(caractere.lower()) - ord('a')
            caractere_criptografado = chave_substituicao[indice %
                                                         tamanho_chave]
            texto_criptografado += caractere_criptografado
        else:
            texto_criptografado += caractere
    return texto_criptografado

# Função de transposição simples


def transposicao(texto, chave_transposicao):
    texto_criptografado = ''
    tamanho_chave = len(chave_transposicao)
    colunas = tamanho_chave
    linhas = -(-len(texto) // colunas)  # divisão arredondada para cima

    matriz = [[''] * colunas for _ in range(linhas)]
    indice = 0

    for j in range(colunas):
        for i in range(linhas):
            if indice < len(texto):
                matriz[i][j] = texto[indice]
                indice += 1

    for i in range(linhas):
        for j in range(colunas):
            texto_criptografado += matriz[i][j]

    return texto_criptografado

# Classe para a máquina de rotor


class RotorMachine:
    def __init__(self, chave_rotor):
        self.chave_rotor = chave_rotor
        self.posicao = 0

    def criptografar(self, texto):
        texto_criptografado = ''
        for caractere in texto:
            if caractere.isalpha():
                indice = ord(caractere.lower()) - ord('a')
                indice_criptografado = (indice + self.posicao) % 26
                caractere_criptografado = self.chave_rotor[indice_criptografado]
                texto_criptografado += caractere_criptografado
            else:
                texto_criptografado += caractere
            self.posicao = (self.posicao + 1) % 26
        return texto_criptografado


# Ler a chave original do arquivo
with open('chave_original.txt', 'r') as arquivo_chave_original:
    chave_original = arquivo_chave_original.read().strip()

# Gerar a chave hash
hasher = hashlib.sha256()
hasher.update(chave_original.encode())
chave_hash = hasher.hexdigest()

# Escrever a chave hash no arquivo
with open('chave_hash.txt', 'w') as arquivo_chave_hash:
    arquivo_chave_hash.write(chave_hash)

# Ler a chave secreta do arquivo
with open('chave_secreta.txt', 'r') as arquivo_chave_secreta:
    chave_secreta = arquivo_chave_secreta.read().strip()

# Ler a mensagem do arquivo
with open('mensagem.txt', 'r') as arquivo_mensagem:
    mensagem = arquivo_mensagem.read().strip()

# Realizar a substituição
mensagem_substituida = substituicao(mensagem.lower(), chave_secreta)

# Realizar a transposição
mensagem_transposta = transposicao(mensagem_substituida, chave_secreta)

# Criar a máquina de rotor
maquina_rotor = RotorMachine(chave_secreta)

# Criptografar a mensagem com a máquina de rotor
mensagem_criptografada = maquina_rotor.criptografar(mensagem_transposta)

# Calcular o hash da mensagem criptografada
hasher.update(mensagem_criptografada.encode())
hash_final = hasher.hexdigest()

print("Mensagem criptografada:", mensagem_criptografada)
print("Hash:", hash_final)
