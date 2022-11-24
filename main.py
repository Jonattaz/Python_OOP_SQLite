#Importar arquivo Pessoa.py
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
jonatas = Pessoa(1, "Jonatas Santos")
print(jonatas.nome)

#Chamar objeto de banco de dados
db = Database()

#Instância o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = PessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)
