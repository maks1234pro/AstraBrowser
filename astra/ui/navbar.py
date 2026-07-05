from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLineEdit


class NavBar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        self.back = QPushButton("←")
        self.forward = QPushButton("→")
        self.reload = QPushButton("⟳")
        self.home = QPushButton("🏠")
        self.bookmark = QPushButton("⭐")
        self.new_tab = QPushButton("+")

        self.url = QLineEdit()
        self.url.setPlaceholderText("Search Google or enter URL...")

        for btn in [
            self.back,
            self.forward,
            self.reload,
            self.home,
            self.bookmark,
            self.new_tab,
        ]:
            btn.setFixedSize(42, 42)

        layout.addWidget(self.back)
        layout.addWidget(self.forward)
        layout.addWidget(self.reload)
        layout.addWidget(self.home)
        layout.addWidget(self.bookmark)
        layout.addWidget(self.new_tab)
        layout.addWidget(self.url)

        self.setStyleSheet("""
        QWidget{
            background:#1b1d26;
        }

        QPushButton{
            background:#2b2d3a;
            color:white;
            border:none;
            border-radius:10px;
            font-size:18px;
        }

        QPushButton:hover{
            background:#3b3d4c;
        }

        QLineEdit{
            background:#2b2d3a;
            color:white;
            border:none;
            border-radius:10px;
            padding:10px;
            font-size:15px;
        }
        """)