import pygame
from pygame import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint

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
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 10, 171, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 280, 211, 31))
        self.label_3.setStyleSheet("font-size: 20px;\n"
"background-color: white")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 530, 21, 20))
        self.pushButton_8.setStyleSheet("font-size:7px")
        self.pushButton_8.setObjectName("pushButton_8")
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
        self.label_2.setText(_translate("MainWindow", "You don\'t have permit to cross border!"))
        self.pushButton_7.setText(_translate("MainWindow", "Choose plane!"))
        self.label_3.setText(_translate("MainWindow", "Money: 1488"))
        self.pushButton_8.setText(_translate("MainWindow", "1488"))
        
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(287, 467)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 291, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 291, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 160, 291, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 390, 291, 81))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Censa 125"))
        self.pushButton_2.setText(_translate("Form", "AirShip A023"))
        self.pushButton_3.setText(_translate("Form", "Bang B474"))
        self.pushButton_4.setText(_translate("Form", "Abroad Safety license"))

class Physics():
    def __init__(self, p:str, p_working:str, height_p:int ,width:int, max_speed_p:int,stall_speed_p, rotating_index, a_airport, b_airport, laps = 2):
        self.p = p
        self.p_working = p_working
        self.max_speed_p = max_speed_p
        self.height_p = height_p
        self.width_p = width
        self.crashed = False
        self.index = rotating_index
        self.a_airport = a_airport
        self.b_airport = b_airport
        self.laps = laps
        self.stall = stall_speed_p
        self.ended = False
    def start(self):
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        global physics
        global bomba
        global mama
        self.window = display.set_mode((700,600))
        self.shpare = Scene("skibidi sigma pomni (digital fortnite chamba flow) xxxtenctation.png", 0, 500,0, 40000, 100)
        self.shparet = Scene("sky.png", 0 ,-19400 ,0, 40000, 20000)
        self.plane = Plane(physics.p, 0,500 - physics.width_p, physics.height_p,physics.width_p, physics.max_speed_p, physics.stall)
        self.a_airport = Scene(physics.a_airport, 0 , 0,0,800,500)
        self.b_airport = Scene(physics.b_airport ,38200 , 0, 0, 800,500)
        self.scene = [self.shpare,self.shparet,self.a_airport, self.b_airport]
        self.laps_gone = 1
        self.text_surface = font.render(f"Altitude: {self.shpare.rect.y}", True, (255,255,255))
        self.text_surface2 = font.render(f"Speed: {self.plane.speed}", True,(255,255,255))
        self.timer = 0
        self.game = True
        self.filled = 0
        self.fully_filled = False
        mama = False
        while not self.fully_filled:
            self.create_mountain()
        bomba.label_2.hide()
        for i in self.scene:
                    i.move_up(-1)
    def playing(self):
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        global physics
        
        self.timer += 60 / 100
        self.text_surface = font.render(f"Altitude: {self.shpare.rect.y - 500}", True, (255, 255, 255))
        self.text_surface2 = font.render(f"Speed: {int(self.plane.speed)}", True, (255, 255, 255))
        self.text_surface3 = font.render(f"Power: {self.plane.power}%", True, (255, 255, 255))
        self.text_surface4 = font.render(f"Left to go: {int((self.shpare.rect.x + 39000 + (40000 * (physics.laps - self.laps_gone))) / 100)}м", True, (255, 255, 255))
        self.shparet.reset()
        self.shpare.reset()
        for e in event.get():
            if e.type == QUIT:
                self.game = False
                self.crashed = True
        amamama = 1
        for i in self.scene:
            if amamama > 4:
                i.reset()
            amamama += 1
        if self.laps_gone < 2:
            self.a_airport.reset()
        self.plane.reset()
        if self.shpare.rect.x + 40000 < 100:
            self.laps_gone += 1
            for i in self.scene:
                i.move_forward(-40000)
        self.window.blit(physics.text_surface, (10, 10))
        self.window.blit(physics.text_surface2, (10, 46))
        self.window.blit(physics.text_surface3, (10, 82))
        self.window.blit(physics.text_surface4, (450, 10))
        if self.laps_gone >= self.laps:
            self.b_airport.reset()
    def create_mountain(self):
        height = randint(500,1000)
        width = randint(100,2000)
        x = 0
        if self.filled < 15000:
            x = self.filled + 10000
            self.filled += width
        elif self.filled >= 15000:
            self.fully_filled = True
        elif 15000 - self.filled < 3000:
            width = 15000-self.filled
            x = self.filled + 10000
            self.filled += width
        y = -height + 500
        if x > 0:
            self.scene.append(Scene("Mountain.png",x,y,0,width,height))
    


class Scene(sprite.Sprite):
    def __init__(self, image_path, x, y, speed, height, width):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (height, width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.images = image_path

    def reset(self):
        physics.window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_forward(self, px):
        self.rect.x -= px
        
    def move_up(self,px):
        self.rect.y += px
        
class Game(sprite.Sprite):
    def __init__(self, image_path, x, y, height, width):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (height, width))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))
mama = False

class Plane(sprite.Sprite):
    def __init__(self, image_path, x, y, height, width, max_speed,stall_speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (height, width))
        self.original_image = transform.scale(image.load(image_path), (height, width))
        self.rect = self.image.get_rect()
        self.speed = 0
        self.y_speed = 0
        self.x_speed = 0
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.width = width
        self.angle = 0
        self.engine_working = False
        self.power = 0
        self.max_speed = max_speed
        self.stall_speed = stall_speed

    def toggle_engine(self):
        if not self.engine_working and physics.timer > 5:
            self.original_image = transform.scale(image.load(physics.p_working), (self.height, self.width))
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.engine_working = True
            physics.timer = 0
        elif physics.timer > 5:
            self.original_image = transform.scale(image.load(physics.p), (self.height, self.width))
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.engine_working = False
            self.power = 0
            physics.timer = 0
    def reset(self):
        global physics
        
        keys_pressed = pygame.key.get_pressed()


        if keys_pressed[pygame.K_w]:
            self.rotate(physics.index * self.speed)
        elif keys_pressed[pygame.K_s]:
            self.rotate(-(physics.index * self.speed))

        if keys_pressed[pygame.K_e]:
            self.toggle_engine()


        if keys_pressed[pygame.K_d]:
            if self.power < 100 and self.engine_working:
                self.power += 2

        if keys_pressed[pygame.K_a]:
            if self.power > 0:
                self.power -= 2

        if keys_pressed[pygame.K_a] and pygame.sprite.collide_rect(self, physics.shpare) and self.speed > 0:
            self.speed -= 0.5
            if self.speed < 0:
                self.speed = 0  

        umymumymu = 1
        for i in physics.scene:
            if umymumymu > 4:
                if pygame.sprite.collide_rect(self,i):
                    physics.crashed = True
            umymumymu += 1

        if pygame.sprite.collide_rect(self, physics.b_airport) and self.speed <= 0:
            physics.ended = True

        physics.window.blit(self.image, (self.rect.x, self.rect.y))

        if self.speed < self.stall_speed and not pygame.sprite.collide_rect(self, physics.shpare):
            self.y_speed -= (self.stall_speed + 0.5 - self.speed) / 5000000
        if not pygame.sprite.collide_rect(self, physics.shpare):
            if not self.speed < self.stall_speed + 1:
                if self.angle / 90 > 1:
                    self.y_speed = self.max_speed - (self.angle / 90 - 1) * self.speed
                elif self.angle / 90 > 2:
                    self.y_speed = (self.max_speed * 2) - (self.angle / 90 - 2) * self.speed
                else:
                    self.y_speed = (self.angle / 90) * self.speed

        else:
            self.y_speed = 0

        if self.engine_working:
            if self.speed < self.max_speed + 0.1:
                self.speed += 0.3 * self.power / 100
        if self.speed > 0:
            self.speed -= 0.2

        if self.angle > 90:
            self.x_speed = 0 - self.speed + self.y_speed


        else:
            self.x_speed = self.speed - self.y_speed
        if self.angle > 15:
            if self.speed > 2:
                self.speed -= (self.angle - 40) * 0.01
        

        amama = 0

        for i in physics.scene:
            i.move_forward(self.x_speed)
            i.move_up(self.y_speed)
            amama += 1
            
        if self.y_speed < -3 and pygame.sprite.collide_rect(self, physics.shpare):
                physics.crashed = True

        
        
    def rotate(self, angle):
        global game

        if not pygame.sprite.collide_rect(self, physics.shpare):
            self.angle += angle
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        else:
            self.angle = 0
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            if self.speed > self.stall_speed:
                for i in physics.scene:
                    i.move_up(1)
spisok = ["Frankivsk","Kolomya","Kyiv","Donetsk","Warsaw","Chisinau"]
def restart_map(location):
    if location == spisok[0]:
        bomba.pushButton.setText(f"{spisok[0]} (You are here)")
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        bomba.label_3.setText(f"Money: {money}")
        return 1
    if location == spisok[1]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(f"{spisok[1]} (You are here)")
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        bomba.label_3.setText(f"Money: {money}")
        return 2
    if location == spisok[2]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(f"{spisok[2]} (You are here)")
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        bomba.label_3.setText(f"Money: {money}")
        return 3
    if location == spisok[3]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(f"{spisok[3]} (You are here)")
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(spisok[5])
        bomba.label_3.setText(f"Money: {money}")
        return 4
    if location == spisok[4]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(f"{spisok[4]} (You are here)")
        bomba.pushButton_6.setText(spisok[5])
        bomba.label_3.setText(f"Money: {money}")
        return 5
    if location == spisok[5]:
        bomba.pushButton.setText(spisok[0])
        bomba.pushButton_2.setText(spisok[1])
        bomba.pushButton_3.setText(spisok[2])
        bomba.pushButton_4.setText(spisok[3])
        bomba.pushButton_5.setText(spisok[4])
        bomba.pushButton_6.setText(f"{spisok[5]} (You are here)")
        bomba.label_3.setText(f"Money: {money}")
        return 6
        
        
def gaming(stopped_p, working_p, width, height, max_speed, stall_speed, rotating_index, a_airport, b_airport, given_money, laps):
    global physics
    global money
    global whereyouat
    global theme
    clock = time.Clock()
    pygame.init()
    windows.hide()
    physics = Physics(stopped_p, working_p, width, height, max_speed, stall_speed, rotating_index, a_airport + ".png", b_airport + ".png", laps)
    physics.start()
    theme.stop()
    game = True
    while game:
        physics.playing()
        display.update()
        clock.tick(60)
        if physics.crashed:
            game = False
            money -= given_money / 2
            restart_map(whereyouat)
        elif physics.ended:
            game = False
            money += given_money
            whereyouat = b_airport
            restart_map(whereyouat)

    pygame.quit() 
    physics = None
    pygame.init()
    windows.show()
    pygame.mixer.init()
    theme.play()

def frankivsk():
    laps = "а"
    if restart_map(whereyouat) == 2:
        given_money = planes[aircraft_chosen][7] * 100
        laps = 2
    elif restart_map(whereyouat) == 3:
        given_money = planes[aircraft_chosen][7] * 1000
        laps = 10
    if not laps == "а":
        gaming(planes[aircraft_chosen][0], planes[aircraft_chosen][1],planes[aircraft_chosen][2],planes[aircraft_chosen][3],planes[aircraft_chosen][4],planes[aircraft_chosen][5],planes[aircraft_chosen][6],spisok[restart_map(whereyouat) - 1], "Frankivsk", given_money,laps)

def kolomya():
    if restart_map(whereyouat) == 1:
        gaming(planes[aircraft_chosen][0], planes[aircraft_chosen][1],planes[aircraft_chosen][2],planes[aircraft_chosen][3],planes[aircraft_chosen][4],planes[aircraft_chosen][5],planes[aircraft_chosen][6],spisok[restart_map(whereyouat) - 1], "Kolomya", 2000 ,2)

def kyiv():
    laps = "а"
    if restart_map(whereyouat) == 4:
        given_money = planes[aircraft_chosen][7] * 1000
        laps = 8
    elif restart_map(whereyouat) == 1:
        given_money = planes[aircraft_chosen][7] * 1000
        laps = 10
    elif restart_map(whereyouat) == 5 and licenses:
        given_money = planes[aircraft_chosen][7] * 2500
        laps = 12
    elif restart_map(whereyouat) == 6 and licenses:
        given_money = planes[aircraft_chosen][7] * 2000
        laps = 8
    if not laps == "а":
        gaming(planes[aircraft_chosen][0], planes[aircraft_chosen][1],planes[aircraft_chosen][2],planes[aircraft_chosen][3],planes[aircraft_chosen][4],planes[aircraft_chosen][5],planes[aircraft_chosen][6],spisok[restart_map(whereyouat) - 1], "Frankivsk", given_money,laps)

def donetsk():
    laps = "а"
    if restart_map(whereyouat) == 3:
        given_money = planes[aircraft_chosen][7] * 1000
        laps = 8
    elif restart_map(whereyouat) == 6:
        given_money = planes[aircraft_chosen][7] * 3250
        laps = 15
    
    if not laps == "а":
        gaming(planes[aircraft_chosen][0], planes[aircraft_chosen][1],planes[aircraft_chosen][2],planes[aircraft_chosen][3],planes[aircraft_chosen][4],planes[aircraft_chosen][5],planes[aircraft_chosen][6],spisok[restart_map(whereyouat) - 1], "Frankivsk", given_money,laps)

def warsaw():
    laps = "а"
    if restart_map(whereyouat) == 3:
        given_money = 250
        laps = 12
    if not laps == "а":
        if licenses:
            gaming(planes[aircraft_chosen][0], planes[aircraft_chosen][1],planes[aircraft_chosen][2],planes[aircraft_chosen][3],planes[aircraft_chosen][4],planes[aircraft_chosen][5],planes[aircraft_chosen][6],spisok[restart_map(whereyouat) - 1], "Frankivsk", given_money,laps)
        else:
            bomba.label_2.show()


def chisinau():
    laps = "а"
    if restart_map(whereyouat) == 4:
        given_money = planes[aircraft_chosen][7] * 3500
        laps = 15
    elif restart_map(whereyouat) == 3:
        given_money = planes[aircraft_chosen][7] * 2000
        laps = 8
    if not laps == "а":
        if licenses:
            gaming(planes[aircraft_chosen][0], planes[aircraft_chosen][1],planes[aircraft_chosen][2],planes[aircraft_chosen][3],planes[aircraft_chosen][4],planes[aircraft_chosen][5],planes[aircraft_chosen][6],spisok[restart_map(whereyouat) - 1], "Frankivsk", given_money,laps)
        else:
            bomba.label_2.show()
            


def closeEvent(event):
    global game
    game = False
planes = {
    "Censa":["Censa - 125 (Stopped).png","Censa - 125 (Working).png", 100,33,25,5,0.01,20],
    "A230":["A230.png","A230.png", 333,133,60,10,0.005,120],
    "B474":["B474.png","B474.png", 600,200,70,15,0.0025,330]
    
    
}

def posholko():
    global money
    money += 7000
    restart_map(whereyouat)
def window_reset():
    if A230:
        if aircraft_chosen == "A230":
            bomba2.pushButton_2.setText("AirShip A230 (Chosen)")
        else:
            bomba2.pushButton_2.setText("AirShip A230 (Bought)")
    else:
        bomba2.pushButton_2.setText("AirShip A230 (10.000$)")
    if B474:
        if aircraft_chosen == "B474":
            bomba2.pushButton_3.setText("Bang 474 (Chosen)")
        else:
            bomba2.pushButton_3.setText("Bang 474 (Bought)")
    else:
        bomba2.pushButton_3.setText("Bang 474 (100.000$)")
    if licenses:
        bomba2.pushButton_4.setText("Abroad License (Bought)")
    else:
        bomba2.pushButton_4.setText("Abroad License (20.000$)")
    if aircraft_chosen == "Censa":
        bomba2.pushButton.setText("Censa 125 (Chosen)")
    else:
        bomba2.pushButton.setText("Censa 125 (Bought)")
        
def bong():
    global money
    global B474
    global aircraft_chosen
    if not B474:
        if money > 99999:
            B474 = True
    elif not aircraft_chosen == "B474":
        aircraft_chosen = "B474"
        money -= 100000
    restart_map(whereyouat)
    window_reset()
    
def airship():
    global money
    global A230
    global aircraft_chosen
    if not A230:
        if money > 9999:
            A230 = True
            money -= 10000
    elif not aircraft_chosen == "A230":
        aircraft_chosen = "A230"
        money -= 10000
    restart_map(whereyouat)
    window_reset()

def censa():
    global money
    global aircraft_chosen
    if not aircraft_chosen == "Censa":
        aircraft_chosen = "Censa"
    restart_map(whereyouat)
    window_reset()
        
def license():
    global money
    global licenses
    if not licenses:
        if money > 19999:
            licenses = True
            money -= 20000
    restart_map(whereyouat)
    window_reset()
            
def shop():
    window2.show()

money = 1000
licenses = False
pygame.font.init()
font = pygame.font.Font(None, 36)
pygame.init()
whereyouat = "Donetsks"
aircraft_chosen = "Censa"
A230 = False
B474 = False
clock = pygame.time.Clock()
pygame.mixer.init()
theme = pygame.mixer.Sound("theme.mp3")
theme.set_volume(10)
theme.play()
FPS = 60
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows= QtWidgets.QMainWindow()
    window2 = QtWidgets.QWidget()
    bomba2 = Ui_Form()
    bomba = Ui_MainWindow()
    bomba.setupUi(windows)
    bomba2.setupUi(window2)
    bomba.pushButton.released.connect(frankivsk)
    bomba.pushButton_2.released.connect(kolomya)
    bomba.pushButton_3.released.connect(kyiv)
    bomba.pushButton_4.released.connect(donetsk)
    bomba.pushButton_5.released.connect(warsaw)
    bomba.pushButton_6.released.connect(chisinau)
    bomba.pushButton_7.released.connect(shop)
    bomba.pushButton_8.released.connect(posholko)
    bomba2.pushButton_2.released.connect(airship)
    bomba2.pushButton_3.released.connect(bong)
    bomba2.pushButton_4.released.connect(license)
    window_reset()
    bomba.label_2.hide()
    restart_map(whereyouat)
    windows.show()
    sys.exit(app.exec_())
pygame.quit()