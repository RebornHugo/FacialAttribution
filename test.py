from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
path = "C:/"
class SelectDialog(QDialog):
    def __init__(self, parent=None):
        super(SelectDialog, self).__init__(parent)
        self.path = path
        self.filetype = None
        self.initUI()
        self.setWindowTitle("选择")
        self.resize(240, 100)
    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("路径："), 0, 0)
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.setFixedWidth(200)
        self.pathLineEdit.setText(self.path)
        grid.addWidget(self.pathLineEdit, 0, 1)
        button = QPushButton("更改")
        button.clicked.connect(self.changePath)
        grid.addWidget(button, 0, 2)

        buttonBox = QDialogButtonBox()
        buttonBox.setOrientation(Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        buttonBox.button(QDialogButtonBox.Ok).setText('选择')
        buttonBox.button(QDialogButtonBox.Cancel).setText('取消')
        grid.addWidget(buttonBox, 2, 1)
        self.setLayout(grid)

    def changePath(self):
        open = QFileDialog()
        self.path , self.filetype = open.getOpenFileName(self,self.tr("打开图片"),"C:/",self.tr("图片文件(*.png *.jpg *.bmp)"))
        print(self.path)
        #self.path = open.getExistingDirectory()
        self.pathLineEdit.setText(self.path)

