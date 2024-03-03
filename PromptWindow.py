from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidget, QPushButton, QVBoxLayout, QWidget
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtGui import QPixmap
from PySide6.QtMultimediaWidgets import QVideoWidget
from VideoScroller import VideoScroller
from data import ret_reasons, ret_subjects

class PromptWindow(QMainWindow):
    """
    This is the window that the program opens when the program is first opened
    The code is generated as a class, but functions as sequenced code due to __init__.
    """
    def __init__(self) -> None:
        super().__init__() # needed for QMainWindow properties
        self.initWindow() # initalizes window
        self.UX() # initalizes ui
    
    def initWindow(self) -> None:
        """
        Initalizes the window size and starting position.
        """
        screen_geometry = QApplication.primaryScreen().availableGeometry() # Gets the width and height of the primary screen

        self.setWindowTitle("Form Submission")
        self.setFixedSize(800, 400) # set size + prevent resizing
        self.move(((screen_geometry.width() - self.width()) // 2), ((screen_geometry.height() - self.height()) // 2)) # centers application

    def image(self, dir, x, y) -> None:
        """
        Creates an image object.
        Due to how PySide6 works, it's technically a label, but don't worry about that.
        """
        label = QLabel(self)
        pixmap = QPixmap(dir)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry(0, 0, pixmap.width()/3, pixmap.height()/3)
        label.move(x, y)

    def selection_panel(self, items : list, x : int, y : int) -> QListWidget:
        rlist = QListWidget(self)
        rlist.setSelectionMode(QListWidget.MultiSelection)
        rlist.addItems(items)
        rlist.setFixedHeight(270)
        rlist.setFixedWidth(270)
        rlist.move(x,y)
        rlist.setStyleSheet('color: #ffa07a; font-size: 18px')
        return rlist 
    
    def open_window(self) -> None:
        self.w = VideoScroller([i.text() for i in self.intrestlist.selectedItems()] + [i.text() for i in self.goallist.selectedItems()])
        # the weird list returns the selected parameters in a list of strings.
        self.w.show()
        
    def UX(self) -> None:
        self.image("logo.jpeg", 310, 100)
        
        title = QLabel("Proliem", self)
        title.setStyleSheet("color: #ffa07a;font-family: Savoye LET; font-size: 90px;")
        title.setGeometry(300,120,300,120)
        title.move(318,9)
        
        self.intrestlist = self.selection_panel(ret_subjects(),9,60)
        self.goallist = self.selection_panel(ret_reasons(),521,60)
        
        get_button = QPushButton('Proceed',self) 
        get_button.setGeometry(180,60,180,60)
        get_button.move(310,300)
        get_button.setStyleSheet('background-color: #808080; color: #ffa07a')
        get_button.clicked.connect(self.open_window)