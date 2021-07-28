# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowZyxRiY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 628)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"#top_bar_title_frame, #left_menu_background_frame {\n"
"\n"
"background-color: rgb(46, 47, 63);\n"
"\n"
"}\n"
"\n"
"#content_frame {\n"
"\n"
"background-color: rgb(74, 76, 102)\n"
"\n"
"}")
        self.v_centralwidget_layout = QVBoxLayout(self.centralwidget)
        self.v_centralwidget_layout.setSpacing(0)
        self.v_centralwidget_layout.setObjectName(u"v_centralwidget_layout")
        self.v_centralwidget_layout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_frame = QFrame(self.centralwidget)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_bar_frame.sizePolicy().hasHeightForWidth())
        self.top_bar_frame.setSizePolicy(sizePolicy1)
        self.top_bar_frame.setMinimumSize(QSize(0, 50))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 50))
        self.top_bar_frame.setFrameShape(QFrame.NoFrame)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.h_top_bar_frame_layout = QHBoxLayout(self.top_bar_frame)
        self.h_top_bar_frame_layout.setSpacing(0)
        self.h_top_bar_frame_layout.setObjectName(u"h_top_bar_frame_layout")
        self.h_top_bar_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame = QFrame(self.top_bar_frame)
        self.toggle_frame.setObjectName(u"toggle_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggle_frame.sizePolicy().hasHeightForWidth())
        self.toggle_frame.setSizePolicy(sizePolicy2)
        self.toggle_frame.setMinimumSize(QSize(70, 0))
        self.toggle_frame.setMaximumSize(QSize(70, 16777215))
        self.toggle_frame.setStyleSheet(u"background-color:rgb(46, 47, 63)")
        self.toggle_frame.setFrameShape(QFrame.NoFrame)
        self.toggle_frame.setFrameShadow(QFrame.Raised)
        self.v_toggle_frame_layout = QVBoxLayout(self.toggle_frame)
        self.v_toggle_frame_layout.setSpacing(0)
        self.v_toggle_frame_layout.setObjectName(u"v_toggle_frame_layout")
        self.v_toggle_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.toggle_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(70, 0))
        self.btn_toggle.setMaximumSize(QSize(70, 16777215))
        self.btn_toggle.setStyleSheet(u"QPushButton {\n"
"\n"
"color: rgb(238, 238, 238);\n"
"border: 0px solid;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"\n"
"	background-color:rgb(163, 163, 244);\n"
"	color: rgb(227, 227, 227);\n"
"}")

        self.v_toggle_frame_layout.addWidget(self.btn_toggle)


        self.h_top_bar_frame_layout.addWidget(self.toggle_frame)

        self.top_bar_title_frame = QFrame(self.top_bar_frame)
        self.top_bar_title_frame.setObjectName(u"top_bar_title_frame")
        sizePolicy.setHeightForWidth(self.top_bar_title_frame.sizePolicy().hasHeightForWidth())
        self.top_bar_title_frame.setSizePolicy(sizePolicy)
        self.top_bar_title_frame.setFrameShape(QFrame.NoFrame)
        self.top_bar_title_frame.setFrameShadow(QFrame.Raised)

        self.h_top_bar_frame_layout.addWidget(self.top_bar_title_frame)


        self.v_centralwidget_layout.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.h_content_frame_layout = QHBoxLayout(self.content_frame)
        self.h_content_frame_layout.setSpacing(0)
        self.h_content_frame_layout.setObjectName(u"h_content_frame_layout")
        self.h_content_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_background_frame = QFrame(self.content_frame)
        self.left_menu_background_frame.setObjectName(u"left_menu_background_frame")
        sizePolicy.setHeightForWidth(self.left_menu_background_frame.sizePolicy().hasHeightForWidth())
        self.left_menu_background_frame.setSizePolicy(sizePolicy)
        self.left_menu_background_frame.setMinimumSize(QSize(70, 0))
        self.left_menu_background_frame.setMaximumSize(QSize(70, 16777215))
        self.left_menu_background_frame.setStyleSheet(u"")
        self.left_menu_background_frame.setFrameShape(QFrame.NoFrame)
        self.left_menu_background_frame.setFrameShadow(QFrame.Raised)
        self.v_left_menu_background_frame_layout = QVBoxLayout(self.left_menu_background_frame)
        self.v_left_menu_background_frame_layout.setSpacing(0)
        self.v_left_menu_background_frame_layout.setObjectName(u"v_left_menu_background_frame_layout")
        self.v_left_menu_background_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_frame = QFrame(self.left_menu_background_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy3)
        self.buttons_frame.setStyleSheet(u"#buttons_frame {\n"
"\n"
"	background-color: rgb(46, 47, 63);\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"	background-color:rgb(46, 47, 63);\n"
"	color: rgb(227, 227, 227);\n"
"	border: 0px solid;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"\n"
"	background-color:rgb(153, 153, 229);\n"
"	color: rgb(227, 227, 227);\n"
"}")
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.v_buttons_frame_layout = QVBoxLayout(self.buttons_frame)
        self.v_buttons_frame_layout.setSpacing(0)
        self.v_buttons_frame_layout.setObjectName(u"v_buttons_frame_layout")
        self.v_buttons_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.recipes_btn_frame = QFrame(self.buttons_frame)
        self.recipes_btn_frame.setObjectName(u"recipes_btn_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.recipes_btn_frame.sizePolicy().hasHeightForWidth())
        self.recipes_btn_frame.setSizePolicy(sizePolicy4)
        self.recipes_btn_frame.setMinimumSize(QSize(0, 40))
        self.recipes_btn_frame.setMaximumSize(QSize(16777215, 40))
        self.recipes_btn_frame.setFrameShape(QFrame.NoFrame)
        self.recipes_btn_frame.setFrameShadow(QFrame.Raised)
        self.h_recipes_btn_frame_layout = QHBoxLayout(self.recipes_btn_frame)
        self.h_recipes_btn_frame_layout.setSpacing(5)
        self.h_recipes_btn_frame_layout.setObjectName(u"h_recipes_btn_frame_layout")
        self.h_recipes_btn_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.recipes_btn = QPushButton(self.recipes_btn_frame)
        self.recipes_btn.setObjectName(u"recipes_btn")
        sizePolicy.setHeightForWidth(self.recipes_btn.sizePolicy().hasHeightForWidth())
        self.recipes_btn.setSizePolicy(sizePolicy)
        self.recipes_btn.setMinimumSize(QSize(70, 40))
        self.recipes_btn.setMaximumSize(QSize(70, 40))
        self.recipes_btn.setText(u"recipes")

        self.h_recipes_btn_frame_layout.addWidget(self.recipes_btn)


        self.v_buttons_frame_layout.addWidget(self.recipes_btn_frame, 0, Qt.AlignHCenter)

        self.ingredients_btn_frame = QFrame(self.buttons_frame)
        self.ingredients_btn_frame.setObjectName(u"ingredients_btn_frame")
        sizePolicy4.setHeightForWidth(self.ingredients_btn_frame.sizePolicy().hasHeightForWidth())
        self.ingredients_btn_frame.setSizePolicy(sizePolicy4)
        self.ingredients_btn_frame.setMinimumSize(QSize(0, 40))
        self.ingredients_btn_frame.setMaximumSize(QSize(16777215, 40))
        self.ingredients_btn_frame.setFrameShape(QFrame.NoFrame)
        self.ingredients_btn_frame.setFrameShadow(QFrame.Raised)
        self.h_ingredients_btn_frame_layout = QHBoxLayout(self.ingredients_btn_frame)
        self.h_ingredients_btn_frame_layout.setSpacing(5)
        self.h_ingredients_btn_frame_layout.setObjectName(u"h_ingredients_btn_frame_layout")
        self.h_ingredients_btn_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.ingredients_btn = QPushButton(self.ingredients_btn_frame)
        self.ingredients_btn.setObjectName(u"ingredients_btn")
        sizePolicy.setHeightForWidth(self.ingredients_btn.sizePolicy().hasHeightForWidth())
        self.ingredients_btn.setSizePolicy(sizePolicy)
        self.ingredients_btn.setMinimumSize(QSize(70, 40))
        self.ingredients_btn.setMaximumSize(QSize(70, 40))

        self.h_ingredients_btn_frame_layout.addWidget(self.ingredients_btn)


        self.v_buttons_frame_layout.addWidget(self.ingredients_btn_frame, 0, Qt.AlignHCenter)

        self.about_btn_frame = QFrame(self.buttons_frame)
        self.about_btn_frame.setObjectName(u"about_btn_frame")
        sizePolicy4.setHeightForWidth(self.about_btn_frame.sizePolicy().hasHeightForWidth())
        self.about_btn_frame.setSizePolicy(sizePolicy4)
        self.about_btn_frame.setMinimumSize(QSize(0, 40))
        self.about_btn_frame.setMaximumSize(QSize(16777215, 40))
        self.about_btn_frame.setFrameShape(QFrame.NoFrame)
        self.about_btn_frame.setFrameShadow(QFrame.Raised)
        self.h_about_btn_frame_layout = QHBoxLayout(self.about_btn_frame)
        self.h_about_btn_frame_layout.setSpacing(5)
        self.h_about_btn_frame_layout.setObjectName(u"h_about_btn_frame_layout")
        self.h_about_btn_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.about_btn = QPushButton(self.about_btn_frame)
        self.about_btn.setObjectName(u"about_btn")
        sizePolicy.setHeightForWidth(self.about_btn.sizePolicy().hasHeightForWidth())
        self.about_btn.setSizePolicy(sizePolicy)
        self.about_btn.setMinimumSize(QSize(70, 40))
        self.about_btn.setMaximumSize(QSize(70, 40))

        self.h_about_btn_frame_layout.addWidget(self.about_btn)


        self.v_buttons_frame_layout.addWidget(self.about_btn_frame, 0, Qt.AlignHCenter)


        self.v_left_menu_background_frame_layout.addWidget(self.buttons_frame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.h_content_frame_layout.addWidget(self.left_menu_background_frame)

        self.widgets_frame = QFrame(self.content_frame)
        self.widgets_frame.setObjectName(u"widgets_frame")
        self.widgets_frame.setStyleSheet(u"background-color: rgb(74, 76, 102);\n"
"")
        self.widgets_frame.setFrameShape(QFrame.NoFrame)
        self.widgets_frame.setFrameShadow(QFrame.Raised)
        self.v_widgets_frame_layout = QVBoxLayout(self.widgets_frame)
        self.v_widgets_frame_layout.setSpacing(0)
        self.v_widgets_frame_layout.setObjectName(u"v_widgets_frame_layout")
        self.v_widgets_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.pages_stack_widget = QStackedWidget(self.widgets_frame)
        self.pages_stack_widget.setObjectName(u"pages_stack_widget")
        self.recipes_page = QWidget()
        self.recipes_page.setObjectName(u"recipes_page")
        self.pages_stack_widget.addWidget(self.recipes_page)
        self.ingredients_page = QWidget()
        self.ingredients_page.setObjectName(u"ingredients_page")
        self.pages_stack_widget.addWidget(self.ingredients_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.pages_stack_widget.addWidget(self.about_page)

        self.v_widgets_frame_layout.addWidget(self.pages_stack_widget)


        self.h_content_frame_layout.addWidget(self.widgets_frame)


        self.v_centralwidget_layout.addWidget(self.content_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_stack_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.ingredients_btn.setText(QCoreApplication.translate("MainWindow", u"ingredients", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi
    