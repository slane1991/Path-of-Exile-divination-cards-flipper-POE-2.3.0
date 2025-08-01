import json
from typing import Dict, List, Optional

from PyQt6.QtCore import QPropertyAnimation, Qt, QTimer, QUrl
from PyQt6.QtGui import QColor, QDesktopServices
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStyle,
    QStyledItemDelegate,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QTabWidget,
)

from __version__ import __version__ as version
from gui.styles import (
    COMBO_BOX,
    COPY_LABEL,
    FOOTER,
    FOOTER_LABEL,
    HEADER,
    HEADER_LABEL,
    MAIN_WINDOW,
    MESSAGE_BOX,
    START_BUTTON,
    STATUS_LABEL,
    TABLE_WIDGET,
    UPDATE_BUTTON,
    get_update_message,
    TAB_STYLE,
    TABLE_HEADER_STYLE,
    CYBERPUNK_MAIN_WINDOW,
    CYBERPUNK_HEADER_LABEL,
    CYBERPUNK_TAB_STYLE,
    CYBERPUNK_TABLE_WIDGET,
    CYBERPUNK_TABLE_HEADER,
    CYBERPUNK_BUTTON,
    OCCULT_MAIN_WINDOW,
    OCCULT_HEADER_LABEL,
    OCCULT_TAB_STYLE,
    OCCULT_TABLE_WIDGET,
    OCCULT_TABLE_HEADER,
    OCCULT_BUTTON,
    BLACK_PURPLE_MAIN_WINDOW,
    BLACK_PURPLE_HEADER_LABEL,
    BLACK_PURPLE_TAB_STYLE,
    BLACK_PURPLE_TABLE_WIDGET,
    BLACK_PURPLE_TABLE_HEADER,
    BLACK_PURPLE_BUTTON,
    CYBERPUNK_DARK_MAIN_WINDOW,
    CYBERPUNK_DARK_HEADER_LABEL,
    CYBERPUNK_DARK_TAB_STYLE,
    CYBERPUNK_DARK_TABLE_WIDGET,
    CYBERPUNK_DARK_TABLE_HEADER,
    CYBERPUNK_DARK_BUTTON,
)
from poeNinja.ninjaAPI import PoeNinja
from utils.utils import Utils
from essence_flipper import get_essence_flips
from awakened_gem_flipper import get_awakened_gem_flips
from alt_gem_flipper import get_lab_alt_gem_flips


class NoFocusDelegate(QStyledItemDelegate):
    """Delegate that removes focus highlight from table items."""

    def paint(self, painter, option, index):
        if option.state & QStyle.StateFlag.State_HasFocus:
            option.state &= ~QStyle.StateFlag.State_HasFocus
        super().paint(painter, option, index)


class MainWindow(QMainWindow):
    """Main application window for Path of Exile Card Flipper."""

    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self._setup_ui()
        self._setup_animation_timers()
        self._setup_connections()
        self.setStyleSheet(
            CYBERPUNK_DARK_MAIN_WINDOW +
            CYBERPUNK_DARK_TAB_STYLE +
            CYBERPUNK_DARK_TABLE_WIDGET +
            CYBERPUNK_DARK_TABLE_HEADER
        )

    def _setup_ui(self) -> None:
        """Initialize all UI components."""
        self._configure_main_window()
        self._create_top_bar()
        self._create_tabs()
        self.setStyleSheet(MAIN_WINDOW)

    def _configure_main_window(self) -> None:
        """Configure main window properties."""
        self.setWindowTitle(
            f"Path of Exile Card Flipper v{version} | github.com/ezbooz"
        )
        self.setFixedSize(1070, 700)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

    def _create_top_bar(self):
        """Create the league selector and status label at the top."""
        self.top_bar = QHBoxLayout()
        self.league_selector = QComboBox()
        self.league_selector.addItems(
            [league["name"] for league in self.utils.get_current_leagues()]
        )
        self.league_selector.setStyleSheet(COMBO_BOX)
        self.status_label = QLabel("Select league")
        self.status_label.setStyleSheet(STATUS_LABEL)
        self.top_bar.addWidget(QLabel("League:"))
        self.top_bar.addWidget(self.league_selector)
        self.top_bar.addWidget(self.status_label)
        self.top_bar.addStretch(1)
        # Add update button to top bar
        self.update_button = QPushButton("Check for Updates")
        self.update_button.setStyleSheet(UPDATE_BUTTON)
        self.top_bar.addWidget(self.update_button)

    def _create_tabs(self):
        """Create the main tab widget and each flipping tab."""
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)

        # Divination Cards Tab
        self.div_tab = QWidget()
        self.div_tab_layout = QVBoxLayout(self.div_tab)
        self.div_start_button = QPushButton("Run Divination Card Flipper")
        self.div_start_button.setStyleSheet(CYBERPUNK_DARK_BUTTON)
        self.div_table = QTableWidget()
        self.div_tab_layout.addWidget(self.div_start_button)
        self.div_tab_layout.addWidget(self.div_table)
        self.tabs.addTab(self.div_tab, "Divination Cards")

        # Essence Flipper Tab
        self.essence_tab = QWidget()
        self.essence_tab_layout = QVBoxLayout(self.essence_tab)
        self.essence_flipper_button = QPushButton("Run Essence Flipper")
        self.essence_flipper_button.setStyleSheet(CYBERPUNK_DARK_BUTTON)
        self.essence_table = QTableWidget()
        self.essence_tab_layout.addWidget(self.essence_flipper_button)
        self.essence_tab_layout.addWidget(self.essence_table)
        self.tabs.addTab(self.essence_tab, "Essence Flipper")

        # Awakened Gem Flipper Tab
        self.awakened_tab = QWidget()
        self.awakened_tab_layout = QVBoxLayout(self.awakened_tab)
        self.awakened_gem_flipper_button = QPushButton("Run Awakened Gem Flipper")
        self.awakened_gem_flipper_button.setStyleSheet(CYBERPUNK_DARK_BUTTON)
        self.awakened_table = QTableWidget()
        self.awakened_tab_layout.addWidget(self.awakened_gem_flipper_button)
        self.awakened_tab_layout.addWidget(self.awakened_table)
        self.tabs.addTab(self.awakened_tab, "Awakened Gem Flipper")

        # Alt Quality Gem Flipper Tab
        self.alt_tab = QWidget()
        self.alt_tab_layout = QVBoxLayout(self.alt_tab)
        self.alt_gem_flipper_button = QPushButton("Run Alt Quality Gem Flipper")
        self.alt_gem_flipper_button.setStyleSheet(CYBERPUNK_DARK_BUTTON)
        self.alt_table = QTableWidget()
        self.alt_tab_layout.addWidget(self.alt_gem_flipper_button)
        self.alt_tab_layout.addWidget(self.alt_table)
        self.tabs.addTab(self.alt_tab, "Alt Quality Gem Flipper")

        # Layout for the main window
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.addLayout(self.top_bar)
        main_layout.addWidget(self.tabs)

    def _setup_connections(self) -> None:
        """Connect signals to slots."""
        self.div_start_button.clicked.connect(self.run_div_flipper)
        self.essence_flipper_button.clicked.connect(self.run_essence_flipper)
        self.awakened_gem_flipper_button.clicked.connect(self.run_awakened_gem_flipper)
        self.alt_gem_flipper_button.clicked.connect(self.run_alt_gem_flipper)
        self.update_button.clicked.connect(self.check_for_updates)
        # Add more connections as needed for table interactions

    def _setup_animation_timers(self) -> None:
        """Initialize animation timers."""
        self._copy_timer = QTimer()
        self._copy_timer.setSingleShot(True)
        self._copy_timer.timeout.connect(self._hide_copy_label)

    def _create_header(self) -> None:
        """Create the header widget."""
        self.header = QLabel(HEADER)
        self.header.setStyleSheet(CYBERPUNK_DARK_HEADER_LABEL)

    def _create_table(self) -> None:
        """Create and configure the main table widget."""
        self.table_widget = QTableWidget()
        self.table_widget.setItemDelegate(NoFocusDelegate())
        self.table_widget.setStyleSheet(TABLE_WIDGET)
        self.table_widget.setShowGrid(False)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_widget.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table_widget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)


    def _create_controls(self) -> None:
        """Create control widgets (buttons, combo boxes, labels)."""
        self.controls_layout = QHBoxLayout()
        self.controls_layout.setSpacing(10)

        self._create_league_selector()
        self._create_start_button()
        self._create_status_label()
        self._create_update_button()
        self._create_copy_label()

        # Add flipping buttons
        self.essence_flipper_button = QPushButton("Essence Flipper")
        self.essence_flipper_button.setStyleSheet(START_BUTTON)
        self.controls_layout.addWidget(self.essence_flipper_button)

        self.awakened_gem_flipper_button = QPushButton("Awakened Gem Flipper")
        self.awakened_gem_flipper_button.setStyleSheet(START_BUTTON)
        self.controls_layout.addWidget(self.awakened_gem_flipper_button)

        self.alt_gem_flipper_button = QPushButton("Alt Quality Gem Flipper")
        self.alt_gem_flipper_button.setStyleSheet(START_BUTTON)
        self.controls_layout.addWidget(self.alt_gem_flipper_button)

    def _create_league_selector(self) -> None:
        """Create and populate the league selector combo box."""
        self.league_selector = QComboBox()
        self.league_selector.addItems(
            [league["name"] for league in self.utils.get_current_leagues()]
        )
        self.league_selector.setStyleSheet(COMBO_BOX)
        self.controls_layout.addWidget(self.league_selector)

    def _create_start_button(self) -> None:
        """Create the start/process data button."""
        self.start_button = QPushButton(" Start ")
        self.start_button.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        )
        self.start_button.setStyleSheet(START_BUTTON)
        self.controls_layout.addWidget(self.start_button)

    def _create_status_label(self) -> None:
        """Create the status label."""
        self.status_label = QLabel("Select league")
        self.status_label.setStyleSheet(STATUS_LABEL)
        self.controls_layout.addWidget(self.status_label)
        self.controls_layout.addStretch(1)

    def _create_update_button(self) -> None:
        """Create the update check button."""
        self.update_button = QPushButton(" Check for Updates ")
        self.update_button.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload)
        )
        self.update_button.setStyleSheet(UPDATE_BUTTON)
        self.controls_layout.addWidget(self.update_button)

    def _create_copy_label(self) -> None:
        """Create the copy notification label."""
        self.copy_label = QLabel("")
        self.copy_label.setStyleSheet(COPY_LABEL)
        self.copy_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.copy_label.setVisible(False)

    def _create_footer(self) -> None:
        """Create the footer widget."""
        self.footer = QLabel(FOOTER)
        self.footer.setStyleSheet(FOOTER_LABEL)
        self.footer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.footer.setOpenExternalLinks(True)
        self.footer.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )

    def process_data(self) -> None:
        """Process and display PoE card flipping data."""
        self.status_label.setText("Processing data...")
        QApplication.processEvents()

        try:
            data = self._fetch_and_process_data()
            if data:
                self._display_results(data)
                self.status_label.setText(f"Data loaded successfully for {self.league_selector.currentText()} league")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

    def _fetch_and_process_data(self) -> Optional[List[Dict]]:
        """Fetch and process PoE Ninja data."""
        selected_league = self.league_selector.currentText()
        poe_ninja = PoeNinja()
        poe_ninja.get_data(selected_league)
        divination_data, currency_data, unique_items = self.utils.load_data()

        highscores = self.utils.calculate_highscores(
            divination_data, currency_data, unique_items
        )
        return sorted(highscores.values(), key=lambda x: x["Profit"], reverse=True)

    def _display_results(self, highscores_sorted: List[Dict]) -> None:
        """Display processed results in the table."""
        divine_orb_value = self._get_divine_orb_value()
        if divine_orb_value is None:
            self.status_label.setText("Error: Divine Orb price not found!")
            return

        self._setup_table_structure(highscores_sorted)
        self._populate_table_data(highscores_sorted, divine_orb_value)

    def _get_divine_orb_value(self) -> Optional[float]:
        """Get the current Divine Orb value from currency data."""
        try:
            with open("Data\\Currency.json", "r") as file:
                data = json.load(file)
                return next(
                    (
                        line["receive"]["value"]
                        for line in data["lines"]
                        if line["currencyTypeName"] == "Divine Orb"
                    ),
                    None,
                )
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def _setup_table_structure(self, data: List[Dict]) -> None:
        """Configure table structure and headers."""
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(8)
        self.table_widget.setHorizontalHeaderLabels(
            [
                "#",
                "Name",
                "Type",
                "Total profit",
                "Profit per card",
                "1 card price",
                "Total set price",
                "Reward price",
            ]
        )

        header = self.table_widget.horizontalHeader()
        for col in range(self.table_widget.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table_widget.setColumnWidth(0, 50)
        self.table_widget.setColumnWidth(1, 55)
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(row, 25)

    def _populate_table_data(self, data: List[Dict], divine_value: float) -> None:
        """Populate table with processed data."""
        for row, item in enumerate(data):
            self._add_table_row(row, item, divine_value)

        for col in range(1, self.table_widget.columnCount()):
            self.table_widget.resizeColumnToContents(col)

    def _add_table_row(self, row: int, item: Dict, divine_value: float) -> None:
        """Add a single row of data to the table."""

        # Create conversion functions for currency
        def to_divine(value: float) -> float:
            return round(float(str(value).replace(',', '')) / divine_value, 2)


        # Convert values
        profit_divine = to_divine(item["Profit"])
        profit_per_card_divine = to_divine(item["Profitpercard"])
        total_divine = to_divine(item["Total"])
        sellprice_divine = to_divine(item["Sellprice"])
        cost_divine = to_divine(item["Cost"])

        # Add items to the row
        self._create_table_item(row, 0, str(row + 1))
        self._create_table_item(row, 1, item["Name"], align_left=True)
        self._create_table_item(row, 2, item["Type"], align_left=True)
        self._create_table_item(row, 3, f"{int(item['Profit'])} c ({profit_divine} d)")
        self._create_table_item(
            row, 4, f"{int(item['Profitpercard'])} c ({profit_per_card_divine} d)"
        )
        self._create_table_item(row, 5, f"{int(item['Cost'])} c ({cost_divine} d)")
        self._create_table_item(row, 6, f"{int(item['Total'])} c ({total_divine} d)")
        self._create_table_item(
            row, 7, f"{int(item['Sellprice'])} c ({sellprice_divine} d)"
        )

    def _create_table_item(
        self, row: int, col: int, text: str, align_left: bool = False
    ) -> QTableWidgetItem:
        """Create and configure a table widget item."""
        item = QTableWidgetItem(text)
        item.setBackground(QColor(0, 0, 0, 0))

        if col == 3:
            self._set_item_foreground_color(item, text)

        if not align_left:
            item.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )

        self.table_widget.setItem(row, col, item)
        return item

    @staticmethod
    def _set_item_foreground_color(item: QTableWidgetItem, text: str) -> None:
        """Set item text color based on value (positive/negative)."""
        try:
            value = float(text.split()[0])
            color = "#4CAF50" if value > 0 else "#F44336" if value < 0 else None
            if color:
                item.setForeground(QColor(color))
        except (ValueError, IndexError):
            pass

    def copy_card_name(self, row: int) -> None:
        """Copy card name to clipboard from selected row."""
        item = self.table_widget.item(row, 1)
        QApplication.clipboard().setText(item.text())
        self.show_notification("Copied!")

    def show_notification(self, text: str, duration: int = 2) -> None:
        """Show a temporary notification message."""
        if not hasattr(self, "copy_label"):
            return

        # Stop any ongoing animations/timers
        self._copy_timer.stop()
        if hasattr(self, "fade_animation"):
            self.fade_animation.stop()

        # Position the label
        label_width = 200
        label_height = 30
        label_x = (self.central_widget.width() - label_width) // 2
        label_y = self.central_widget.height() - label_height - 10

        self.copy_label.setGeometry(label_x, label_y, label_width, label_height)
        self.copy_label.setText(text)
        self.copy_label.setStyleSheet(COPY_LABEL)

        # Set up fade-in animation
        self.fade_animation = QPropertyAnimation(self.copy_label, b"opacity")
        self.fade_animation.setDuration(200)
        self.fade_animation.setStartValue(0)
        self.fade_animation.setEndValue(1)
        self.fade_animation.start()

        self.copy_label.setVisible(True)
        self._copy_timer.start(duration * 1000)

    def _hide_copy_label(self) -> None:
        """Hide the copy notification with fade-out animation."""
        if hasattr(self, "fade_animation"):
            self.fade_animation.stop()

        self.fade_animation = QPropertyAnimation(self.copy_label, b"opacity")
        self.fade_animation.setDuration(200)
        self.fade_animation.setStartValue(1)
        self.fade_animation.setEndValue(0)
        self.fade_animation.finished.connect(lambda: self.copy_label.setVisible(False))
        self.fade_animation.start()

    def check_for_updates(self) -> None:
        """Check for application updates."""
        result = self.utils.check_for_updates()

        if not result:
            self.status_label.setText("Failed to check for updates")
            return

        remote_version, remote_description = result

        if remote_version != version:
            self.status_label.setText(f"Update available: v{remote_version}")
            self.show_notification("Update available!", 5)
            self._show_update_message(remote_version, remote_description)
        else:
            self.show_notification("You have the latest version")
            self.status_label.setText("You have the latest version")

    def _show_update_message(
        self, remote_version: str, remote_description: str
    ) -> None:
        """Show update available message box."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Update Available")
        msg_box.setTextFormat(Qt.TextFormat.RichText)
        msg_box.setText(get_update_message(remote_version, version, remote_description))
        msg_box.setStyleSheet(MESSAGE_BOX)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        msg_box.exec()

    def generate_trade_link(self, row: int) -> None:
        """Generate trade link for the selected item and copy to clipboard."""
        item_name = self.table_widget.item(row, 1).text()
        league = self.league_selector.currentText()
        trade_url = self.utils.generate_trade_link(item_name, league)
        QDesktopServices.openUrl(QUrl(trade_url))

    # --- Flipper Logic for Each Tab ---

    def run_div_flipper(self):
        self.status_label.setText("Processing divination card data...")
        QApplication.processEvents()
        try:
            data = self._fetch_and_process_data()
            if data:
                self.display_div_flips(data)
                self.status_label.setText(f"Divination card results for {self.league_selector.currentText()} loaded.")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

    def display_div_flips(self, highscores_sorted):
        headers = ["Name", "Type", "Profit", "Cost", "Stack", "Profit per card", "Total", "Sell price"]
        self.div_table.setColumnCount(len(headers))
        self.div_table.setHorizontalHeaderLabels(headers)
        self.div_table.setRowCount(len(highscores_sorted))
        for row, item in enumerate(highscores_sorted):
            self.div_table.setItem(row, 0, QTableWidgetItem(str(item.get("Name", ""))))
            self.div_table.setItem(row, 1, QTableWidgetItem(str(item.get("Type", ""))))
            self.div_table.setItem(row, 2, QTableWidgetItem(str(item.get("Profit", ""))))
            self.div_table.setItem(row, 3, QTableWidgetItem(str(item.get("Cost", ""))))
            self.div_table.setItem(row, 4, QTableWidgetItem(str(item.get("Stack", ""))))
            self.div_table.setItem(row, 5, QTableWidgetItem(str(item.get("Profitpercard", ""))))
            self.div_table.setItem(row, 6, QTableWidgetItem(str(item.get("Total", ""))))
            self.div_table.setItem(row, 7, QTableWidgetItem(str(item.get("Sellprice", ""))))
        self.div_table.resizeColumnsToContents()

    def run_essence_flipper(self):
        self.status_label.setText("Fetching essence flipping opportunities...")
        QApplication.processEvents()
        league = self.league_selector.currentText()
        try:
            results = get_essence_flips(league)
            self.display_essence_flips(results)
            self.status_label.setText(f"Essence flipping results for {league} loaded.")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

    def display_essence_flips(self, flips):
        headers = ["Essence Type", "Shrieking Value", "Deafening Value", "Profit", "Margin (%)"]
        self.essence_table.setColumnCount(len(headers))
        self.essence_table.setHorizontalHeaderLabels(headers)
        self.essence_table.setRowCount(len(flips))
        for row, flip in enumerate(flips):
            self.essence_table.setItem(row, 0, QTableWidgetItem(flip["essence_type"]))
            self.essence_table.setItem(row, 1, QTableWidgetItem(f"{flip['shrieking_value']:.2f}"))
            self.essence_table.setItem(row, 2, QTableWidgetItem(f"{flip['deafening_value']:.2f}"))
            profit_item = QTableWidgetItem(f"{flip['profit']:.2f}")
            margin_item = QTableWidgetItem(f"{flip['margin']:.2f}")
            if flip['profit'] > 0:
                profit_item.setForeground(QColor('#bfa046'))
                margin_item.setForeground(QColor('#bfa046'))
            elif flip['profit'] < 0:
                profit_item.setForeground(QColor('#b400a1'))
                margin_item.setForeground(QColor('#b400a1'))
            self.essence_table.setItem(row, 3, profit_item)
            self.essence_table.setItem(row, 4, margin_item)
        self.essence_table.resizeColumnsToContents()

    def run_awakened_gem_flipper(self):
        self.status_label.setText("Fetching awakened gem flipping opportunities...")
        QApplication.processEvents()
        league = self.league_selector.currentText()
        try:
            results = get_awakened_gem_flips(league)
            self.display_awakened_gem_flips(results)
            self.status_label.setText(f"Awakened gem flipping results for {league} loaded.")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

    def display_awakened_gem_flips(self, flips):
        headers = ["Gem", "Level 1 Value", "Level 5 Value", "Beast Cost", "Profit", "Margin (%)"]
        self.awakened_table.setColumnCount(len(headers))
        self.awakened_table.setHorizontalHeaderLabels(headers)
        self.awakened_table.setRowCount(len(flips))
        for row, flip in enumerate(flips):
            self.awakened_table.setItem(row, 0, QTableWidgetItem(flip["gem"]))
            self.awakened_table.setItem(row, 1, QTableWidgetItem(f"{flip['level1_value']:.2f}"))
            self.awakened_table.setItem(row, 2, QTableWidgetItem(f"{flip['level5_value']:.2f}"))
            self.awakened_table.setItem(row, 3, QTableWidgetItem(f"{flip['beast_cost']:.2f}"))
            self.awakened_table.setItem(row, 4, QTableWidgetItem(f"{flip['profit']:.2f}"))
            self.awakened_table.setItem(row, 5, QTableWidgetItem(f"{flip['margin']:.2f}"))
        self.awakened_table.resizeColumnsToContents()

    def run_alt_gem_flipper(self):
        self.status_label.setText("Fetching alternate quality gem flipping opportunities...")
        QApplication.processEvents()
        league = self.league_selector.currentText()
        try:
            results = get_lab_alt_gem_flips(league)
            self.display_alt_gem_flips(results)
            self.status_label.setText(f"Alt quality gem flipping results for {league} loaded.")
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")

    def display_alt_gem_flips(self, flips):
        headers = ["Base Gem", "Alt Gem", "Gem Level", "Gem Quality", "Base Value", "Alt Value", "Profit", "Margin (%)"]
        self.alt_table.setColumnCount(len(headers))
        self.alt_table.setHorizontalHeaderLabels(headers)
        self.alt_table.setRowCount(len(flips))
        for row, flip in enumerate(flips):
            self.alt_table.setItem(row, 0, QTableWidgetItem(flip["base"]))
            self.alt_table.setItem(row, 1, QTableWidgetItem(flip["alt"]))
            self.alt_table.setItem(row, 2, QTableWidgetItem(str(flip["gem_level"])))
            self.alt_table.setItem(row, 3, QTableWidgetItem(str(flip["gem_quality"])))
            self.alt_table.setItem(row, 4, QTableWidgetItem(f"{flip['base_value']:.2f}"))
            self.alt_table.setItem(row, 5, QTableWidgetItem(f"{flip['alt_value']:.2f}"))
            self.alt_table.setItem(row, 6, QTableWidgetItem(f"{flip['profit']:.2f}"))
            self.alt_table.setItem(row, 7, QTableWidgetItem(f"{flip['margin']:.2f}"))
        self.alt_table.resizeColumnsToContents()
