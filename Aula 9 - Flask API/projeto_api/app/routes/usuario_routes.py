#ROTAS 
from flask import Blueprint, jsonify, request
import app.controllers.usuario_controller as controller

usuario_bp=Blueprint('usuarios', __name__, url_prefix='/usuarios')

# GET *
@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    try:
        usuarios = controller.listar_todos()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({'menssage': str(e)}), 500

# GET ONE
@usuario_bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    try:
        usuarios = controller.buscar(id)
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({'menssage': str(e)}), 500


# POST
@usuario_bp.route("/", methods=["POST"])
def criar():
    try:
        dados = request.json
        novo_id = controller.criar(dados)
        return jsonify({"id": novo_id, "mensagem":"Usuário criado com sucesso."})
    
    except Exception as e:
        return jsonify({"mensagem":str(e)}), 500
    
# PUT
@usuario_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    try:
        dados = request.json
        controller.atualizar(id, dados)
        return jsonify({"id":id, "mensagem":"Usuário atualizado com sucesso."}), 200
    except Exception as e:
        return jsonify({"mensagem": str(e)}), 500
    
# DELETE
@usuario_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    try:
        controller.deletar(id)
        return jsonify({"id":id, "mensagem":"Usuário deletado com sucesso."}), 200
    except Exception as e:
        return jsonify({"mensagem": str(e)}), 500