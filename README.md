# braza-browser
python based browser with implemented ai


# compiler code (works in vscode)
pyinstaller --onefile --windowed --hidden-import=PyQt5.QtWebEngineCore --hidden-import=PyQt5.QtWebEngineWidgets --hidden-import=PyQt5.QtWebChannel --collect-all PyQt5.QtWebEngineWidgets braza.py
