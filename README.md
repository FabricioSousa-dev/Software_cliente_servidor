📡 Chat Cliente-Servidor com Sockets e Criptografia
🎯 Objetivo

Desenvolver uma aplicação de chat utilizando arquitetura cliente-servidor com comunicação via sockets TCP e criptografia de mensagens.

🏗 Arquitetura

O sistema segue o modelo Cliente-Servidor, onde:

O servidor centraliza as conexões

Múltiplos clientes podem se conectar simultaneamente

Cada cliente é tratado em uma thread separada

🌐 Comunicação

Foi utilizado:

Sockets nativos do Python

Protocolo TCP (Transmission Control Protocol)

O TCP foi escolhido por:

Garantir entrega das mensagens

Manter a ordem dos pacotes

Fornecer comunicação confiável

🔄 Serialização de Dados

As mensagens passam pelo seguinte fluxo:

String digitada pelo usuário

Conversão para bytes usando .encode()

Criptografia

Envio via socket

No recebimento:

Recebimento dos bytes

Descriptografia

Conversão para string usando .decode()

🔐 Criptografia

Foi utilizada Criptografia Simétrica AES através da biblioteca cryptography (Fernet).

🔑 Chave Criptográfica

A chave é gerada pelo arquivo gerar_chave.py

É armazenada em chave.key

A mesma chave é utilizada pelo cliente e pelo servidor

Como é criptografia simétrica, a mesma chave criptografa e descriptografa

🔒 Funcionamento

Mensagem original → AES Encrypt → Rede → AES Decrypt → Mensagem original

Mesmo que a mensagem seja interceptada, o conteúdo trafega criptografado.

🧵 Concorrência

O servidor utiliza Threads para:

Permitir múltiplos clientes simultâneos

Permitir envio de mensagens pelo próprio servidor

🚀 Como Executar

Instalar dependência:

pip install cryptography

Gerar chave:

python gerar_chave.py

Iniciar servidor:

python servidor.py

Iniciar clientes (em terminais separados):

python cliente.py
🎓 3️⃣ Explicação Formal da Chave:

Foi utilizada criptografia simétrica AES por meio da biblioteca Fernet.
A chave criptográfica é gerada previamente e compartilhada entre cliente e servidor.
Como se trata de criptografia simétrica, a mesma chave é responsável tanto pela criptografia quanto pela descriptografia das mensagens.
Isso garante confidencialidade no tráfego de dados na rede.
