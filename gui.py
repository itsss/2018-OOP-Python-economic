from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
import socket
from threading import Thread

loc = 0  # 이미지 보이는 위치 확인용

# 접속하고자 하는 서버의 주소 및 포트 기술
server_ip = '127.0.0.1'
server_port = 60043
address = (server_ip, server_port)

# socket을 이용해서 접속 할 준비
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

item2 = [5,5,5,5,5,5,5,5]

# 서버에 접속을 시도
try:
    mysock.connect(address)

# 만약, 서버에 접속이 어려울 경우
except ConnectionRefusedError:
    print('서버 상태를 확인하십시오.')
    exit()

# any 문서에 대한 정보를 담는 배열 및 ListView 정보를 담는 배열
Model = QStandardItemModel()
pic_a = []
pic_b = []
pic_c = []

class Ui_MainWindow(QMainWindow, object):
    '''
    GUI MainWindow 클래스
    '''

    def setupUi(self, MainWindow):
        '''
        UI Setup 클래스
        :param MainWindow:
        :return:
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(380, 41, 231, 411))
        self.listView_2.setObjectName("listView_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 10, 111, 16))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 351, 261))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 10, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 420, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 330, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 360, 41, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 390, 51, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 420, 51, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 330, 31, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 330, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 360, 31, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 360, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 390, 31, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 390, 31, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 420, 31, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 420, 31, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 330, 31, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(300, 330, 31, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(260, 360, 31, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(300, 360, 31, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 390, 31, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(300, 390, 31, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(260, 420, 31, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(300, 420, 31, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 310, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(120, 310, 31, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(260, 310, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(300, 310, 31, 16))
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 450, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btn_choice_clicked)

        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(90, 10, 271, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 351, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 351, 251))
        self.label_15.setObjectName("label_15")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.btn_left_clicked)  # 왼쪽, 오른쪽 버튼 클릭
        self.pushButton_2.clicked.connect(self.btn_right_clicked)

        pixmap = QPixmap('image/example.png') # 이미지 구현
        pixmap = pixmap.scaled(351, 251)
        self.label_15.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.lineEdit_17.setText("데이터 전송 대기 중입니다.")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''
        GUI에 들어가는 여러 아이템의 텍스트 설정 함수
        :param MainWindow:
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EconomicGame"))
        self.label_2.setText(_translate("MainWindow", "Status"))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "커피"))
        self.label_4.setText(_translate("MainWindow", "밀가루"))
        self.label_5.setText(_translate("MainWindow", "희토류"))
        self.label_6.setText(_translate("MainWindow", "석유"))
        self.label_7.setText(_translate("MainWindow", "소고기"))
        self.label_8.setText(_translate("MainWindow", "시멘트"))
        self.label_9.setText(_translate("MainWindow", "알루미늄"))
        self.label_10.setText(_translate("MainWindow", "강철"))
        self.label_11.setText(_translate("MainWindow", "사기"))
        self.label_12.setText(_translate("MainWindow", "팔기"))
        self.label_13.setText(_translate("MainWindow", "사기"))
        self.label_14.setText(_translate("MainWindow", "팔기"))

        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.lineEdit_4.setText(_translate("MainWindow", "0"))
        self.lineEdit_5.setText(_translate("MainWindow", "0"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.lineEdit_10.setText(_translate("MainWindow", "0"))
        self.lineEdit_11.setText(_translate("MainWindow", "0"))
        self.lineEdit_12.setText(_translate("MainWindow", "0"))
        self.lineEdit_13.setText(_translate("MainWindow", "0"))
        self.lineEdit_14.setText(_translate("MainWindow", "0"))
        self.lineEdit_15.setText(_translate("MainWindow", "0"))
        self.lineEdit_16.setText(_translate("MainWindow", "0"))

        self.pushButton_3.setText(_translate("MainWindow", "결정"))

    def receive(self):
        '''
            메시지를 받는 형식

            [게임 시작 전]
            플레이어 들어오고 나가는 정보,
            PLAYER_JOIN|1
            PLAYER_QUIT|1

            플레이어가 전부 들어가면 시작한다는 메시지
            그냥 텍스트로 보내기 (Status 창에 띄움)

            [게임 중]
            1. 표시할 그림 정보 11, 21, 31 등으로…
            DATA|11/22/33/44...

            2. 현재 시세표 보여주기 (밀가루 5만원 등)
            PRICE|10/9/…

            3. 각 턴마다 아이템의 가격(변동된 시세) 및 플레이어별 서로의 손익 정보
            PL|10/-10

            [게임 종료 후]
            누적 수익이 가장 높은 사람 및 순위 출력
            END|10/20/30

        '''
        global mysock, Model, pic_a, pic_b, pic_c, item2

        while True:
            try:
                re = mysock.recv(1024)
                data = re.decode('UTF-8')
                # print(data)

            # 오류수정 ref: https://github.com/kadragon/oop_python_ex/blob/master/study_ex/16_socket/1603_socket_client.py

            except ConnectionError:
                print("서버와 접속이 끊겼습니다. Enter를 누르세요.")
                break
            except OSError:
                print("서버와의 접속을 끊었습니다.")
                break

            if not data:  # 넘어온 데이터가 없다면.. 로그아웃!
                print("서버로부터 정상적으로 로그아웃했습니다.")
                break

            if data[:11] == 'PLAYER_JOIN':  # 게임 시작 전, 플레이어가 들어오는 경우
                data2 = str(data[12] + '이 입장하였습니다.')
                Model.appendRow(QStandardItem(data2))
                self.listView_2.setModel(Model)

            elif data[:11] == 'PLAYER_QUIT':  # 게임 시작 전, 플레이어가 나가는 경우
                data2 = str(data[12] + '이 퇴장하였습니다.')
                Model.appendRow(QStandardItem(data2))
                self.listView_2.setModel(Model)

            elif data[:4] == 'DATA':  # 이미지 데이터가 들어오는 경우 처리하는 함수
                # [11, 22, 33, 44, 55, 65, 75, 85] 형식으로 저장
                pic = list(map(int, data[5:-1].split("/")))
                pic_a, pic_b, pic_c = self.test_image_view(pic)

            elif data[:2] == 'PL':  # 플레이어별 서로의 손익 정보
                score = list(map(int, data[3:].split("/")))
                Model.appendRow(QStandardItem("=======플레이어별 손익 정보======="))
                cnt = 0
                for i in score:
                    cnt += 1
                    Model.appendRow(QStandardItem('플레이어 ' + str(cnt) + ': ' + str(i)))
                self.listView_2.setModel(Model)

            elif data[:5] == 'PRICE':  # 각 턴마다의 아이템의 가격 (현재 시세)
                price = list(map(int, data[6:-1].split("/")))
                item = ['소고기', '커피', '희토류', '밀가루', '시멘트', '알루미늄', '강철', '석유']
                Model.appendRow(QStandardItem("=======현재 시세======="))
                cnt = 0
                for i in item:
                    Model.appendRow(QStandardItem(str(i) + ': ' + str(price[cnt])))
                    cnt += 1
                self.listView_2.setModel(Model)

                # item = ['소고기', '커피', '희토류', '밀가루', '시멘트', '알루미늄', '강철', '석유']
                Model.appendRow(QStandardItem("=======현재 가지고 있는 수량======="))
                Model.appendRow(QStandardItem('커피:' + str(item2[0])))
                Model.appendRow(QStandardItem('밀가루:' + str(item2[1])))
                Model.appendRow(QStandardItem('희토류:' + str(item2[2])))
                Model.appendRow(QStandardItem('석유:' + str(item2[3])))
                Model.appendRow(QStandardItem('소고기:' + str(item2[4])))
                Model.appendRow(QStandardItem('시멘트:' + str(item2[5])))
                Model.appendRow(QStandardItem('알루미늄:' + str(item2[6])))
                Model.appendRow(QStandardItem('강철:' + str(item2[7])))

                self.listView_2.setModel(Model)

            elif data[:3] == 'END':  # 게임이 종료된 후, 누적 수익이 가장 높은 사람 및 순위 출력
                player = list(map(int, data[4:-1].split("/")))
                Model.appendRow(QStandardItem("=======게임 끝: 최종손익 정보======="))
                cnt = 0
                max = 0
                maxp = 0
                for i in player:
                    cnt += 1
                    Model.appendRow(QStandardItem('플레이어 ' + str(cnt) + ': ' + str(i)))
                    if int(i) > max:
                        max = i
                        maxp = cnt
                Model.appendRow(QStandardItem('플레이어 ' + str(maxp) + '님이 ' + str(max) + '점으로 1등입니다!'))
                self.listView_2.setModel(Model)

            else:
                Model.appendRow(QStandardItem(data))
                self.listView_2.setModel(Model)

        print('소켓의 읽기 버퍼를 닫습니다.')
        try:
            mysock.shutdown(socket.SHUT_RD)
        except OSError:
            print("읽기 버퍼를 닫기 전에 서버에서 연결이 종료되었습니다.")

    def read_price_text(self, val):
        # val: 아이템명 (beef, coffee, rare earth, etc...)
        # ref: Millstone Project (oop-project-ex)
        '''
        val 파라미터로 입력된 데이터에서 텍스트를 긁어오는 함수
        '|' 로 구분된 데이터가 리스트에 저장됨.
        :param val:
        :return:
        '''
        id = []
        description = []
        sd = []
        image = []
        f = open('./news/' + str(val), 'r', encoding="UTF-8")
        while True:
            newline = f.readline()
            if not newline:
                break
            id.append(newline.split('|')[0])
            description.append(newline.split('|')[1])
            sd.append(newline.split('|')[2])
            image.append(newline.split('|')[3])
            # coffee-1 | 브라질이 최악의 가뭄을 경험하고 있다.| 공급 | image/coffee/drought.png

        return id, description, sd, image

    def test_image_view(self, srv_val):
        '''
        서버에서 입력된 리스트가 함수에 입력됨,
        그럼 이 함수는 입력된 리스트의 그림 위치, 수요/공급 정보, 내용을 입력받아 반환함.
        첫 번째 이미지를 pixmap을 활용해 띄우는 역할 또한 수행함.
        :param srv_val:
        :return:
        '''
        # [11, 22, 33, 44, 51, 61, 71, 81] 형태로 이미지 번호가 리스트로 들어옴
        global loc
        a,b,c,d = self.read_price_text('any')

        test_image_link=[]
        quote = []
        supply_demand = []

        for i in range(8):  # 표시해야 하는 아이템의 개수
            for j in range(40):  # 파일에 저장되어 있는 아이템의 개수
                if int(srv_val[i]) == int(a[j]):  # 만약 찾고자 하는 이미지가 인덱스에 있다면
                    test_image_link.append(d[j])  # 문구와 이미지 location을 append함
                    quote.append(b[j])
                    supply_demand.append(c[j])

        text_img_file = test_image_link[0]  # 첫 번째 이미지를 현시해 주는 기능
        pixmap = QPixmap(text_img_file[1:-1])
        pixmap = pixmap.scaled(351, 251)
        self.label_15.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        text_img = '['+str(int(loc+1))+'/8] ' + quote[0] + '(' + supply_demand[0] + ')'

        # pixmap = QPixmap('image/beef/cow_price_increase.png')
        self.lineEdit_17.setText(text_img)

        return test_image_link, quote, supply_demand


    def btn_left_clicked(self):
        '''
        왼쪽 버튼을 눌렀을 때, 이전 이미지로 바꾸는 함수
        :return:
        '''
        global loc
        loc -= 1
        print('<<<', loc)
        if loc < 0:  # 0 밑으로 데이터가 없으므로, 데이터가 없다는 메시지를 출력
            QMessageBox.about(self, "Economic", "데이터가 없습니다.")
            loc += 1

        else:
            text_img_file = pic_a[loc]  # 이전 이미지를 현시해 주는 기능
            print(text_img_file[1:-1])
            pixmap2 = QPixmap(text_img_file[1:-1])
            pixmap2 = pixmap2.scaled(351, 251)
            self.label_15.setPixmap(pixmap2)
            self.resize(pixmap2.width(), pixmap2.height())
            text_img = '[' + str(int(loc + 1)) + '/8] ' + pic_b[loc] + '(' + pic_c[loc] + ')'
            QMessageBox.about(self, "Economic", "전체 8개 그림 중 " + str(int(loc + 1)) + " 번째 그림")

            # pixmap = QPixmap('image/beef/cow_price_increase.png')
            self.lineEdit_17.setText(text_img)

    def btn_right_clicked(self):
        '''
        오른쪽 버튼을 눌렀을 때, 다음 이미지로 바꾸는 함수
        :return:
        '''
        global loc
        loc += 1
        print('>>>', loc)
        print(pic_a)
        print(pic_b)
        print(pic_c)
        if loc >= 8:  # 8 이상으로 데이터가 없으므로, 데이터가 없다는 메시지를 출력
            QMessageBox.about(self, "Economic", "데이터가 없습니다.")
            loc -= 1

        else:
            text_img_file = pic_a[loc]  # 다음 이미지를 현시해 주는 기능
            print(text_img_file[1:-1])
            pixmap2 = QPixmap(text_img_file[1:-1])
            pixmap2 = pixmap2.scaled(351, 251)
            self.label_15.setPixmap(pixmap2)
            self.resize(pixmap2.width(), pixmap2.height())
            text_img = '[' + str(int(loc + 1)) + '/8] ' + pic_b[loc] + '(' + pic_c[loc] + ')'
            QMessageBox.about(self, "Economic", "전체 8개 그림 중 "+str(int(loc+1)) + " 번째 그림")

            self.lineEdit_17.setText(text_img)

    def btn_choice_clicked(self):
        global item
        '''
        사용자가 결정 버튼을 눌렀을 때, 서버에 플레이어가 사고판 내역을 전송함.
        :return:
        '''
        try:
            buy = int(
                int(self.lineEdit.text()) + int(self.lineEdit_3.text()) + int(self.lineEdit_5.text()) + int(self.lineEdit_7.text()) + int(self.lineEdit_9.text()) + int(self.lineEdit_11.text()) + int(self.lineEdit_13.text()) + int(self.lineEdit_15.text()))
            sale = int(
                int(self.lineEdit_2.text()) + int(self.lineEdit_4.text()) + int(self.lineEdit_6.text()) + int(self.lineEdit_8.text()) + int(self.lineEdit_10.text()) + int(self.lineEdit_12.text()) + int(self.lineEdit_14.text()) + int(self.lineEdit_16.text()))

        except ValueError:
            QMessageBox.about(self, "Economic", "0~10 범위 내로 값을 올바르게 입력하였는지 다시 확인해 주시기 바랍니다.")

        '''
        5개 초과 사기, 10개 초과 팔기
        음수 데이터, 정수가 아닌 데이터 입력 방지 코드
        '''

        if buy > 5:
            QMessageBox.about(self, "Economic", "5개 초과로 살 수 없습니다.")

        elif sale > 10:
            QMessageBox.about(self, "Economic", "10개 초과로 팔 수 없습니다.")

        else:
            if (int(self.lineEdit.text()) < 0 or int(self.lineEdit_3.text()) < 0 or int(
                    self.lineEdit_5.text()) < 0 or int(self.lineEdit_7.text()) < 0 or int(
                    self.lineEdit_9.text()) < 0 or int(self.lineEdit_11.text()) < 0 or int(
                    self.lineEdit_13.text()) < 0 or int(self.lineEdit_15.text()) < 0) \
                    or (int(self.lineEdit_2.text()) < 0 or int(self.lineEdit_4.text()) < 0 or int(
                        self.lineEdit_6.text()) < 0 or int(self.lineEdit_8.text()) < 0 or int(
                        self.lineEdit_10.text()) < 0 or int(self.lineEdit_12.text()) < 0 or int(
                        self.lineEdit_14.text()) < 0 or int(self.lineEdit_16.text()) < 0):
                QMessageBox.about(self, "Economic", "0~10 범위 내로 값을 올바르게 입력하였는지 다시 확인해 주시기 바랍니다.")

            elif item2[0] < int(self.lineEdit_2.text()) or item2[1] < int(self.lineEdit_4.text()) or item2[2] < int(self.lineEdit_6.text()) or item2[3] < int(self.lineEdit_8.text()) or item2[4] < int(self.lineEdit_10.text()) or item2[5] < int(self.lineEdit_12.text()) or item2[6] < int(self.lineEdit_14.text()) or item2[7] < int(self.lineEdit_16.text()):
                QMessageBox.about(self, "Economic", "현재 보유한 아이템보다 더 많이 팔 수 없습니다.")

            else:
                # Dict 만들어 주고 서버로 전송하는 부분 추가
                data = "SEND/" + str(self.lineEdit.text()) + ":" + str(self.lineEdit_2.text()) + "/" + str(
                    self.lineEdit_3.text()) + ":" + str(self.lineEdit_4.text()) + "/" + str(
                    self.lineEdit_5.text()) + ":" + str(self.lineEdit_6.text()) + "/" + str(
                    self.lineEdit_7.text()) + ":" + str(self.lineEdit_8.text()) + "/" + str(
                    self.lineEdit_9.text()) + ":" + str(self.lineEdit_10.text()) + "/" + str(
                    self.lineEdit_11.text()) + ":" + str(self.lineEdit_12.text()) + "/" + str(
                    self.lineEdit_13.text()) + ":" + str(self.lineEdit_14.text()) + "/" + str(
                    self.lineEdit_15.text()) + ":" + str(self.lineEdit_16.text())
                # QMessageBox.about(self, "Economic", data)
                # {'커피': 5, '밀가루': 5, '희토류': 5, '석유': 5, '소고기': 5, '시멘트': 5, '알루미늄': 5, '강철': 5}
                try:
                    mysock.send(bytes(data, 'UTF-8'))  # 서버에 메시지를 전송
                except OSError:
                    exit()


                '''
                아이템 값 갱신
                '''
                item2[0] -= int(self.lineEdit_2.text())
                item2[1] -= int(self.lineEdit_4.text())
                item2[2] -= int(self.lineEdit_6.text())
                item2[3] -= int(self.lineEdit_8.text())
                item2[4] -= int(self.lineEdit_10.text())
                item2[5] -= int(self.lineEdit_12.text())
                item2[6] -= int(self.lineEdit_14.text())
                item2[7] -= int(self.lineEdit_16.text())

                item2[0] += int(self.lineEdit.text())
                item2[1] += int(self.lineEdit_3.text())
                item2[2] += int(self.lineEdit_5.text())
                item2[3] += int(self.lineEdit_7.text())
                item2[4] += int(self.lineEdit_9.text())
                item2[5] += int(self.lineEdit_11.text())
                item2[6] += int(self.lineEdit_13.text())
                item2[7] += int(self.lineEdit_15.text())


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setMinimumSize(QSize(620, 506))
        self.setWindowTitle("Economic")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    thread_recv = Thread(target=ui.receive, args=())
    thread_recv.start()
    MainWindow.show()
    sys.exit(app.exec_())
