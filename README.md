📌 Software Cliente-Servidor

Este projeto implementa uma comunicação simples entre cliente e servidor utilizando Python e sockets TCP. Ele serve como exemplo prático para entender o modelo cliente-servidor, onde um programa (cliente) envia requisições e outro programa (servidor) responde a essas requisições.

💡 Visão Geral

O repositório contém dois scripts principais:

servidor.py: código que implementa o servidor, que fica escutando conexões e responde às mensagens do cliente.

cliente.py: código que envia mensagens ao servidor e recebe respostas.

O objetivo é demonstrar a base de comunicação via socket TCP entre dois componentes de rede.

📁 Estrutura do Projeto
Software_cliente_servidor/
├── .idea/                 -> Configurações do IDE
├── cliente.py             -> Cliente que se conecta ao servidor
├── servidor.py            -> Servidor que atende clientes
└── README.md              -> Documentação do projeto
🚀 Pré-requisitos

Para rodar o projeto você precisa ter:

🐍 Python 3.x instalado

Terminal ou prompt de comando

📦 Como Usar
1. Iniciar o Servidor

Abra um terminal e execute:

python servidor.py

O servidor irá iniciar e começar a escutar conexões na porta configurada no código.

2. Iniciar o Cliente

Em outro terminal, execute:

python cliente.py

O cliente irá se conectar ao servidor e trocar mensagens conforme implementado no script.

🛠 Funcionamento
📌 Cliente

O cliente cria um socket e se conecta ao servidor, enviando uma requisição. Ele pode enviar mensagens e aguardar respostas para cada uma:

Conecta ao servidor

Envia mensagem

Recebe resposta

Implementação ocorre no arquivo cliente.py.

📌 Servidor

O servidor cria um socket que “escuta” em uma porta específica e aguarda conexões. Quando um cliente se conecta:

Aceita a conexão

Recebe dados

Processa e envia resposta

Aguarda novas requisições

Implementação ocorre no arquivo servidor.py.

📚 Conceitos Importantes

Este projeto explora o modelo cliente-servidor, um padrão arquitetural comum em aplicações distribuídas onde:

O servidor fornece serviços/processa requisições

O cliente solicita tais serviços/processamento

Esses dois componentes se comunicam via sockets em uma rede (ou localmente).

🤝 Contribuindo

Contribuições, sugestões ou melhorias são bem-vindas!
Sinta-se à vontade para abrir um issue ou fazer um pull request.

📜 Licença

Este projeto não possui uma licença especificada.
Você pode adicionar uma conforme sua preferência (por exemplo, MIT, GPL etc.).
