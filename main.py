import sys
from PyQt6.QtWidgets import QApplication
from astra.window import AstraWindow


def main():
    app = QApplication(sys.argv)

    window = AstraWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()