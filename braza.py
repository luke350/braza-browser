import sys
import threading
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QGraphicsDropShadowEffect,
    QTabWidget,
    QLabel,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QColor


class CustomWebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, line, source_id):
        print(f"JavaScript Error: {message} (Source: {source_id}, Line: {line})")


class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Luke's HTTPS Browser with Gemini AI")
        self.setGeometry(100, 100, 1024, 768)
        self.setMinimumSize(800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Add a QTabWidget to manage tabs
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)  # Enable close buttons on tabs
        self.tab_widget.tabCloseRequested.connect(self.close_tab)  # Connect close signal
        self.layout.addWidget(self.tab_widget)

        # Create the main browser tab
        self.new_tab()

        # Navigation bar
        self.nav_bar = QHBoxLayout()
        self.layout.addLayout(self.nav_bar)

        def add_shadow(widget):
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setOffset(2, 2)
            shadow.setColor(QColor(0, 0, 0, 160))
            widget.setGraphicsEffect(shadow)

        button_style = """
            QPushButton {
                border: 1px solid #555;
                border-radius: 5px;  
                background-color: #f0f0f0;
                padding: 2px 10px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """
        search_style = """
            QLineEdit {
                border: 1px solid #555;
                border-radius: 5px;  
                padding: 2px;  
                background-color: #f0f0f0;
            }
        """

        self.back_button = QPushButton("<")
        self.back_button.setShortcut("Ctrl+B")
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setStyleSheet(button_style)
        add_shadow(self.back_button)
        self.nav_bar.addWidget(self.back_button)

        self.home_button = QPushButton("Home")
        self.home_button.setShortcut("Ctrl+H")
        self.home_button.clicked.connect(self.go_home)
        self.home_button.setStyleSheet(button_style)
        add_shadow(self.home_button)
        self.nav_bar.addWidget(self.home_button)

        self.forward_button = QPushButton(">")
        self.forward_button.setShortcut("Ctrl+F")
        self.forward_button.clicked.connect(self.go_forward)
        self.forward_button.setStyleSheet(button_style)
        add_shadow(self.forward_button)
        self.nav_bar.addWidget(self.forward_button)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(self.reload_page)
        self.reload_button.setStyleSheet(button_style)
        add_shadow(self.reload_button)
        self.nav_bar.addWidget(self.reload_button)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("(By Luke Beckmann) Search Google or enter a URL...")
        self.search_bar.returnPressed.connect(self.search)
        self.search_bar.setStyleSheet(search_style)
        self.nav_bar.addWidget(self.search_bar)

        # Create a search button next to the search bar
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        self.search_button.setStyleSheet(button_style)
        add_shadow(self.search_button)
        self.nav_bar.addWidget(self.search_button)

        # Add Gemini AI button
        self.copilot_button = QPushButton("AI")
        self.copilot_button.setToolTip("Open Gemini AI in a new tab")
        self.copilot_button.clicked.connect(self.open_copilot_tab)
        self.copilot_button.setStyleSheet(button_style)
        add_shadow(self.copilot_button)
        self.nav_bar.addWidget(self.copilot_button)

        # Add a button to create a new tab on the tab bar
        self.new_tab_button = QPushButton("+")
        self.new_tab_button.setToolTip("New Tab (Ctrl+T)")
        self.new_tab_button.setShortcut("Ctrl+T")
        self.new_tab_button.clicked.connect(self.new_tab)  # Connect to the new_tab method
        self.new_tab_button.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                font-size: 18px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-radius: 5px;
            }
        """)
        self.tab_widget.setCornerWidget(self.new_tab_button, Qt.TopRightCorner)  # Place on the tab bar

    def new_tab(self):
        new_browser = QWebEngineView()
        new_browser.setPage(CustomWebEnginePage(new_browser))  # Use the custom page
        new_browser.setUrl(QUrl("https://www.google.com"))  # Default URL for new tabs
        new_browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        new_browser.settings().setAttribute(QWebEngineSettings.ErrorPageEnabled, False)

        self.tab_widget.addTab(new_browser, "New Tab")
        self.tab_widget.setCurrentWidget(new_browser)

    def open_copilot_tab(self):
        # Create a new tab with the Gemini webpage
        gemini_browser = QWebEngineView()
        gemini_browser.setPage(CustomWebEnginePage(gemini_browser))  # Use the custom page

        # Load the Gemini HTTP page
        gemini_browser.setUrl(QUrl("https://duck.ai"))  # Updated to the Gemini URL

        # Enable JavaScript and other necessary settings
        gemini_browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        gemini_browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        gemini_browser.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        gemini_browser.settings().setAttribute(QWebEngineSettings.ErrorPageEnabled, True)

        # Add the Gemini browser to a new tab
        self.tab_widget.addTab(gemini_browser, "AI")
        self.tab_widget.setCurrentWidget(gemini_browser)

    def close_tab(self, index):
        if self.tab_widget.count() > 1:  # Ensure at least one tab remains open
            self.tab_widget.removeTab(index)

    def get_current_browser(self):
        return self.tab_widget.currentWidget()

    def go_back(self):
        current_browser = self.get_current_browser()
        if isinstance(current_browser, QWebEngineView):
            current_browser.back()

    def go_forward(self):
        current_browser = self.get_current_browser()
        if isinstance(current_browser, QWebEngineView):
            current_browser.forward()

    def reload_page(self):
        current_browser = self.get_current_browser()
        if isinstance(current_browser, QWebEngineView):
            current_browser.reload()

    def search(self):
        current_browser = self.get_current_browser()
        if isinstance(current_browser, QWebEngineView):
            query = self.search_bar.text().strip()
            if not query.startswith(("http://", "https://")):
                query = f"http://{query}"  # Default to HTTP if no scheme is provided
            url = QUrl(query)
            current_browser.setUrl(url)

    def go_home(self):
        current_browser = self.get_current_browser()
        if isinstance(current_browser, QWebEngineView):
            current_browser.setUrl(QUrl("https://www.google.com"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    window.show()
    sys.exit(app.exec_())