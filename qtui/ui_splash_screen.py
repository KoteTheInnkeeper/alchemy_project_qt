# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenEhjRfV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(489, 270)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.v_central_widget_layout = QVBoxLayout(self.central_widget)
        self.v_central_widget_layout.setObjectName(u"v_central_widget_layout")
        self.splash_main_frame = QFrame(self.central_widget)
        self.splash_main_frame.setObjectName(u"splash_main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splash_main_frame.sizePolicy().hasHeightForWidth())
        self.splash_main_frame.setSizePolicy(sizePolicy1)
        self.splash_main_frame.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color: rgb(32, 37, 47);\n"
"	border-radius: 15px;\n"
"	color:rgb(193, 13, 31)\n"
"\n"
"}\n"
"\n"
"#splash_subtitle_label {\n"
"\n"
"color: rgb(191, 191, 191)\n"
"\n"
"}")
        self.splash_main_frame.setFrameShape(QFrame.StyledPanel)
        self.splash_main_frame.setFrameShadow(QFrame.Raised)
        self.splash_title_label = QLabel(self.splash_main_frame)
        self.splash_title_label.setObjectName(u"splash_title_label")
        self.splash_title_label.setGeometry(QRect(6, 30, 451, 51))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splash_title_label.sizePolicy().hasHeightForWidth())
        self.splash_title_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(25)
        self.splash_title_label.setFont(font)
        self.splash_title_label.setAlignment(Qt.AlignCenter)
        self.splash_subtitle_label = QLabel(self.splash_main_frame)
        self.splash_subtitle_label.setObjectName(u"splash_subtitle_label")
        self.splash_subtitle_label.setGeometry(QRect(0, 80, 471, 21))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.splash_subtitle_label.sizePolicy().hasHeightForWidth())
        self.splash_subtitle_label.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setItalic(True)
        self.splash_subtitle_label.setFont(font1)
        self.splash_subtitle_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.progress_bar = QProgressBar(self.splash_main_frame)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(50, 160, 361, 23))
        self.progress_bar.setStyleSheet(u"QProgressBar {\n"
"\n"
"	background-color: rgb(117, 136, 172);\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	border-style: none;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"\n"
"	border-radius: 10px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0.551, x2:1, y2:0.517, stop:0 rgba(235, 119, 121, 255), stop:1 rgba(170, 0, 0, 255));\n"
"\n"
"}")
        self.status_label = QLabel(self.splash_main_frame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(0, 190, 461, 21))
        sizePolicy3.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setItalic(False)
        self.status_label.setFont(font2)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.credits_label = QLabel(self.splash_main_frame)
        self.credits_label.setObjectName(u"credits_label")
        self.credits_label.setGeometry(QRect(260, 230, 191, 21))
        sizePolicy3.setHeightForWidth(self.credits_label.sizePolicy().hasHeightForWidth())
        self.credits_label.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setItalic(False)
        self.credits_label.setFont(font3)
        self.credits_label.setText(u"<strong>Created by:</strong> KoteTheInnkeeper")
        self.credits_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.v_central_widget_layout.addWidget(self.splash_main_frame)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.splash_title_label.setText(QCoreApplication.translate("MainWindow", u"<strong>Skyrim</strong> Alchemy Project", None))
        self.splash_subtitle_label.setText(QCoreApplication.translate("MainWindow", u"The unfunny perk tree made easier", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
    # retranslateUi

