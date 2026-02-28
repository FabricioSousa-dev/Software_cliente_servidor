import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

cliente.send('Servidor online!'.encode())

resposta = cliente.recv(1024).decode()
print("Servidor respondeu: ",resposta)

cliente.close()
