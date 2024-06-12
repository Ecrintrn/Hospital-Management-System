# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import Doctor  # Doctor.py modülünü ithal ediyoruz

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 333)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 421, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_dctr_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_dctr_name.setObjectName("txt_dctr_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_dctr_name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txt_dctr_surname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_dctr_surname.setObjectName("txt_dctr_surname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_dctr_surname)
        self.box_dctr_spe = QtWidgets.QComboBox(self.formLayoutWidget)
        self.box_dctr_spe.setObjectName("box_dctr_spe")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.box_dctr_spe)
        self.box_aca_rank = QtWidgets.QComboBox(self.formLayoutWidget)
        self.box_aca_rank.setObjectName("box_aca_rank")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.box_aca_rank)
        self.txt_pass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_pass.setObjectName("txt_pass")
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)  # Şifreyi gizlemek için
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_pass)
        self.btn_dctr_save = QtWidgets.QPushButton(self.groupBox)
        self.btn_dctr_save.setGeometry(QtCore.QRect(150, 240, 111, 51))
        self.btn_dctr_save.setObjectName("btn_dctr_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.doctor = Doctor.Doctor()

        self.box_aca_rank.addItems(self.doctor.academic_rank)
        self.box_dctr_spe.addItems(self.doctor.specialization)
        
        self.btn_dctr_save.clicked.connect(self.add_doctor)  # Düğmeyi metodumuza bağladık

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Doctor Information"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Surname:"))
        self.label_3.setText(_translate("MainWindow", "Academic Rank:"))
        self.label_5.setText(_translate("MainWindow", "Specialization:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.btn_dctr_save.setText(_translate("MainWindow", "Save"))
    
    def add_doctor(self):
        doctor_name = self.txt_dctr_name.text()
        doctor_surname = self.txt_dctr_surname.text()
        academic_rank = self.box_aca_rank.currentText()
        specialization = self.box_dctr_spe.currentText()
        password = self.txt_pass.text()
        
        if not doctor_name or not doctor_surname or not academic_rank or not specialization or not password:
            QtWidgets.QMessageBox.warning(None, "Input Error", "All fields must be filled out.")
            return
        
        self.doctor.add_doctor(doctor_name, doctor_surname, academic_rank, specialization, password)
        QtWidgets.QMessageBox.information(None, "Success", "Doctor added successfully.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
