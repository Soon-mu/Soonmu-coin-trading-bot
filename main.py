import sys
from PyQt5.QtWidgets import * # PyQt5 디렉터리에 있는 Qtwidgets.py 파일로부터 모든 것을 import
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("mywindows.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Qt Designer 에서 만든 클래스들을 초기화
        self.pushButton.clicked.connect(self.inquiry)
        self.setWindowTitle("코빗 비트코인 시세 조회기")
        self.setWindowIcon(QIcon("coin.png"))


        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

    def btn_clicked(self):
        print("버튼클릭")

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
# class Mywindow(QMainWindow): #Mywindow 클래스는 QmainWindow를 상속받음
#     def __init__(self):
#         super().__init__() # super()를 통해서 부모 클래스의 초기화 함수를 호출
#                            # 부모 클래스의 초기화자를 반드시 호출할 필요는 없지만, QMainWindow 클래스는 필요하다.
#                            # PyQt 가 제공하는 클래스 상속시 부모클래스 초기화 반드시 필요함.
#         self.setGeometry(100,200,300,400) # 100 : 좌상단 x 좌표, 200 : 좌상단 y좌표(모니터 상단에서부터)
#                                           # 300 : window창 가로, 400 : window창 세로
#         self.setWindowTitle("PyQt")             #윈도우 타이틀 이름
#         self.setWindowIcon(QIcon("coin.png"))   #윈도우 타이틀 왼쪽 아이콘
#
#         btn = QPushButton("버튼1", self)
#         btn.move(10,10)
#         btn.clicked.connect(self.btn_clicked)
#
#         btn2 = QPushButton("버튼2", self)
#         btn2.move(10, 40)
#         btn2.clicked.connect(self.btn_clicked)
#
#     def btn_clicked(Self):
#         print("버튼클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
# #label = QLabel("hello")
# #label.show()
# btn = QPushButton("Hello")
# btn.show()
#
# app.exec_()
