from PyQt5 import QtCore, QtGui, QtWidgets, Qt, uic


def funcao_principal():
    linha1 = Login.lineEdit.text()
    linha2 = Login.lineEdit_2.text()
    Login.lineEdit.setText("")
    Login.lineEdit_2.setText("")

'''def login():
    Login.pushButton.'''

def limpar_entrada():
    Login.pushButton_2.command = linha1.remove ()
    Login.pushButton_2.lineEdit_2.remove()

def fechar():
    Login.pushButton_3.command = quit()

def chama_segunda_tela():
      segunda_tela.show()
    

app =  QtWidgets.QApplication([])
Login = uic.loadUi('Login.ui')
segunda_tela = uic.loadUi('Tela2.ui')
#Login.label.Q
#photo = application.qrc ("C:\\Users\\Edi e Josi\\Documents\\repositorio_python\\codepython\\sistemaSerasa\\Icon\\login.qrc")
#Login.label_2 = photo
Login.pushButton.clicked.connect(chama_segunda_tela)
Login.pushButton_2.clicked.connect(limpar_entrada)
Login.pushButton_3.clicked.connect(fechar)
Login.show()
app.exec()