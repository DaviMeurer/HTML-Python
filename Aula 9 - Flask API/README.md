# Módulos à serem baixados
``
pip install flask, flask-cors, mysql-connector-python
``
# Atividade Avaliativa

## Objetivo

Um aplicativo web que recebe inputs do usuário e realiza uma validação para checar se ele está registrado em nosso sistema.  
Se sim, aparecerá um alert de "usuário encontrado". Caso contrário, um alert de "usuário inválido".

## Funcionalidade

Os valores são inseridos pelo usuário na página web e convertidos em JSON.  
Esses dados são enviados via métodos HTTP para o back-end, permitindo a comunicação entre sistemas.

A API recebe os dados e valida com uma consulta ao banco de dados, feita por um cursor criado na própria API.  
Ao finalizar, o front-end exibe um alert informando se o login foi bem-sucedido ou não.
