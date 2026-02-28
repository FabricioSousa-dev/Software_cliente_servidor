import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print("Conectado ao servidor!")

while True:
    mensagem = input("Digite uma mensagem : ")

    if mensagem.lower() == "sair":
        break

    cliente.send(mensagem.encode())

    resposta = cliente.recv(1024).decode()
    print("O servidor respondeu:", resposta)

cliente.close()

print("******")