from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox
from PySide6.QtGui import QPixmap, QFont
#from PySide6.QtMultimedia import QMediaPlayer
#from PySide6.QtMultimediaWidgets import QVideoWidget
#from PySide6.QtCore import Qt, QUrl

class PromptWindow(QMainWindow):
    """
    This is the window that the program opens when the program is first opened
    The code is generated as a class, but functions as sequenced code due to __init__.
    """
    def __init__(self):
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
        label.setFont(QFont("Helvetica", 12.5))
        label.adjustSize()
        label.move(x, y)
        options = QComboBox(self)
        options.setFont(QFont("Helvetica", 12.5))
        options.addItems(items)
        options.adjustSize()
        options.move(x + label.width() + 10, y - 3)
        return options

    
    def initUI(self):
        # self.image("bing chilling.png", 0,0)
        self.image("graphic design is my passion.png", 0, 0)
        title = QLabel("ResearchHub", self)
        title.setFont(QFont("Helevetica", 30))
        title.adjustSize()
        title.move(400 - title.width() // 2, 0)
        self.combo_box("What do you want to focus on?", [
            "Algebra",
            "Geometry",
            "Algebra II",
            "Pre-Calculus",
            "Math Analysis",
            "Statistics",
            "Calculus AB",
            "Calculus BC",
            "Linear Algebra",
            "Physics 1",
            "Physics 2",
            "Physics C",
            "Computer Science Principles",
            "Computer Science A",
            "Data Structures",
            "Algorithims",
            "Inorganic Chemistry",
            "Organic Chemistry",
            "Zoology",
            "Human Biology",
            "Biotechnology",
            "Biochemistry",
            "Psychology",
            "English",
            "Creative Writing",
            "Multimodal Literature",
            "Historical Literature",
            "Political Science",
            "American History",
            "European History",
            "Russian History",
            "Asian History",
            "African History",
            "International History",
            "Spanish",
            "French",
            "Japanese",
            ], 10,60)
        self.combo_box("What are you studying for?", 
            ["Homework", 
            "Standardized Test (ACT, SAT)",
            "Research",
            "For Fun"],
             10, 100)
""
        # subjects
        # tests?


    # def video(self, url, x, y):
    #     player = QMediaPlayer()
    #     player.setSource(QUrl("https://www.youtube.com/watch?v=QMR9KR5IMYs"))
    #     video_widget = QVideoWidget()
    #     player.setVideoOutput(video_widget)
    #     video_widget.show()
    #     video_widget.move(x,y)
    #     player.play()

