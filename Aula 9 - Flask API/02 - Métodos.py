from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

# Conexão com Banco de Dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="php_db"
    )


#GET - Consulta de dados (geral)
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    resultado = cursor.fetchall()
    conexao.close()
    return jsonify(resultado)


#GET - Consulta de dados (individual)
@app.route('/usuarios/<int:id>', methods=["GET"])
def buscar_usuarios(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    resultado = cursor.fetchall()
    conexao.close()
    return jsonify(resultado)


#POST - Enviar dados
@app.route('/usuarios', methods=["POST"])
def enviar_usuario():
    dados = request.json
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT into USERS (login, senha) VALUES (%s, %s)", (dados['login'], dados['senha']))
    conexao.commit()
    conexao.close()
    return jsonify({"login":dados['login']}), 201
    
    
#PUT - Atualizar dados
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.json
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET login = %s where id = %s', (dados['login'], id))
    conn.commit()
    conn.close()
    if cursor.rowcount:
        return jsonify({"id":id, "login":dados["login"]})
    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)