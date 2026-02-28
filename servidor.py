import socket
HOST = "127.0.0.1"
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(1)
print("Servidor entrando em conexão...")
conexao, endereço = s.accept()

print("Cliente conectado: ",endereço)

mensagem = conexao.recv(1024).decode()
print("Mensagem recebida:",mensagem)

conexao.send("Recebi sua mensagem!".encode())
conexao.close()

