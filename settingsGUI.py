# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 271)
        Form.setMinimumSize(QtCore.QSize(500, 271))
        Form.setMaximumSize(QtCore.QSize(500, 271))
        Form.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #0f121c, stop: 1 #0b0d14);\n"
"color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 461, 67))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #0f121c, stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.cropline = QtWidgets.QLineEdit(self.layoutWidget)
        self.cropline.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #0f121c, stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;")
        self.cropline.setObjectName("cropline")
        self.gridLayout.addWidget(self.cropline, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.saveSet = QtWidgets.QPushButton(Form)
        self.saveSet.setGeometry(QtCore.QRect(220, 240, 50, 20))
        self.saveSet.setMinimumSize(QtCore.QSize(50, 20))
        self.saveSet.setMaximumSize(QtCore.QSize(50, 20))
        self.saveSet.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"border-radius: 10px;\n"
"width: 60px;\n"
"height: 30px;")
        self.saveSet.setObjectName("saveSet")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Folder Paths"))
        self.label_4.setText(_translate("Form", "CroppedText Folder:"))
        self.label_2.setText(_translate("Form", "Translated Folder:"))
        self.saveSet.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
