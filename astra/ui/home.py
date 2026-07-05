from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(25)

        logo = QLabel("🌌")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setStyleSheet("""
            font-size:80px;
        """)

        title = QLabel("Astra Browser")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            color:white;
            font-size:34px;
            font-weight:bold;
        """)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Google or enter URL...")
        self.search.setFixedWidth(600)
        self.search.setFixedHeight(48)

        self.button = QPushButton("Search")
        self.button.setFixedWidth(180)
        self.button.setFixedHeight(45)

        quick = QHBoxLayout()

        self.google = QPushButton("Google")
        self.youtube = QPushButton("YouTube")
        self.github = QPushButton("GitHub")

        for b in (
            self.google,
            self.youtube,
            self.github,
        ):
            b.setFixedSize(150, 45)
            quick.addWidget(b)

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(self.search, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(quick)

        self.setStyleSheet("""
        QWidget{
            background:#111319;
        }

        QLabel{
            color:white;
        }

        QLineEdit{
            background:#222633;
            color:white;
            border:2px solid #33394b;
            border-radius:14px;
            padding:10px;
            font-size:16px;
        }

        QPushButton{
            background:#3B82F6;
            color:white;
            border:none;
            border-radius:12px;
            font-size:16px;
        }

        QPushButton:hover{
            background:#2563EB;
        }
        """)