import data
import sqlite3
from PyQt5 import uic, QtWidgets

#função de cadastro
def cadastrar():
    tela.close()
    conexao = data.connect()
    #data.create(conexao)  # comentar essa linha depois de criar a tabela
    tela_cadastrar.show()
    nome = tela_cadastrar.lineEdit_nome.text()
    telefone = tela_cadastrar.lineEdit_tel.text()
    endereco = tela_cadastrar.lineEdit_end.text()
    cpf = tela_cadastrar.lineEdit_cpf.text()

    data.insert(conexao, nome, telefone, endereco, cpf)

    #limpando o lineEdit
    tela_cadastrar.lineEdit_nome.setText("")
    tela_cadastrar.lineEdit_tel.setText("")
    tela_cadastrar.lineEdit_end.setText("")
    tela_cadastrar.lineEdit_cpf.setText("")
    deletar() 

#se o pushbutton de cadastro for apertado essa mensagem aparece confirmando cadastro
def confirma_cadastro():
    tela_cadastrar.label_cadastro.setText("Cliente cadastrado com sucesso!")

#função de retornar ao menu
def menu():
    tela_cadastrar.label_cadastro.setText("")
    tela_excluir.label_cadastro.setText("")
    tela_procurar.lineEdit_nome.setText("")
    tela_excluir.lineEdit_nome.setText("")
    tela_cadastrar.close()
    tela_mostrar.close()
    tela_procurar.close()
    tela_procuraresultado.close()
    tela_excluir.close()
    tela.show()

#função exibir todos clientes
def mostrar():
    tela.close()
    tela_mostrar.show()
    banco = sqlite3.connect("cliente.db")
    cursor = banco.cursor()
    cursor.execute("select * from cliente")
    lidos = cursor.fetchall()

    #jogando na tabela
    tela_mostrar.tableWidget.setRowCount(len(lidos))
    tela_mostrar.tableWidget.setColumnCount(5)

    for i in range(0, len(lidos)):
        for j in range(0, 5):
            tela_mostrar.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
    
    deletar()

#função deletar
def deletar():
    banco = sqlite3.connect("cliente.db")
    cursor = banco.cursor()
    cursor.execute("""
    delete from cliente 
    where nome is NULL
    or nome = ""
    """)
    banco.commit()
    banco.close()

def procurar():
    tela.close()
    tela_procurar.show()
    banco = sqlite3.connect("cliente.db")
    cursor = banco.cursor()
    nome = tela_procurar.lineEdit_nome.text()
    cursor.execute("select * from cliente where nome = ?", (nome, ))
    lidos = cursor.fetchall()

    #jogando na tabela
    tela_procuraresultado.tableWidget.setRowCount(len(lidos))
    tela_procuraresultado.tableWidget.setColumnCount(5)

    for i in range(0, len(lidos)):
        for j in range(0, 5):
            tela_procuraresultado.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
    banco.close()

def procuraresultado():
    tela_procuraresultado.show()

def excluirnome():
    tela.close()
    tela_excluir.show()
    banco = sqlite3.connect("cliente.db")
    cursor = banco.cursor()
    nome = tela_excluir.lineEdit_nome.text()
    cursor.execute("delete from cliente where nome = ?", (nome, ))
    banco.commit()
    banco.close()
    
def confirma_exclusao():
    tela_excluir.label_cadastro.setText("Cliente excluído com sucesso!")

#telas
app = QtWidgets.QApplication([])
tela = uic.loadUi("menu.ui")
tela_cadastrar = uic.loadUi("cadastro.ui")
tela_mostrar = uic.loadUi("tabela.ui")
tela_procurar = uic.loadUi("procurar.ui")
tela_procuraresultado = uic.loadUi("procuraresultado.ui")
tela_excluir = uic.loadUi("excluir.ui")

#evento dos botões
tela.pushButtonMenuCad.clicked.connect(cadastrar)
tela_cadastrar.pushButtonCad.clicked.connect(cadastrar)
tela_cadastrar.pushButtonCad.clicked.connect(confirma_cadastro)
tela_cadastrar.pushButtonCancel.clicked.connect(menu)
tela_mostrar.pushButtonCancel.clicked.connect(menu)
tela.pushButtonMenuMos.clicked.connect(mostrar)
tela.pushButtonMenuPro.clicked.connect(procurar)
tela_procurar.pushButtonProcurar.clicked.connect(procurar)
tela_procurar.pushButtonProcurar.clicked.connect(procuraresultado)
tela_procuraresultado.pushButtonCancel.clicked.connect(menu)
tela_procurar.pushButtonCancel.clicked.connect(menu)
tela.pushButtonMenuExc.clicked.connect(excluirnome)
tela_excluir.pushButtonCancel.clicked.connect(menu)
tela_excluir.pushButtonExcluir.clicked.connect(excluirnome)
tela_excluir.pushButtonExcluir.clicked.connect(confirma_exclusao)
tela_excluir.pushButtonTabela.clicked.connect(mostrar)

tela.show()
app.exec()