import hashlib

# Recebe uma string do usuário
text = input("Digite uma string para mascarar: ")

# Gera o hash SHA-1 da string
hash_txt = hashlib.sha1(text.encode())

# Exibe o hash no formato hexadecimal
print("Hash (SHA-1):", hash_txt.hexdigest())
