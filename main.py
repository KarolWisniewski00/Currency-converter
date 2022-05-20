# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import requests
import json

class API():
    def __init__(self):
        self.list_code=[]
        self.list_mid=[]
        response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/")
        if (response.status_code != requests.codes.ok):
            print('error')
        else:
            tab = response.json()
            values_list=tab[0]['rates']
            for i in values_list:
                self.list_code.append(i['code'])
                self.list_mid.append(i["mid"])
            self.list_code.append('PLN')
            self.list_mid.append("1")

    
    def retur_list_code(self):
        return self.list_code

    def retur_list_mid(self):
        return self.list_mid

class GUI(object):
    def __init__(self):
        api = API()
        self.list_code=api.retur_list_code()
        self.list_mid=api.retur_list_mid()
        self.set_code_mid={}
        index=0
        for i in self.list_code:
            self.set_code_mid[i] = self.list_mid[index]
            index+=1

    def setupUi(self, Form):
        #Inicjalizacja interfejsu graficznego
        Form.setObjectName("Form")
        Form.resize(792, 480)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)              
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #Podział na 3 kolumny lewo-środek-prawo (zachowanie wymiarów przy rozciąganiu)

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #Styl/właściwości lewej kolumny

        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #podział na komórki (zachowanie wymiarów przy rozciąganiu)

        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 20))               #Rozmiar boxa
        self.comboBox_2.setObjectName("comboBox_2")
        for i in self.list_code:
            self.comboBox_2.addItem("")
        #inicjalizacja dolnego boxa

        self.gridLayout_2.addWidget(self.comboBox_2, 6, 0, 1, 1, QtCore.Qt.AlignHCenter) #dodanie boxa do komórek(lewa kolumna)

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 20))
        self.comboBox.setObjectName("comboBox")
        for i in self.list_code:
            self.comboBox.addItem("")
        #inicjalizacja górnego boxa

        self.gridLayout_2.addWidget(self.comboBox, 4, 0, 1, 1)  #dodanie boxa do komórek(lewa kolumna)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        #inicjalizacja napisu górnego z lewej strony

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom) #dodanie napisu górnego do komórek(lewa kolumna)

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        #inicjalizacja napisu dolnego z lewej strony

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom) #dodanie napisu dolnego do komórek(lewa kolumna)

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        #inicjalizacja pustej przestrzeni

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)   #dodanie pustej przestrzeni do komórek(lewa kolumna)
        self.horizontalLayout_4.addWidget(self.frame)           #dodanie komórek do lewej kolumny

        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        #Styl/właściwości środkowej kolumny

        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        #podział na komórki (zachowanie wymiarów przy rozciąganiu)

        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        #inicjalizacja napisu górnego z prawej strony

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)   #dodanie napisu górnego do komórek(środkowa kolumna)

        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        #inicjalizacja napisu dolnego z prawej strony
        
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom) #dodanie napisu dolnego do komórek(środkowa kolumna)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        #inicjalizacja pola tekstowego dolnego

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 1)    #dodanie pola tekstowego dolnego do komórek(środkowa kolumna)

        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit.setObjectName("lineEdit")
        #inicjalizacja pola tekstowego górnego

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)      #dodanie pola tekstowego górnego do komórek(środkowa kolumna)

        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        #inicjalizacja pustej przestrzeni

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)   #dodanie pustej przestrzeni do komórek(Środkowa kolumna)
        self.horizontalLayout_4.addWidget(self.frame_3)         #dodanie komórek do środkowej kolumny

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        #Styl/właściwości prawej kolumny

        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        #podział na komórki (zachowanie wymiarów przy rozciąganiu)

        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pressed)
        #inicjalizacja górnego przycisku -calculate

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)   #dodanie przycisku Górnego do komórek(prawa kolumna)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 20))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pressed_close)
        #inicjalizacja dolnego przycisku -close

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)    #dodanie przycisku dolnego do komórek(prawa kolumna)

        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        #inicjalizacja pustej przestrzeni

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1) #dodanie pustej przestrzeni do komórek(prawa kolumna)
        self.horizontalLayout_4.addWidget(self.frame_2)     #dodanie komórek do prawej kolumny

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        #inicjalizacja wartości/zawartości przycisków/comboboxów/napisów
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Currency"))
        index=0
        for i in self.list_code:
            self.comboBox_2.setItemText(index, _translate("Form",str(i)))
            index+=1
        index=0
        for i in self.list_code:
            self.comboBox.setItemText(index, _translate("Form",str(i)))
            index+=1
        self.label_2.setText(_translate("Form", "From this currency"))
        self.label_3.setText(_translate("Form", "To this currency"))
        self.label.setText(_translate("Form", "Convert this amount"))
        self.label_4.setText(_translate("Form", "Result"))
        self.pushButton.setText(_translate("Form", "CALCULATE"))
        self.pushButton_2.setText(_translate("Form", "CLOSE"))

    def pressed(self):
        #print("[FROM] Code - {} Mid - {} Line - {}".format(self.comboBox.currentText(),self.set_code_mid[self.comboBox.currentText()],self.lineEdit.text()))
        #print("[TO]   Code - {} Mid - {} Line - {}".format(self.comboBox_2.currentText(),self.set_code_mid[self.comboBox_2.currentText()],self.lineEdit_2.text()))
        #print(20*"-")
        try:
            line_top_value = float(self.lineEdit.text())
            mid_top_value = float(self.set_code_mid[self.comboBox.currentText()])
            mid_bot_value = float(self.set_code_mid[self.comboBox_2.currentText()])
            zloty_top=line_top_value*mid_top_value
            result=zloty_top/mid_bot_value
            self.lineEdit_2.setText(str(result))
        except:
            self.show_popup()
            self.lineEdit.setText("1")
        
    
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Value Error')
        msg.setText("Prease type in digits")
        msg.setIcon(QMessageBox.Warning)
        x= msg.exec_()

    def pressed_close(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GUI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
