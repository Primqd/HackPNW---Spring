from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QFont
from youtoob import search_videos
import webbrowser
import requests
# from json import load # for testing

class VideoPlayer(QWidget):
    def __init__(self, keywords):
        super().__init__()
        self.x = 800
        self.y = 475
        self.idx = 0
        
        self.results = search_videos(keywords)
        # self.results = load(open('yotoob.json')) # for testing
        self.init_window()
        self.init_UI()
    
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
    
    def push_button(self, text, func, x, y):
        button = QPushButton(text, self)
        button.clicked.connect(func)
        button.setFont(QFont("Helevetica", 15))
        button.adjustSize()
        button.move(x - button.width() // 2, y)
        return button
    
    def getImageFromURL(self,imageURL, pixmap, thumbnail):
        request = requests.get(imageURL)
        pixmap.loadFromData(request.content)
        thumbnail.setPixmap(pixmap)
    
    def big(self, text):
        if len(text) >= 80:
            return text[:80] + "..."
        else:
            return text
    
    def init_UI(self):
        if "videoId" in self.results["items"][self.idx]["id"]:
            youtube_link = f'https://www.youtube.com/watch?v={self.results["items"][self.idx]["id"]["videoId"]}'
        else:
            youtube_link = f'https://www.youtube.com/watch?v={self.results["items"][self.idx]["id"]["playlistId"]}'
        
        pixmap = QPixmap()
        self.thumbnail = QLabel(self)
        self.getImageFromURL(self.results["items"][self.idx]["snippet"]["thumbnails"]["high"]["url"], pixmap, self.thumbnail)
        self.thumbnail.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.thumbnail.move(self.x // 2 - 240, 10)
        self.thumbnail.setScaledContents(True)
        self.thumbnail.show()
        
        self.button = QPushButton('', self)
        def link(): webbrowser.open(youtube_link)
        self.button.clicked.connect(link)
        self.button.resize(480, 360)
        self.button.move(self.x // 2 - 240, 10)
        self.button.setFlat(True)
        
        title = self.big(f'{self.results["items"][self.idx]["snippet"]["title"]} by {self.results["items"][self.idx]["snippet"]["channelTitle"]}')
        #title = QLabel(f'{self.results["items"][idx]["snippet"]["title"]} by {self.results["items"][idx]["snippet"]["channelTitle"]}', self)
        self.title = QLabel(f'<a href=\"{youtube_link}\">{title}</a>', self)
        self.title.setOpenExternalLinks(True)
        self.title.setFont(QFont("Helevetica", 15))
        self.title.adjustSize()
        self.title.move(self.x // 2 - self.title.width() // 2, 375)
        self.desc = QLabel(self.results["items"][self.idx]["snippet"]["description"], self)
        shit = QFont("Helevetica", 10)
        shit.setItalic(True)
        self.desc.setFont(shit)
        self.desc.adjustSize()
        self.desc.move(self.x // 2 - self.desc.width() // 2, 400) 
        
        def go_left():
            if self.idx == 0: return
            self.idx -= 1
            self.refresh()
        def go_right():
            self.idx += 1
            if self.idx == len(self.results["items"]):
                #k = search_videos("keywords")
                k = {"items" : ["ligma balls"]}
                self.results["items"].extend(k["items"])
            self.refresh()
        
        left = self.push_button("Go Back", go_left, self.x // 4, 425)
        
        right = self.push_button("Next", go_right, 3 * (self.x // 4), 425)
        # pixmap.loadFromData(request.content)
        # button.setPixmap(pixmap)
    
    def refresh(self):
        if "videoId" in self.results["items"][self.idx]["id"]:
            youtube_link = f'https://www.youtube.com/watch?v={self.results["items"][self.idx]["id"]["videoId"]}'
        else:
            youtube_link = f'https://www.youtube.com/watch?v={self.results["items"][self.idx]["id"]["playlistId"]}'
        
        pixmap = QPixmap()
        self.getImageFromURL(self.results["items"][self.idx]["snippet"]["thumbnails"]["high"]["url"], pixmap, self.thumbnail)
        self.thumbnail.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.thumbnail.move(self.x // 2 - 240, 10)
        self.thumbnail.show()
        
        del self.button
        button = QPushButton('', self)
        button.setVisible(False)
        button.clicked.connect(lambda : webbrowser.open(youtube_link))
        button.resize(480, 360)
        button.move(self.x // 2 - 240, 10)
        button.setFlat(True)
        self.button = button
        self.button.show()
        #self.button.resize(480, 360)
        #self.button.move(self.x // 2 - 240, 10)
        #self.button.setFlat(True)
        
        #title = QLabel(f'{self.results["items"][idx]["snippet"]["title"]} by {self.results["items"][idx]["snippet"]["channelTitle"]}', self)
        title = self.big(f'{self.results["items"][self.idx]["snippet"]["title"]} by {self.results["items"][self.idx]["snippet"]["channelTitle"]}')
        self.title.setText(f'<a href=\"{youtube_link}\">{title}</a>')
        self.title.adjustSize()
        self.title.move(self.x // 2 - self.title.width() // 2, 375)
        
        self.desc.setText(self.results["items"][self.idx]["snippet"]["description"])
        self.desc.adjustSize()
        self.desc.move(self.x // 2 - self.desc.width() // 2, 400) 
#self.video["snippet"]["thumbnails"]["medium"]["url"]