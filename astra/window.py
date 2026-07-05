from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
)

from astra.ui.sidebar import Sidebar
from astra.ui.navbar import NavBar
from astra.ui.tabbar import BrowserTabs
from astra.ui.home import HomePage
from astra.ui.bookmarks import BookmarksPage
from astra.ui.history import HistoryPage

from astra.core.bookmarks import Bookmarks
from astra.core.history import History


class AstraWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🌌 Astra Browser")
        self.resize(1500, 900)

        root = QWidget()
        self.setCentralWidget(root)

        layout = QHBoxLayout(root)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()
        layout.addWidget(self.sidebar)

        right = QWidget()
        rightLayout = QVBoxLayout(right)
        rightLayout.setContentsMargins(0, 0, 0, 0)
        rightLayout.setSpacing(0)

        self.navbar = NavBar()
        rightLayout.addWidget(self.navbar)

        self.stack = QStackedWidget()

        self.home = HomePage()
        self.tabs = BrowserTabs()
        self.bookmarks = BookmarksPage()
        self.history = HistoryPage()

        self.bookmark_manager = Bookmarks()
        self.history_manager = History()

        self.stack.addWidget(self.home)
        self.stack.addWidget(self.tabs)
        self.stack.addWidget(self.bookmarks)
        self.stack.addWidget(self.history)

        rightLayout.addWidget(self.stack)

        layout.addWidget(right)

        self.connect_browser(self.tabs.current_browser())

        # ---------------- Navbar ----------------

        self.navbar.back.clicked.connect(
            lambda: self.tabs.current_browser().back()
        )

        self.navbar.forward.clicked.connect(
            lambda: self.tabs.current_browser().forward()
        )

        self.navbar.reload.clicked.connect(
            lambda: self.tabs.current_browser().reload()
        )

        self.navbar.home.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.home)
        )

        self.navbar.url.returnPressed.connect(self.search_bar)
        self.navbar.new_tab.clicked.connect(self.add_tab)

        if hasattr(self.navbar, "bookmark"):
            self.navbar.bookmark.clicked.connect(self.add_bookmark)

        # ---------------- Sidebar ----------------

        self.sidebar.home_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.home)
        )

        self.sidebar.web_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.tabs)
        )

        if hasattr(self.sidebar, "bookmarks_btn"):
            self.sidebar.bookmarks_btn.clicked.connect(
                self.show_bookmarks
            )

        if hasattr(self.sidebar, "history_btn"):
            self.sidebar.history_btn.clicked.connect(
                self.show_history
            )

        # ---------------- Home ----------------

        self.home.button.clicked.connect(self.search_home)
        self.home.search.returnPressed.connect(self.search_home)

        self.home.google.clicked.connect(
            lambda: self.open_site("google.com")
        )

        self.home.youtube.clicked.connect(
            lambda: self.open_site("youtube.com")
        )

        self.home.github.clicked.connect(
            lambda: self.open_site("github.com")
        )

    # ======================================

    def connect_browser(self, browser):
        browser.urlChanged.connect(self.update_url)
        browser.titleChanged.connect(self.save_history)

    def update_url(self, url):
        self.navbar.url.setText(url.toString())

    def search_bar(self):
        self.tabs.current_browser().open(
            self.navbar.url.text()
        )
        self.stack.setCurrentWidget(self.tabs)

    def search_home(self):
        self.tabs.current_browser().open(
            self.home.search.text()
        )
        self.stack.setCurrentWidget(self.tabs)

    def open_site(self, url):
        self.tabs.current_browser().open(url)
        self.stack.setCurrentWidget(self.tabs)

    def add_tab(self):
        browser = self.tabs.new_tab()
        self.connect_browser(browser)

    # ---------- Bookmarks ----------

    def add_bookmark(self):
        browser = self.tabs.current_browser()

        self.bookmark_manager.add(
            browser.title(),
            browser.url().toString()
        )

        self.bookmarks.refresh()

    def show_bookmarks(self):
        self.bookmarks.refresh()
        self.stack.setCurrentWidget(self.bookmarks)

    # ---------- History ----------

    def save_history(self):
        browser = self.tabs.current_browser()

        url = browser.url().toString()

        if url:
            self.history_manager.add(
                browser.title(),
                url
            )
            self.history.refresh()

    def show_history(self):
        self.history.refresh()
        self.stack.setCurrentWidget(self.history)