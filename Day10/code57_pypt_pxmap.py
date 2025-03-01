# 이미지처리 위젯
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap(800, 600)
        pixmap.load('./Day10/cat.png')
        

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter) # Qt.AlignCenter 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)

        self.setLayout(vbox)

        

        # 필수설정
        self.setWindowTitle('이미지 위젯')
        # self.setGeometry(300, 300, 300 ,300)
        self.showFullScreen() # self.show()

    def onChanged(self, text):
        self.lblResult.setText('입력값 : ' + text)
        self.lblResult.adjustSize() # 라벨사이즈 자동


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
