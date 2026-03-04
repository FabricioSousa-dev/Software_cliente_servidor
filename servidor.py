import socket
import threading
from cryptography.fernet import Fernet

HOST = "127.0.0.1"
PORT = 5000

# Carregar chave
with open("chave.key", "rb") as arquivo:
    chave = arquivo.read()

fernet = Fernet(chave)

clientes = []

def broadcast(mensagem):
    for cliente in clientes:
        try:
            cliente.send(mensagem)
        except:
            cliente.close()
            clientes.remove(cliente)

def atender_cliente(conexao, endereco):
    print("Cliente conectado:", endereco)

    while True:
        try:
            mensagem = conexao.recv(1024)
            if not mensagem:
                break

            mensagem_descriptografada = fernet.decrypt(mensagem).decode()
            print(f"{endereco}: {mensagem_descriptografada}")

            broadcast(mensagem)

        except Exception as e:
            print("Erro:", e)
            break

    print("Cliente desconectado:", endereco)
    clientes.remove(conexao)
    conexao.close()

def enviar_mensagem_servidor():
    while True:
        mensagem = input("Servidor: ")
        mensagem_formatada = f"Servidor: {mensagem}"
        mensagem_criptografada = fernet.encrypt(mensagem_formatada.encode())
        broadcast(mensagem_criptografada)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor iniciado...")
print("Aguardando conexões...")

# Thread para permitir servidor enviar mensagens
thread_envio = threading.Thread(target=enviar_mensagem_servidor)
thread_envio.daemon = True
thread_envio.start()

while True:
    conexao, endereco = servidor.accept()
    clientes.append(conexao)

    thread = threading.Thread(target=atender_cliente, args=(conexao, endereco))
    thread.start()