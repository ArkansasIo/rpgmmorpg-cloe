from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog
from PyQt5.QtGui import QPainter, QColor, QFont
# Ensure QWidget is imported before MapRenderWidget
from PyQt5.QtWidgets import QWidget
# Widget to render 2D map data as a grid
class MapRenderWidget(QWidget):
    def __init__(self, map_data=None, cell_size=18, parent=None):
        super().__init__(parent)
        self.map_data = map_data or []
        self.cell_size = cell_size
        self.setMinimumSize(400, 400)

    def set_map(self, map_data):
        self.map_data = map_data
        self.update()

    def paintEvent(self, event):
        if not self.map_data:
            return
        qp = QPainter(self)
        qp.setFont(QFont('Consolas', int(self.cell_size*0.7)))
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                rect_x = x * self.cell_size
                rect_y = y * self.cell_size
                # Color by cell type
                color = QColor('#222')
                if cell in ('#', 'M'): color = QColor('#888')  # Wall/mountain
                elif cell in ('~',): color = QColor('#3af')    # Water
                elif cell in ('T',): color = QColor('#2a4')    # Forest
                elif cell in ('D',): color = QColor('#edc9af') # Desert
                elif cell in ('O',): color = QColor('#0ff')    # Oasis
                elif cell in ('U',): color = QColor('#ffe4b5') # Dune
                elif cell in ('R',): color = QColor('#a0522d') # Rock
                elif cell in ('*',): color = QColor('#fff')    # Snow/ice
                elif cell in ('H',): color = QColor('#bdb76b') # Hill
                elif cell in ('V',): color = QColor('#f0f')    # Village
                elif cell in ('L',): color = QColor('#0ff')    # Lake
                elif cell in ('S',): color = QColor('#228b22') # Swamp
                elif cell in (' ','.'): color = QColor('#222') # Empty/ground
                qp.fillRect(rect_x, rect_y, self.cell_size, self.cell_size, color)
                qp.setPen(QColor('#333'))
                qp.drawRect(rect_x, rect_y, self.cell_size, self.cell_size)
                qp.setPen(QColor('#b9f2ff'))
                qp.drawText(rect_x+2, rect_y+self.cell_size-4, str(cell))
        qp.end()
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
    QMenuBar, QAction, QStackedWidget, QHBoxLayout, QFrame, QToolButton, QMenu
)
import requests

class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        from PyQt5.QtCore import Qt
        layout = QVBoxLayout()
        label = QLabel('Welcome to the Procedural Generator Suite!')
        label.setStyleSheet('font-size: 22px; font-weight: bold; color: #333; margin-top: 30px;')
        layout.addWidget(label, alignment=Qt.AlignHCenter)
        layout.addStretch()
        self.setLayout(layout)

class GeneratorScreen(QWidget):
    def __init__(self, gen_type):
        super().__init__()
        self.gen_type = gen_type
        layout = QVBoxLayout()
        self.label = QLabel(f'{gen_type.capitalize()} Generator')
        self.label.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 10px;')
        self.result = QLabel('')
        self.result.setStyleSheet('background: #222; color: #b9f2ff; font-family: monospace; border-radius: 6px; padding: 10px; min-height: 200px;')
        self.result.setWordWrap(True)
        self.map_widget = MapRenderWidget()
        self.map_widget.hide()
        self.gen_btn = QPushButton('Generate')
        self.gen_btn.setStyleSheet('background: #4e8cff; color: white; font-weight: bold; padding: 8px 20px; border-radius: 5px;')
        from PyQt5.QtCore import Qt
        layout.addWidget(self.label)
        layout.addWidget(self.gen_btn, alignment=Qt.AlignHCenter)
        layout.addWidget(self.result)
        layout.addWidget(self.map_widget)
        layout.addStretch()
        self.setLayout(layout)
        self.gen_btn.clicked.connect(self.generate)

    def generate(self):
        url = f'http://127.0.0.1:5000/api/{self.gen_type}'
        try:
            resp = requests.get(url)
            data = resp.json()
            # If the response is a map (list of strings), render it
            if isinstance(data, list) and all(isinstance(row, str) for row in data):
                self.result.hide()
                self.map_widget.set_map([list(row) for row in data])
                self.map_widget.show()
            else:
                self.map_widget.hide()
                self.result.setText(str(data))
                self.result.show()
        except Exception as e:
            self.map_widget.hide()
            self.result.setText(f'Error: {e}')
            self.result.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Procedural Generator Suite')
        self.setMinimumSize(1024, 700)
        self.showMaximized()


        # Top menu bar
        self.menu = self.menuBar()

        # File menu
        self.file_menu = self.menu.addMenu('File')
        self.file_menu.addAction('New', self.action_new)
        self.file_menu.addAction('Open...', self.action_open)
        self.file_menu.addAction('Save...', self.action_save)
        self.file_menu.addAction('Export...', self.action_export)
        self.file_menu.addSeparator()
        self.file_menu.addAction('Exit', self.close)


        # Generators menu (actions added after widget setup)
        self.gen_menu = self.menu.addMenu('Generators')


        # Tools menu (future stubs)
        self.tools_menu = self.menu.addMenu('Tools')
        self.tools_menu.addAction('Import...', self.action_import)
        self.tools_menu.addAction('Settings...', self.action_settings)

        # Help menu
        self.help_menu = self.menu.addMenu('Help')
        self.help_menu.addAction('About', self.action_about)
        self.help_menu.addAction('Help', self.action_help)

    def action_new(self):
        QMessageBox.information(self, 'New', 'New project (stub).')

    def action_open(self):
        QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')

    def action_save(self):
        QFileDialog.getSaveFileName(self, 'Save File', '', 'All Files (*)')

    def action_export(self):
        QFileDialog.getSaveFileName(self, 'Export File', '', 'PNG Image (*.png);;All Files (*)')

    def action_import(self):
        QFileDialog.getOpenFileName(self, 'Import File', '', 'All Files (*)')

    def action_settings(self):
        QMessageBox.information(self, 'Settings', 'Settings dialog (stub).')

    def action_about(self):
        QMessageBox.about(self, 'About', 'Procedural Generator Suite\nVersion 1.0\nPowered by PyQt5')

    def action_help(self):
        QMessageBox.information(self, 'Help', 'Help and documentation (stub).')

        # Central widget with horizontal layout
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Left sidebar (main and submenus)
        self.left_sidebar = QFrame()
        self.left_sidebar.setFrameShape(QFrame.StyledPanel)
        self.left_sidebar.setFixedWidth(220)
        self.left_sidebar.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #232b3a, stop:1 #1a1f29); border-right: 2px solid #3a4252;')
        left_layout = QVBoxLayout(self.left_sidebar)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)

        # Sidebar header/logo
        from PyQt5.QtCore import Qt
        sidebar_header = QLabel('🧭<br><b>GENERATOR</b>')
        sidebar_header.setStyleSheet('font-size: 26px; color: #b9f2ff; background: #1a1f29; padding: 32px 0 18px 0; border-bottom: 1px solid #3a4252; text-align: center;')
        sidebar_header.setAlignment(Qt.AlignHCenter)
        left_layout.addWidget(sidebar_header)

        # Main menu buttons with submenus and icons
        self.city_menu_btn = QToolButton()
        self.city_menu_btn.setText('  City')
        self.city_menu_btn.setStyleSheet('color: #b9f2ff; font-size: 16px; padding: 18px 0 18px 24px; text-align: left;')
        self.city_menu_btn.setPopupMode(QToolButton.MenuButtonPopup)
        city_menu = QMenu()
        city_gen_action = QAction('City Generator', self)
        city_menu.addAction(city_gen_action)
        self.city_menu_btn.setMenu(city_menu)

        self.dungeon_menu_btn = QToolButton()
        self.dungeon_menu_btn.setText('  Dungeon')
        self.dungeon_menu_btn.setStyleSheet('color: #b9f2ff; font-size: 16px; padding: 18px 0 18px 24px; text-align: left;')
        self.dungeon_menu_btn.setPopupMode(QToolButton.MenuButtonPopup)
        dungeon_menu = QMenu()
        dungeon_gen_action = QAction('Dungeon Generator', self)
        dungeon_menu.addAction(dungeon_gen_action)
        self.dungeon_menu_btn.setMenu(dungeon_menu)

        self.village_menu_btn = QToolButton()
        self.village_menu_btn.setText('  Village')
        self.village_menu_btn.setStyleSheet('color: #b9f2ff; font-size: 16px; padding: 18px 0 18px 24px; text-align: left;')
        self.village_menu_btn.setPopupMode(QToolButton.MenuButtonPopup)
        village_menu = QMenu()
        village_gen_action = QAction('Village Generator', self)
        village_menu.addAction(village_gen_action)
        self.village_menu_btn.setMenu(village_menu)

        left_layout.addWidget(self.city_menu_btn)
        left_layout.addWidget(self.dungeon_menu_btn)
        left_layout.addWidget(self.village_menu_btn)
        left_layout.addStretch()

        # Central stacked widget
        self.stack = QStackedWidget()
        self.main_menu = MainMenu(self)
        self.generator_screens = {
            'city': GeneratorScreen('city'),
            'dungeon': GeneratorScreen('dungeon'),
            'village': GeneratorScreen('village'),
            'maze': GeneratorScreen('maze'),
            'earthlike': GeneratorScreen('earthlike'),
            'dnd': GeneratorScreen('dnd5e'),
            'fantasy': GeneratorScreen('fantasy'),
            'desert': GeneratorScreen('desert'),
        }
        self.stack.addWidget(self.main_menu)
        for screen in self.generator_screens.values():
            self.stack.addWidget(screen)

        # Add widgets to main layout
        main_layout.addWidget(self.left_sidebar)
        main_layout.addWidget(self.stack)
        main_layout.setStretch(1, 1)


        self.setCentralWidget(main_widget)
        self.show_main_menu()

        # Now that self.stack and screens exist, connect generator menu actions
        self.gen_menu.addAction('City', lambda: self.show_generator('city'))
        self.gen_menu.addAction('Dungeon', lambda: self.show_generator('dungeon'))
        self.gen_menu.addAction('Village', lambda: self.show_generator('village'))
        self.gen_menu.addAction('Maze', lambda: self.show_generator('maze'))
        self.gen_menu.addAction('Earthlike', lambda: self.show_generator('earthlike'))

        # Connect sidebar actions
        city_gen_action.triggered.connect(lambda: self.show_generator('city'))
        dungeon_gen_action.triggered.connect(lambda: self.show_generator('dungeon'))
        village_gen_action.triggered.connect(lambda: self.show_generator('village'))

    def show_main_menu(self):
        self.stack.setCurrentWidget(self.main_menu)

    def show_generator(self, gen_type):
        screen = self.generator_screens.get(gen_type)
        if screen:
            self.stack.setCurrentWidget(screen)
        else:
            QMessageBox.warning(self, 'Not Implemented', f'Generator "{gen_type}" not implemented.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
