import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton

# 화면을 띄우는데 사용되는 Class 선언
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI를 초기화하기 위한 메서드
    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.fruits = ["사과", "배", "감자", "딸기"]

        for fruit in self.fruits:
            checkbox = QCheckBox(fruit, self)
            vbox.addWidget(checkbox)

        button = QPushButton("확인", self)
        button.clicked.connect(self.showSelectedFruits)
        vbox.addWidget(button)

        button2 = QPushButton("취소", self)
        vbox.addWidget(button2)


        self.setWindowTitle("과일 선택")
        self.setGeometry(500, 500, 400, 300)
        self.show()

    def showSelectedFruits(self):
        selected_fruits = []
        for index in range(len(self.fruits)):
            checkbox = self.layout().itemAt(index).widget()
            if checkbox.isChecked():
                selected_fruits.append(self.fruits[index])
        print("선택한 과일:", ", ".join(selected_fruits))

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = MyApp() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
