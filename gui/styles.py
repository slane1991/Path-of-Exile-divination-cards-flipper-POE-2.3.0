MAIN_WINDOW = """
    QMainWindow {
        background-color: #1a1a1a;
    }
    QWidget {
        background-color: #1a1a1a;
        color: #e0e0e0;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
"""

HEADER_LABEL = """
    QLabel {
        font-size: 24px;
        font-weight: bold;
        padding: 15px 0;
        color: #f0f0f0;
        border-bottom: 1px solid #444;
    }
    QLabel:hover {
        color: #aa9c39;
        text-shadow: 0 0 8px rgba(170, 156, 57, 0.3);
    }
"""

TABLE_WIDGET = """
    QTableWidget {
        background-color: #252525;
        border: 1px solid #333;
        border-radius: 6px;
        color: #e0e0e0;
        gridline-color: #333;
        font-size: 13px;
        alternate-background-color: #252525;
    }
    QTableWidget::item {
        padding: 8px;
        border-bottom: 1px solid #333;
    }
    QTableWidget::item:selected {
        background-color: #3a3a3a;
        color: white;
        border: none;
    }
    QHeaderView::section {
        background-color: #2d2d2d;
        color: #f0f0f0;
        padding: 10px;
        border: none;
        font-weight: bold;
        font-size: 13px;
        border-bottom: 2px solid #4CAF50;
    }
    QScrollBar:vertical {
        background: #252525;
        width: 12px;
        margin: 0;
    }
    QScrollBar::handle:vertical {
        background: #4CAF50;
        min-height: 20px;
        border-radius: 6px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0;
        background: none;
    }
"""

COMBO_BOX = """
    QComboBox {
        background-color: #2d2d2d;
        color: #f0f0f0;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 8px 15px;
        font-size: 14px;
        min-width: 100px;
    }
    QComboBox:hover {
        border: 1px solid #4CAF50;
    }
    QComboBox QAbstractItemView {
        background-color: #2d2d2d;
        color: #f0f0f0;
        border: 1px solid #444;
        selection-background-color: #4CAF50;
        padding: 8px;
    }
"""

START_BUTTON = """
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 14px;
        font-weight: bold;
        border-radius: 5px;
        min-width: 120px;
        transition: all 0.3s;
    }
    QPushButton:hover {
        background-color: #45a049;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
    }
    QPushButton:pressed {
        background-color: #3d8b40;
        transform: translateY(1px);
    }
    QPushButton:disabled {
        background-color: #333;
        color: #666;
    }
"""

UPDATE_BUTTON = """
    QPushButton {
        background-color: #2d2d2d;
        color: #f0f0f0;
        border: 1px solid #444;
        padding: 12px 24px;
        font-size: 14px;
        font-weight: bold;
        border-radius: 5px;
        min-width: 120px;
        transition: all 0.3s;
    }
    QPushButton:hover {
        background-color: #3a3a3a;
        border: 1px solid #4CAF50;
        transform: translateY(-1px);
    }
    QPushButton:pressed {
        background-color: #333;
        transform: translateY(1px);
    }
"""

STATUS_LABEL = """
    QLabel {
        color: #aaa;
        font-size: 13px;
        padding: 8px 12px;
        background-color: #2d2d2d;
        border-radius: 4px;
    }
"""

COPY_LABEL = """
    QLabel {
        background-color: rgba(76, 175, 80, 180);
        color: white;
        padding: 3px 8px;
        border-radius: 3px;
        font-size: 12px;
        opacity: 0;
    }
"""
FOOTER = "<a href='https://github.com/ezbooz' style='text-decoration:none; color:#666;'>github.com/ezbooz</a>"
FOOTER_LABEL = """
    QLabel {
        font-size: 11px;
        padding-top: 10px;
        border-top: 1px solid #444;
    }
    QLabel:hover {
        color: #999;
    }
"""

MESSAGE_BOX = """
    QMessageBox {
    }
    QLabel {
        color: #e0e0e0;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 8px 16px;
        font-size: 14px;
        min-width: 80px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
"""


def get_update_message(remote_version, current_version, description) -> str:
    return f"""
        <p style='font-size:14px;'><b>A new version (v{remote_version}) is available!</b></p>
        <p style='font-size:13px;'>Current version: v{current_version}</p>
        <p style='font-size:13px;'><b>Whats new:</b><br>{description }</p><br>
        <p style='font-size:14px;'>Download update: 
        <a href='https://github.com/ezbooz/Path-of-Exile-divination-cards-flipper-POE' 
        style='color:#4CAF50; text-decoration:none;'><b>GitHub Repository</b></a></p>
    """


HEADER = """
            <div style='text-align: center;'>
                <h1 style='margin: 0; color: #f0f0f0; font-weight: bold;'>
                    <a href='https://github.com/ezbooz/Path-of-Exile-divination-cards-flipper-POE'
                    style='text-decoration: none; color: #f0f0f0;'>
                    Path of Exile Card Flipper
                    </a>
                </h1>
                <p style='margin: 5px 0 0; color: #aaa; font-size: 12px;'>
                    Click card name to copy | Double-click to open trade in browser
                </p>
            </div>
        """

TAB_STYLE = """
QTabBar::tab {
    background: #222;
    color: #e0e0e0;
    padding: 10px 20px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    font-weight: bold;
}
QTabBar::tab:selected {
    background: #4CAF50;
    color: #fff;
}
QTabBar::tab:!selected {
    margin-top: 2px;
}
QTabWidget::pane {
    border-top: 2px solid #4CAF50;
    top: -0.5em;
}
"""

TABLE_HEADER_STYLE = """
QHeaderView::section {
    background-color: #2d2d2d;
    color: #f0f0f0;
    padding: 10px;
    border: none;
    font-weight: bold;
    font-size: 13px;
    border-bottom: 2px solid #4CAF50;
}
"""

CYBERPUNK_MAIN_WINDOW = """
QMainWindow, QWidget {
    background-color: #181828;
    color: #e0e0e0;
    font-family: 'Orbitron', 'Segoe UI', Arial, sans-serif;
}
"""

CYBERPUNK_HEADER_LABEL = """
QLabel {
    font-size: 28px;
    font-weight: bold;
    color: #00fff7;
    text-shadow: 0 0 8px #00fff7, 0 0 16px #00fff7;
    padding: 20px 0;
    border-bottom: 2px solid #ff00ea;
}
"""

CYBERPUNK_TAB_STYLE = """
QTabBar::tab {
    background: #23234a;
    color: #ff00ea;
    padding: 12px 24px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-weight: bold;
    border: 2px solid #00fff7;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background: #181828;
    color: #00fff7;
    border-bottom: 2px solid #39ff14;
}
QTabWidget::pane {
    border-top: 2px solid #ff00ea;
    top: -0.5em;
}
"""

CYBERPUNK_TABLE_WIDGET = """
QTableWidget {
    background-color: #23234a;
    color: #e0e0e0;
    border: 2px solid #ff00ea;
    font-size: 14px;
}
QTableWidget::item:selected {
    background-color: #ff00ea;
    color: #181828;
}
"""

CYBERPUNK_TABLE_HEADER = """
QHeaderView::section {
    background-color: #181828;
    color: #39ff14;
    padding: 12px;
    border: none;
    font-weight: bold;
    font-size: 15px;
    border-bottom: 2px solid #00fff7;
}
"""

CYBERPUNK_BUTTON = """
QPushButton {
    background-color: #00fff7;
    color: #181828;
    border-radius: 8px;
    font-weight: bold;
    font-size: 16px;
    padding: 10px 24px;
    border: 2px solid #ff00ea;
    box-shadow: 0 0 8px #00fff7;
}
QPushButton:hover {
    background-color: #ff00ea;
    color: #fff200;
    border: 2px solid #39ff14;
    box-shadow: 0 0 16px #ff00ea;
}
"""

OCCULT_MAIN_WINDOW = """
QMainWindow, QWidget {
    background-color: #181818;
    color: #e0d8b0;
    font-family: 'Georgia', 'Garamond', serif;
}
"""

OCCULT_HEADER_LABEL = """
QLabel {
    font-size: 28px;
    font-weight: bold;
    color: #bfa046;
    text-shadow: 0 0 8px #bfa046, 0 0 16px #1a1410;
    padding: 20px 0;
    border-bottom: 2px solid #a83232;
}
"""

OCCULT_TAB_STYLE = """
QTabBar::tab {
    background: #23201a;
    color: #bfa046;
    padding: 12px 24px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-weight: bold;
    border: 2px solid #6e4a7e;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background: #1a1410;
    color: #e0d8b0;
    border-bottom: 2px solid #a83232;
}
QTabWidget::pane {
    border-top: 2px solid #a83232;
    top: -0.5em;
}
"""

OCCULT_TABLE_WIDGET = """
QTableWidget {
    background-color: #23201a;
    color: #e0d8b0;
    border: 2px solid #6e4a7e;
    font-size: 14px;
}
QTableWidget::item:selected {
    background-color: #6e4a7e;
    color: #e0d8b0;
}
"""

OCCULT_TABLE_HEADER = """
QHeaderView::section {
    background-color: #1a1410;
    color: #bfa046;
    padding: 12px;
    border: none;
    font-weight: bold;
    font-size: 15px;
    border-bottom: 2px solid #a83232;
}
"""

OCCULT_BUTTON = """
QPushButton {
    background-color: #23201a;
    color: #bfa046;
    border-radius: 8px;
    font-weight: bold;
    font-size: 16px;
    padding: 10px 24px;
    border: 2px solid #a83232;
}
QPushButton:hover {
    background-color: #a83232;
    color: #e0d8b0;
    border: 2px solid #bfa046;
}
"""

BLACK_PURPLE_MAIN_WINDOW = """
QMainWindow, QWidget {
    background-color: #181818;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
}
"""

BLACK_PURPLE_HEADER_LABEL = """
QLabel {
    font-size: 28px;
    font-weight: bold;
    color: #ffd700;
    text-shadow: 0 0 8px #ffd700, 0 0 16px #2d193c;
    padding: 20px 0;
    border-bottom: 2px solid #ffd700;
}
"""

BLACK_PURPLE_TAB_STYLE = """
QTabBar::tab {
    background: #2d193c;
    color: #ffd700;
    padding: 12px 24px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-weight: bold;
    border: 2px solid #ffd700;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background: #181818;
    color: #ffd700;
    border-bottom: 2px solid #ffd700;
}
QTabWidget::pane {
    border-top: 2px solid #ffd700;
    top: -0.5em;
}
"""

BLACK_PURPLE_TABLE_WIDGET = """
QTableWidget {
    background-color: #2d193c;
    color: #e0e0e0;
    border: 2px solid #ffd700;
    font-size: 14px;
}
QTableWidget::item:selected {
    background-color: #ffd700;
    color: #2d193c;
}
"""

BLACK_PURPLE_TABLE_HEADER = """
QHeaderView::section {
    background-color: #181818;
    color: #ffd700;
    padding: 12px;
    border: none;
    font-weight: bold;
    font-size: 15px;
    border-bottom: 2px solid #ffd700;
}
"""

BLACK_PURPLE_BUTTON = """
QPushButton {
    background-color: #2d193c;
    color: #ffd700;
    border-radius: 8px;
    font-weight: bold;
    font-size: 16px;
    padding: 10px 24px;
    border: 2px solid #ffd700;
}
QPushButton:hover {
    background-color: #ffd700;
    color: #2d193c;
    border: 2px solid #ffd700;
}
"""

CYBERPUNK_DARK_MAIN_WINDOW = """
QMainWindow, QWidget {
    background-color: #14121a;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
}
"""

CYBERPUNK_DARK_HEADER_LABEL = """
QLabel {
    font-size: 28px;
    font-weight: bold;
    color: #00bcd4;
    text-shadow: 0 0 8px #00bcd4, 0 0 16px #1a1a24;
    padding: 20px 0;
    border-bottom: 2px solid #b400a1;
}
"""

CYBERPUNK_DARK_TAB_STYLE = """
QTabBar::tab {
    background: #1a1a24;
    color: #00bcd4;
    padding: 12px 24px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-weight: bold;
    border: 2px solid #b400a1;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background: #14121a;
    color: #bfa046;
    border-bottom: 2px solid #00bcd4;
}
QTabWidget::pane {
    border-top: 2px solid #b400a1;
    top: -0.5em;
}
"""

CYBERPUNK_DARK_TABLE_WIDGET = """
QTableWidget {
    background-color: #1a1a24;
    color: #e0e0e0;
    border: 2px solid #00bcd4;
    font-size: 14px;
}
QTableWidget::item:selected {
    background-color: #00bcd4;
    color: #1a1a24;
}
"""

CYBERPUNK_DARK_TABLE_HEADER = """
QHeaderView::section {
    background-color: #14121a;
    color: #bfa046;
    padding: 12px;
    border: none;
    font-weight: bold;
    font-size: 15px;
    border-bottom: 2px solid #00bcd4;
}
"""

CYBERPUNK_DARK_BUTTON = """
QPushButton {
    background-color: #1a1a24;
    color: #00bcd4;
    border-radius: 8px;
    font-weight: bold;
    font-size: 16px;
    padding: 10px 24px;
    border: 2px solid #b400a1;
}
QPushButton:hover {
    background-color: #00bcd4;
    color: #1a1a24;
    border: 2px solid #bfa046;
}
"""
