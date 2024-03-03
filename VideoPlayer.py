from PySide6.QtWidgets import QWidget, QApplication, QLabel, QGraphicsScene, QVBoxLayout, QGraphicsView, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QIcon
from youtoob import search_videos
import requests
from json import load # for testing

class VideoPlayer(QWidget):
    def __init__(self, subject, why, time):
        super().__init__()
        self.x = 800
        self.y = 500
        self.idx = 0
        
        # self.results = search_videos(call ai for summarized keywords)
        self.results = load(open('yotoob.json')) # for testing
        self.init_window()
        self.init_UI(self.idx)
    
    def image(self, dir, x, y):
        label = QLabel(self)
        pixmap = QPixmap(dir)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        label.move(x, y)
        label.setScaledContents(True)
        
    def init_window(self):
        self.setWindowIcon(QIcon("subscrib.png"))
        screen_geometry = QApplication.primaryScreen().availableGeometry() # Gets the width and height of the primary screen

        self.setWindowTitle("Video Scroller")
        # self.setGeometry(800, 800, 800, 800) # Default dimensions
        self.setFixedWidth(self.x) # prevent window from being resized
        self.setFixedHeight(self.y)
        
        self.move(((screen_geometry.width() - self.x) // 2), ((screen_geometry.height() - self.y) // 2)) # centers application
    
    def init_UI(self, idx):
        self.label  = QLabel(self)
        self.pixmap = QPixmap()
        self.getAndSetImageFromURL(self.results["items"][idx]["snippet"]["thumbnails"]["high"]["url"])
        self.resize(320, 240)
        self.move(self.x // 2, self.y)
        self.show() 
    
    def getAndSetImageFromURL(self,imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.label.setPixmap(self.pixmap)
#self.video["snippet"]["thumbnails"]["medium"]["url"]