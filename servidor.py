import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def atender_cliente(conexao, endereco):
    print("Cliente conectado:", endereco)

    while True:
        try:
            mensagem = conexao.recv(1024).decode()
            if not mensagem:
                break

            print("Mensagem recebida:", mensagem)

            resposta = f"Servidor recebeu: {mensagem}"
            conexao.send(resposta.encode())

        except:
            break

    print("Cliente desconectado:", endereco)
    conexao.close()


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor iniciado...")
print("Esperando conexões...")

while True:
    conexao, endereco = servidor.accept()
    thread = threading.Thread(target=atender_cliente, args=(conexao, endereco))
    thread.start()
