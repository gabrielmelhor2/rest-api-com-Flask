from flask import Blueprint, Flask, jsonify, request, make_response
from db import Banco

blueprint_api = Blueprint("api", __name__, url_prefix="/books/api/v1/lista")

banco = Banco()

livros = []


@blueprint_api.route("/", methods=["GET"])
@blueprint_api.route("/<int:id>", methods=["GET"])
def get_books(id=None):
    lista = banco.listar_livros()
    if lista != False:
        if id != None:
            lista = banco.listar_livro(id)
            return jsonify({"Lista": lista})
        return jsonify(lista)
    return make_response(jsonify({"error": "Nenhum dado encontrado!"}))


@blueprint_api.route("/add/", methods=["POST"])
def add_books():
    if request.json:
        banco.adicionar_livros(request.json[0])
    return make_response(jsonify({"error": "Dados inseridos com sucesso!"}))


@blueprint_api.route("/put/<int:id>", methods=["PUT"])
def put_books(id=None):
    if request.json and id != None:
        banco.atualizar_livros(id, request.json[0])
    return make_response(jsonify({"error": "Dados atualizados com sucesso!"}))


@blueprint_api.route("/delete/<int:id>", methods=["DELETE"])
def delete_books(id=None):
    if id != None:
        banco.excluir_livros(id)
    return make_response(jsonify({"error": "Dados excluidos com sucesso!"}))


