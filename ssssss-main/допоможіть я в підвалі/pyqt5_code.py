from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 571))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("map.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 240, 131, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 260, 131, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 150, 101, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 300, 121, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 10, 121, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 380, 131, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 531, 41))
        self.label_2.setStyleSheet("font-size: 30px\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Frankivsk (You are here)", "You are here"))
        self.pushButton_2.setText(_translate("MainWindow", "Kolomya (You are here)", "You are here"))
        self.pushButton_3.setText(_translate("MainWindow", "Kyiv (You are here)", "You are here"))
        self.pushButton_4.setText(_translate("MainWindow", "Donetsk (You are here)", "You are here"))
        self.pushButton_5.setText(_translate("MainWindow", "Warsaw (You are here)", "You are here"))
        self.pushButton_6.setText(_translate("MainWindow", "Chisinau (You are here)", "You are here"))
        self.label_2.setText(_translate("MainWindow", "You don't have permit to cross border!"))

        
def gaming(stopped_p,working_p,width,height,max_speed,stall_speed,rotating_index,a_airport,b_airport, given_money,laps):
    global physics
    global money
    windows.hide()
    physics = Physics(stopped_p, working_p, width, height, max_speed, stall_speed, rotating_index, a_airport + ".png", b_airport + ".png", laps)
    physics.start()
    game = True
    while game:
        if game:
            print("playing")
            game = False
    print("finished_flight")
def restart_map(location):
    if location == spisok[0]:
        bomba.pushButton.setText(f"{spisok[0]} (You are here)")
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        return 1
    if location == spisok[1]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(f"{spisok[1]} (You are here)")
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        return 2
    if location == spisok[2]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(f"{spisok[2]} (You are here)")
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        return 3
    if location == spisok[3]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(f"{spisok[3]} (You are here)")
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        return 4
    if location == spisok[4]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(f"{spisok[4]} (You are here)")
        bomba.pushButton_6.setText(spisok[5])
        return 5
    if location == spisok[5]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(f"{spisok[5]} (You are here)")
        return 6

def frankivsk():
    if restart_map(whereyouat) == 2:
        given_money = 2000
        laps = 2
    gaming(planes["Censa"][0], planes["Censa"][1],150,50,15,5,0.01,spisok[restart_map(whereyouat) - 1], "Frankivsk", given_money,laps)

def closeEvent(event):
    global game
    game = False        

spisok = ["Frankivsk","Kolomya","Kyiv","Donetsk","Warsaw","Chisinau"]
        
planes = {
    "Censa":["Censa - 125 (Stopped).png","Censa - 125 (Working).png"]  
}
whereyouat = "Kolomya"
aircraft_chosen = "Censa"



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows= QtWidgets.QMainWindow()
    bomba = Ui_MainWindow()
    bomba.setupUi(windows)
    bomba.pushButton.released.connect(frankivsk)
    bomba.label_2.hide()
    restart_map(whereyouat)
    windows.show()
    sys.exit(app.exec_())

