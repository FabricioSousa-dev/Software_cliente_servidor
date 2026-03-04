from cryptography.fernet import Fernet

chave = Fernet.generate_key()

with open("chave.key", "wb") as arquivo:
    arquivo.write(chave)

print("Chave gerada com sucesso!")