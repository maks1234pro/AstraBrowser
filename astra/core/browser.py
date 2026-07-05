from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QWebEngineView):

    def __init__(self):
        super().__init__()
        self.load_home()

    def load_home(self):
        self.setUrl(QUrl("https://www.google.com"))

    def open(self, text):
        text = text.strip()

        if not text:
            return

        if "." in text and " " not in text:
            if not text.startswith("http://") and not text.startswith("https://"):
                text = "https://" + text
        else:
            text = "https://www.google.com/search?q=" + text.replace(" ", "+")

        self.setUrl(QUrl(text))