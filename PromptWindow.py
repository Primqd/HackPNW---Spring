from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox, QSpinBox, QPushButton
from PySide6.QtGui import QPixmap, QFont
from VideoPlayer import VideoPlayer
import data
#from PySide6.QtMultimedia import QMediaPlayer
#from PySide6.QtMultimediaWidgets import QVideoWidget
#from PySide6.QtCore import Qt

class PromptWindow(QMainWindow):
    """
    This is the window that the program opens when the program is first opened
    The code is generated as a class, but functions as sequenced code due to __init__.
    """
    def __init__(self):
        self.font = "Helevetica"
        super().__init__() # needed for QMainWindow properties
        self.initWindow() # initalizes window
        self.initUI() # initalizes ui
    
    def initWindow(self):
        """
        Initalizes the window size and starting position.
        """
        screen_geometry = QApplication.primaryScreen().availableGeometry() # Gets the width and height of the primary screen

        self.setWindowTitle("Form Submission")
        # self.setGeometry(800, 800, 800, 800) # Default dimensions
        self.setFixedWidth(800) # prevent window from being resized
        self.setFixedHeight(400)
        self.move(((screen_geometry.width() - self.width()) // 2), ((screen_geometry.height() - self.height()) // 2)) # centers application

    def image(self, dir, x, y):
        label = QLabel(self)
        pixmap = QPixmap(dir)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        label.move(x, y)
        label.setScaledContents(True)
    
    def combo_box(self, text, items, x, y):
        label = QLabel(text, self)
        label.setFont(QFont(self.font, 12.5))
        label.adjustSize()
        label.move(x, y)
        options = QComboBox(self)
        options.setFont(QFont(self.font, 12.5))
        options.addItems(items)
        options.adjustSize()
        options.move(x + label.width() + 10, y)
        return options

    def spin_box(self, text, small, big, x, y):
        label = QLabel(text, self)
        label.setFont(QFont(self.font, 12.5))
        label.adjustSize()
        label.move(x, y)
        options = QSpinBox(self)
        options.setFont(QFont(self.font, 12.5))
        options.setMinimum = small
        options.setMaximum = big
        options.adjustSize()
        options.move(x + label.width() + 10, y)
        return options

    def video_time(self, subject, why, time):
        self.w = VideoPlayer(subject, why, time)
        self.w.show()

    def initUI(self):
        # self.image("bing chilling.png", 0,0)
        self.image("graphic design is my passion.png", 0, 350)
        title = QLabel("ResearchHub", self)
        title.setFont(QFont("Helevetica", 30))
        # title.setStyleSheet("color: white")
        title.adjustSize()

        title.move(400 - title.width() // 2, 0)
        subject = self.combo_box("What do you want to focus on?", data.ret_subjects(), 10,60)
        why = self.combo_box("What are you studying for?", data.ret_reasons(),10, 100)
        time = self.spin_box("How long should the videos be? (in minutes)", 1, 60, 10, 140)

        generate_button = QPushButton("Find videos", self)
        generate_button.setFont(QFont(self.font, 12.5))
        generate_button.move(400, 300)
        generate_button.clicked.connect(self.video_time)
        # subjects
        # tests?
    

