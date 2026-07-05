from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QPushButton,
)

from astra.core.history import History


class HistoryPage(QWidget):

    def __init__(self):
        super().__init__()

        self.manager = History()

        layout = QVBoxLayout(self)

        title = QLabel("🕘 History")
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

        self.clear_btn = QPushButton("Clear History")

        self.clear_btn.setStyleSheet("""
            QPushButton{
                background:#c0392b;
                color:white;
                border:none;
                border-radius:10px;
                padding:10px;
            }

            QPushButton:hover{
                background:#e74c3c;
            }
        """)

        self.clear_btn.clicked.connect(self.clear_history)

        layout.addWidget(title)
        layout.addWidget(self.list)
        layout.addWidget(self.clear_btn)

        self.setStyleSheet("""
            QWidget{
                background:#111319;
            }
        """)

        self.refresh()

    def refresh(self):
        self.list.clear()

        for item in self.manager.get_all():
            self.list.addItem(
                f"{item['title']}   —   {item['url']}"
            )

    def clear_history(self):
        self.manager.clear()
        self.refresh()