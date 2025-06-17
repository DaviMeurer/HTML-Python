#MODELAGEM (lógica)

from app.services.db import conectar
 
def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * from USUARIOS")
    usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()
 
    return usuarios

def buscar(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * from USUARIOS WHERE id=%s", (id,))
    usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()

    return usuarios

def criar(dados):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO USUARIOS(nome, email, senha) VALUES(%s, %s, SHA2(%s, 256))"
    cursor.execute(sql, (dados["nome"], dados["email"], dados["senha"]))
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()
    return novo_id

def atualizar(id, dados):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "UPDATE USUARIOS SET nome = %s, email = %s, senha = %s WHERE id = %s"
    cursor.execute(sql, (dados["nome"], dados["email"], dados["senha"], id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return

def deletar(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM USUARIOS WHERE id = %s"
    cursor.execute(sql, (id, ))
    cursor.commit()
    cursor.close()
    conexao.close()
    return