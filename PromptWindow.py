from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox, QListWidget, QPushButton, QVBoxLayout, QWidget
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QPixmap, QFont
#from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from VideoPlayer import VideoPlayer
#from PySide6.QtCore import Qt, QUrl

class PromptWindow(QMainWindow):
    """
    This is the window that the program opens when the program is first opened
    The code is generated as a class, but functions as sequenced code due to __init__.
    """
    def __init__(self):
        super().__init__() # needed for QMainWindow propert ies
        self.initWindow() # initalizes window
        self.UX() # initalizes ui
    
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
        label.setScaledContents(True)
        label.setGeometry(0, 0, pixmap.width()/3, pixmap.height()/3)
        label.move(x, y)
    
    def combo_box(self, text, items, x, y):
        label = QLabel(text, self)
        label.setFont(QFont("Helvetica", 12.5))
        label.adjustSize()
        label.move(x, y)
        options = QComboBox(self)
        options.setFont(QFont("Helvetica", 12))
        options.addItems(items)
        options.adjustSize()
        options.move(x + label.width() + 10, y - 10)
        return options

    def selection_panel(self,items:list, x, y):
        rlist = QListWidget(self)
        rlist.setSelectionMode(QListWidget.MultiSelection)
        rlist.addItems(items)
        rlist.setFixedHeight(270)
        rlist.setFixedWidth(270)
        rlist.move(x,y)
        rlist.setStyleSheet('color: #ffa07a; font-size: 18px')
        return rlist 
    
    def open_window(self):
        self.w = VideoPlayer([i.text() for i in self.intrestlist.selectedItems()] + [i.text() for i in self.goallist.selectedItems()])
        self.w.show()
    def UX(self):
        self.image("knight.jpeg", 310, 100)
        title = QLabel("Proliem", self)
        title.setStyleSheet("color: #ffa07a;font-family: Savoye LET; font-size: 90px;")
        title.setGeometry(300,120,300,120)
        title.move(318,9)
        interests = ["Algebra",
            "Geometry",
            "Algebra II",
            "Pre-Calculus",
            "Math Analysis",
            "Statistics",
            "Calculus AB",
            "Calculus BC",
            "Linear Algebra",
            "Physics",
            "Computer Science",
            "Chemistry",
            "Zoology",
            "Human Biology",
            "Biotechnology",
            "Biochemistry",
            "Psychology",
            "English",
            "Creative Writing",
            "Historical Literature",
            "Political Science",
            "American History",
            "History",
            "African History",
            "World History",
            "Spanish",
            "French",
            "Japanese",
            ]
        self.intrestlist = self.selection_panel(interests,9,60)
        goals = ["Homework", 
            "Standardized Test (ACT, SAT)",
            "Research",
            "For Fun",
            "AP tests"]
        self.goallist = self.selection_panel(goals,521,60)
        get_button = QPushButton('Proceed',self) 
        get_button.setGeometry(180,60,180,60)
        get_button.move(310,300)
        get_button.setStyleSheet('background-color: #808080; color: #ffa07a')
        get_button.clicked.connect(self.open_window)



    def video(self, url, x, y):
        player = QMediaPlayer()
        video_widget = QVideoWidget()
        player.setVideoOutput(self.video_widget)