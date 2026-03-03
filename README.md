Projeto simples de comunicação Cliente-Servidor utilizando sockets TCP em Python.

O objetivo é demonstrar, de forma prática, como funciona a troca de mensagens entre dois programas através de conexão de rede.

📚 Sobre o Projeto

Este projeto implementa:

🖥️ Servidor que aguarda conexões

💬 Cliente que se conecta ao servidor

🔄 Troca de mensagens entre ambos

🧵 Uso de threads para permitir múltiplas conexões

É um projeto didático para estudo de:

Programação em rede

Arquitetura Cliente-Servidor

Conceito de sockets

Comunicação TCP/IP

📂 Estrutura do Projeto
Software_cliente_servidor/
│
├── servidor.py   # Código do servidor
├── cliente.py    # Código do cliente
└── README.md     # Documentação do projeto
⚙️ Tecnologias Utilizadas

Python 3

Biblioteca padrão socket

Biblioteca threading

Não é necessário instalar nenhuma dependência externa.

🚀 Como Executar
1️⃣ Inicie o servidor

No terminal:

python servidor.py

O servidor ficará aguardando conexões na porta definida no código.

2️⃣ Execute o cliente

Em outro terminal:

python cliente.py

Agora você pode enviar mensagens para o servidor.

💬 Exemplo de Funcionamento

Cliente envia:

Olá servidor!

Servidor responde:

Servidor recebeu: Olá servidor!

Para encerrar a conexão, digite: sair
🧠 Conceitos Aplicados

✔ Modelo Cliente-Servidor
✔ Comunicação via TCP
✔ Manipulação de sockets
✔ Programação concorrente com threads
