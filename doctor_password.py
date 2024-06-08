# doctor_password.py

from PyQt5 import QtCore, QtGui, QtWidgets
import Main_Window  # Main_Window modülünü ithal ediyoruz

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.passwordList = QtWidgets.QListWidget(self.centralwidget)
        self.passwordList.setObjectName("passwordList")
        self.verticalLayout.addWidget(self.passwordList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Şifreleri yüklemek için Main_Window'daki rtn_pass metodunu kullanıyoruz
        self.passwords = Main_Window.Ui_MainWindow().rtn_pass()
        self.load_passwords()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.label.setText(_translate("MainWindow", "Doctor Passwords"))

    def load_passwords(self):
        for password in self.passwords:
            self.passwordList.addItem(password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
