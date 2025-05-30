from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="AA_DB",
    )

@app.route("/login", methods=["POST"])
def checarUsuario():
    dados = request.json
    usuario = dados.get("usuario")
    senha = dados.get("senha")

    if not usuario or not senha:
        return jsonify({"erro":"Nome ou senha incorretos."}), 400

    conexao = conectar(),
    cursor = conexao.cursor(dictionary=True),
    cursor.execute("SELECT id, usuario FROM USUARIOS WHERE id=%s", (dados["usuario"]))
    retorno = cursor.fetchone()
    conexao.close()

    if retorno(retorno["senha"], senha):
        return jsonify({"mensagem":"Login bem-sucedido!"}), 200
    return jsonify({"erro":"Usuário ou senha incorretos."}), 401

if __name__ == "__main__":
    app.run(debug=True, port=5000)