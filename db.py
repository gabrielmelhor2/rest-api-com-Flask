import dataset


class Banco:
    def listar_livros(self):
        with dataset.connect("sqlite:///db.db") as db:
            books = db["books"].all()
            if db["books"].count() > 0:
                listaLivros = [
                    dict(livro=data["livro"], autor=data["autor"]) for data in books
                ]
                return listaLivros
            else:
                return False

    def listar_livro():
        with dataset.connect("sqlite:///db.db") as db:
            livro = db["books"].find_one(id=id)
        if livro:
            return livro
        else:
            return False

    def adicionar_livros(self, data):
        with dataset.connect("sqlite:///db.db") as db:
            return db["books"].insert(dict(livro=data["livro"], autor=data["autor"]))

    def atualizar_livros(self, id, data):
        with dataset.connect("sqlite:///db.db") as db:
            return db["books"].update(
                dict(id=id, livro=data["livro"], autor=data["autor"]), ["id"]
            )

    def excluir_livros(self, id):
        with dataset.connect("sqlite:///db.db") as db:
            return db["books"].delete(id=id)
    