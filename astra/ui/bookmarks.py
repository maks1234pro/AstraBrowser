from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
)

from astra.core.bookmarks import Bookmarks


class BookmarksPage(QWidget):

    def __init__(self):
        super().__init__()

        self.manager = Bookmarks()

        layout = QVBoxLayout(self)

        title = QLabel("⭐ Bookmarks")
        title.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        self.list = QListWidget()

        self.list.setStyleSheet("""
            QListWidget{
                background:#1f2430;
                color:white;
                border:none;
                border-radius:10px;
                padding:10px;
                font-size:15px;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(self.list)

        self.setStyleSheet("""
            QWidget{
                background:#111319;
            }
        """)

        self.refresh()

    def refresh(self):
        self.list.clear()

        for bookmark in self.manager.get_all():
            self.list.addItem(
                f"{bookmark['title']}   —   {bookmark['url']}"
            )