import sqlite3


CREATE_TABLE = "create table cliente(id integer primary key, nome text, telefone integer, endereco text, cpf integer)"

INSERT_CLIENTE = "insert into cliente (nome, telefone, endereco, cpf) values (?, ?, ?, ?);"

BUSCA_CLIENTE_POR_NOME = "select * from cliente where nome = ?;"

EXCLUIR_CLIENTE_POR_NOME = "delete from cliente where nome = ?;"

def connect():
    return sqlite3.connect("cliente.db")

def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

def insert(conexao, nome, telefone, endereco, cpf):
    with conexao:
        conexao.execute(INSERT_CLIENTE,( nome, telefone, endereco, cpf))

def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_CLIENTE_POR_NOME, (nome,)).fetchall()

def excluir_nome(conexao, nome):
    with conexao:
        return conexao.execute(EXCLUIR_CLIENTE_POR_NOME, (nome,)).fetchall()