from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(70)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(8)

        self.home_btn = QPushButton("🏠")
        self.web_btn = QPushButton("🌍")
        self.bookmarks_btn = QPushButton("⭐")
        self.downloads_btn = QPushButton("📥")
        self.history_btn = QPushButton("🕘")

        for btn in (
            self.home_btn,
            self.web_btn,
            self.bookmarks_btn,
            self.downloads_btn,
            self.history_btn,
        ):
            btn.setFixedSize(50, 50)
            layout.addWidget(btn)

        self.setStyleSheet("""
        QWidget{
            background:#111319;
        }

        QPushButton{
            background:transparent;
            color:white;
            border:none;
            border-radius:12px;
            font-size:22px;
        }

        QPushButton:hover{
            background:#2b2d3a;
        }
        """)