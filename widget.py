# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\clive\Desktop\人脸识别\2\widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets, QtGui, QtCore
import test


class Ui_Widget(object):
    def setupUi(self, Widget):
        self.path = None
        Widget.setObjectName("Widget")
        Widget.resize(1142, 497)
        Widget.setStyleSheet("background-color: rgb(204,204,204);")
        self.pushButton_3 = QtWidgets.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 340, 141, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            "QPushButton { color: rgb(255, 255, 255);background-color: rgb(0, 0, 0); border-radius: 3px; } QPushButton:hover { color: rgb(0, 0, 0);background-color: rgb(255, 255, 255); }\n"
            "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(Widget)
        self.label_9.setGeometry(QtCore.QRect(690, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(690, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(410, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(690, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(690, 330, 101, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(90, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(820, 390, 231, 51))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(700, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(720, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_4.setGeometry(QtCore.QRect(820, 210, 231, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_6.setGeometry(QtCore.QRect(820, 330, 231, 51))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_5.setGeometry(QtCore.QRect(820, 270, 231, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton_4 = QtWidgets.QPushButton(Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 340, 141, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            "QPushButton { color: rgb(255, 255, 255);background-color: rgb(0, 0, 0); border-radius: 3px; } QPushButton:hover { color: rgb(0, 0, 0);background-color: rgb(255, 255, 255); }\n"
            "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(820, 90, 231, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(Widget)
        self.textBrowser.setGeometry(QtCore.QRect(820, 30, 231, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Widget)
        self.textBrowser_3.setGeometry(QtCore.QRect(820, 150, 231, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(720, 90, 71, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.graphicsView = QtWidgets.QGraphicsView(Widget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 60, 256, 256))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Widget)
        self.graphicsView_2.setGeometry(QtCore.QRect(330, 60, 256, 256))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(10, 470, 71, 20))
        self.widget.setObjectName("widget")
        self.pushButton_3.raise_()
        self.label_9.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.textBrowser_7.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.textBrowser_4.raise_()
        self.textBrowser_6.raise_()
        self.textBrowser_5.raise_()
        self.pushButton_4.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.label_4.raise_()
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.widget.raise_()

        self.retranslateUi(Widget)
        self.pushButton_4.clicked.connect(self.testDialog)
        self.pushButton_3.clicked.connect(self.processDialog)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def testDialog(self):
        #    app = QApplication(sys.argv)
        dialog = test.SelectDialog()
        dialog.exec_()
        if dialog.path is not test.path or None:
            self.path = dialog.path
            self.label.setVisible(False)
            #                pic = QtGui.QPixmap()
            #                pic.load(dialog.path)
            scene = QtWidgets.QGraphicsScene()
            #        scene.setSceneRect(-600, -600, 1200, 1200)
            pic = QtGui.QPixmap(dialog.path).scaled(252, 252)
            scene.addItem(QtWidgets.QGraphicsPixmapItem(pic))
            view = self.graphicsView
            view.setScene(scene)
            view.setRenderHint(QtGui.QPainter.Antialiasing)
            view.show()

        return

    def processDialog(self):
        import os
        res = os.popen('python guess.py --model_type inception --model_dir '
                       '/home/hugo/Coding/WorkSpace/rude-carnie/Module/22801 '
                       '--filename %s --device_id /gpu:0' % self.path).readlines()
        print(res[-1])
        print(type(res[-1]))
        self.textBrowser_2.setText(res[-1])
        res = os.popen('python guess.py --class_type gender --model_type inception --model_dir '
                       '/home/hugo/Coding/WorkSpace/rude-carnie/Module/21936 '
                       '--filename %s --device_id /gpu:0  --face_detection_model '
                       '/home/hugo/Coding/python/Anaconda/ENTER/envs/tf2/share/'
                       'OpenCV/haarcascades/haarcascade_frontalface_default.xml '
                       % self.path).readlines()
        print(res[-1])
        print(type(res[-1]))
        self.textBrowser.setText(res[-1])
        self.textBrowser_3.setText('Y')
        self.textBrowser_4.setText('N')
        self.textBrowser_5.setText('N')
        self.textBrowser_6.setText('N')
        self.textBrowser_7.setText('Y')

        add = '/home/hugo/Coding/WorkSpace/FacialAttribution/frontal-face.jpg'
        self.label_2.setVisible(False)
        scene_2 = QtWidgets.QGraphicsScene()
        pic_2 = QtGui.QPixmap(add).scaled(252, 252)
        scene_2.addItem(QtWidgets.QGraphicsPixmapItem(pic_2))
        view_2 = self.graphicsView_2
        view_2.setScene(scene_2)
        view_2.setRenderHint(QtGui.QPainter.Antialiasing)
        view_2.show()
        return

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "人脸特征鉴定系统"))
        self.pushButton_3.setText(_translate("Widget", "开始鉴定"))
        self.label_9.setText(_translate("Widget", "是否有胡子"))
        self.label_5.setText(_translate("Widget", "是否戴帽子"))
        self.label_2.setText(_translate("Widget", "鉴定结果"))
        self.label_8.setText(_translate("Widget", "是否黑头发"))
        self.label_6.setText(_translate("Widget", "是否带眼镜"))
        self.label.setText(_translate("Widget", "请添加图片"))
        self.label_7.setText(_translate("Widget", "是否微笑"))
        self.label_3.setText(_translate("Widget", "性别"))
        self.pushButton_4.setText(_translate("Widget", "图片位置"))
        self.label_4.setText(_translate("Widget", "年龄"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
