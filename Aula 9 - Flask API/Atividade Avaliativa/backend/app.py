from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="aa_db",
    )

@app.route("/", methods=["GET"])
def telaInicial():
    return "Seja bem-vindo!", 200

@app.route("/login", methods=["POST"])
def checarUsuario():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Email ou senha não informados."}), 400

    conectar = conexao()
    cursor = conectar.cursor(dictionary=True)
    cursor.execute("SELECT id, email, senha FROM USUARIOS WHERE email = %s", (email,))
    retorno = cursor.fetchone()
    conectar.close()

    if retorno and retorno["senha"] == senha:
        return jsonify({"mensagem": "Login bem-sucedido!"}), 200

    return jsonify({"erro": "Usuário ou senha incorretos."}), 401

if __name__ == "__main__":
    app.run(debug=True, port=5000)