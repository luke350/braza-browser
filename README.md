![appicon](https://github.com/user-attachments/assets/9acd0cc2-ca6d-4685-aea9-ef6084a8f2de)

# Braza Browser

A modern Python-based web browser with integrated AI functionality, built using PyQt5. Features a clean, user-friendly interface with tabbed browsing and AI assistance powered by Duck.ai.

## Features

- **Tabbed Browsing**: Full support for multiple tabs with easy tab management
- **AI Integration**: Built-in AI assistant accessible via dedicated AI button (opens Duck.ai)
- **Modern UI**: Clean interface with shadow effects and responsive design
- **Navigation Controls**: Standard browser controls including back, forward, reload, and home buttons
- **Smart Search Bar**: Supports both URL navigation and web search
- **Keyboard Shortcuts**: 
  - `Ctrl+T`: New tab
  - `Ctrl+H`: Home page
  - `Ctrl+B`: Go back
  - `Ctrl+F`: Go forward
- **Custom Error Handling**: Enhanced JavaScript console error reporting
- **Responsive Design**: Minimum 800x600 resolution with scalable interface

## Requirements

- Python 3.6+
- PyQt5
- requests

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/luke350/braza-browser.git
   cd braza-browser
   ```

2. **Install dependencies**:
   ```bash
   pip install PyQt5 requests
   ```
   
   Or on Ubuntu/Debian:
   ```bash
   sudo apt-get install python3-pyqt5 python3-pyqt5.qtwebengine
   pip install requests
   ```

3. **Run the browser**:
   ```bash
   python braza.py
   ```

## Usage

- **Basic Navigation**: Use the address bar to enter URLs or search terms
- **New Tab**: Click the "+" button or press `Ctrl+T`
- **AI Assistant**: Click the "AI" button to open Duck.ai in a new tab
- **Tab Management**: Close tabs using the "×" button on each tab
- **Search**: Enter search terms or URLs in the search bar and press Enter or click "Search"

## Building Executable

You can compile the browser into a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --hidden-import=PyQt5.QtWebEngineCore --hidden-import=PyQt5.QtWebEngineWidgets --hidden-import=PyQt5.QtWebChannel --collect-all PyQt5.QtWebEngineWidgets braza.py
```

The executable will be created in the `dist/` directory.

**Note**: This compilation method has been tested and works in VS Code environments.

## Default Homepage

The browser uses [Google](https://www.google.com) as the default homepage for new tabs.

## What's Next?

Currently in development:
- **Lite Version**: A lightweight variant with reduced resource usage
- **Version 2.0**: Enhanced AI implementation with improved integration and features

## Contributing

Feel free to fork this project and submit pull requests. All contributions are welcome!

## Credits

Special thanks to **roocraft2** for their contributions to this project.

## License

This project is open source. Please respect the terms when using or modifying the code.
