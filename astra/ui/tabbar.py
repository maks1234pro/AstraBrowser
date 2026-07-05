from PyQt6.QtWidgets import QTabWidget
from astra.core.browser import Browser


class BrowserTabs(QTabWidget):

    def __init__(self):
        super().__init__()

        self.setDocumentMode(True)
        self.setTabsClosable(True)
        self.setMovable(True)

        self.tabCloseRequested.connect(self.close_tab)

        self.new_tab()

    def new_tab(self, title="New Tab"):
        browser = Browser()

        index = self.addTab(browser, title)
        self.setCurrentIndex(index)

        browser.titleChanged.connect(
            lambda title, b=browser: self.rename_tab(b, title)
        )

        return browser

    def rename_tab(self, browser, title):
        index = self.indexOf(browser)

        if index != -1:
            self.setTabText(index, title if title else "New Tab")

    def close_tab(self, index):
        if self.count() <= 1:
            return

        widget = self.widget(index)
        self.removeTab(index)
        widget.deleteLater()

    def current_browser(self):
        return self.currentWidget()