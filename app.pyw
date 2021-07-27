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
db = Database('data/data.db', alchemy_effects_content, alchemy_ingredients_content, counter)

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
        if counter >= 100:
            log.debug("Stoping timer")
            self.timer.stop()
            log.debug("Showing main window.")
            self.main = MainWindow()
            self.main.show()
            log.debug("Closing splash screen.")
            self.close()
        counter += 1
        
        # Progressbar while the file is being set up.
        if counter <= 10 and (not db.check_if_exists()):
            log.debug("The counter is under 11 and the database file doens't exist. Creating one.")
            self.ui.status_label.setText("Setting up database file")
            QApplication.processEvents()
            db.setup_file()
        if db.check_if_exists() and counter <= 10:
            log.debug("The database file exist but the counter stills being under 11. Updating it to 11.")
            counter = 11
            self.ui.progress_bar.setValue(counter)
            QApplication.processEvents()

        #Progressbar while the database is being populated or checked if populated.
        if counter >= 11 and counter <= 80:
            log.debug("Counter above 10 and below 81. It's neded to check the database info.")
            self.ui.status_label.setText("Checking the database info.")
            QApplication.processEvents()
            if db.check_tables():
                log.debug("The tables are ok and populated. Updating the counter to exit this conditional up to 81.")
                counter = 81
                self.ui.progress_bar.setValue(counter)
                self.ui.status_label.setText("Database ready. Loading GUI.")
                QApplication.processEvents()
            else:
                log.debug("The tables weren't populated. Requesting both effects and ingredients.")
                self.ui.status_label.setText("Requesting alchemy effects from uesp.net")
                QApplication.processEvents()
                alchemy_effects = requests.get('https://en.uesp.net/wiki/Skyrim:Alchemy_Effects').content
                self.ui.status_label.setText("Requesting ingreddients from elderscrolls.fandom.com")
                QApplication.processEvents()
                alchemy_ingredients = requests.get('https://elderscrolls.fandom.com/wiki/Ingredients_(Skyrim)').content
                log.debug("Clearing them just in case.")
                db.clearing_tables()                
                log.debug("Setting up the database with the obtained info.")
                self.ui.status_label.setText("Updating the database.")
                QApplication.processEvents()
                self.show()
                db.tables_setup(alchemy_effects, alchemy_ingredients)  
        

if __name__ == "__main__":
    # Set the database
    data = Database('data/data.db', alchemy_effects_content, alchemy_ingredients_content, counter)
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())





