import socket
import threading
from cryptography.fernet import Fernet

HOST = "127.0.0.1"
PORT = 5000

# Carregar chave
with open("chave.key", "rb") as arquivo:
    chave = arquivo.read()

fernet = Fernet(chave)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print("Conectado ao servidor!")

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024)
            mensagem_descriptografada = fernet.decrypt(mensagem).decode()
            print("\nMensagem recebida:", mensagem_descriptografada)
        except:
            print("Conexão encerrada.")
            cliente.close()
            break

thread = threading.Thread(target=receber)
thread.start()

while True:
    mensagem = input("")
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    cliente.send(mensagem_criptografada)

