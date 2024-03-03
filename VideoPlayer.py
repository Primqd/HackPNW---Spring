from PySide6.QtWidgets import QWidget
from youtoob import search_videos

class VideoPlayer(QWidget):
    def __init__(self, subject, why, time):
        super().__init__()
        # self.results = search_videos(call ai for summarized keywords)
        
        