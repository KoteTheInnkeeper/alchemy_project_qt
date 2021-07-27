import logging
from PyQt5 import QtCore

# Setting the logger
# Set the basic configurations for the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')
# Create the logger
log = logging.getLogger("alchemy_project_qt.app")

import requests
import sys


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow

from data.database_management import Database

from qtui.ui_splash_screen import Ui_SplashScreen
from qtui.ui_main_window import Ui_MainWindow

# Globals (for progress bar)
counter = 0

# Get the page content for the effects and ingredients
alchemy_effects_content = requests.get('https://en.uesp.net/wiki/Skyrim:Alchemy_Effects').content
counter += 15
alchemy_ingredients_content = requests.get('https://elderscrolls.fandom.com/wiki/Ingredients_(Skyrim)').content
counter += 15

# Set the database
data = Database('data/data.db', alchemy_effects_content, alchemy_ingredients_content, counter)


# Main window class

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# Splash screen class

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        # REMOVE title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECTS
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.splash_main_frame.setGraphicsEffect(self.shadow)

        # QTIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in miliseconds.
        self.timer.start(35)



        # SHOW => Main window
        self.show()


     # App functions
    def progress(self):
        global counter
        log.debug("Updating progress bar value.")
        self.ui.progress_bar.setValue(counter)
        log.debug("Closing splash screen and open app.")
        # Wait in 35% until the database is created.

        # Wait in 80% until the database is populated.
        if counter >= 100:
            log.debug("Stoping timer")
            self.timer.stop()
            log.debug("Showing main window.")
            self.main = MainWindow()
            self.main.show()
            log.debug("Closing splash screen.")
            self.close()
        counter += 1

            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())





