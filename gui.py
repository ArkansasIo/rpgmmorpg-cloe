import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
    QMenuBar, QAction, QStackedWidget, QHBoxLayout, QFrame, QToolButton, QMenu
)
import requests

class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel('Welcome to the Procedural Generator Suite!')
        label.setStyleSheet('font-size: 18px; font-weight: bold;')
        layout.addWidget(label)
        layout.addStretch()
        self.setLayout(layout)

class GeneratorScreen(QWidget):
    def __init__(self, gen_type):
        super().__init__()
        self.gen_type = gen_type
        layout = QVBoxLayout()
        self.label = QLabel(f'{gen_type.capitalize()} Generator')
        self.result = QLabel('')
        self.gen_btn = QPushButton('Generate')
        layout.addWidget(self.label)
        layout.addWidget(self.gen_btn)
        layout.addWidget(self.result)
        self.setLayout(layout)
        self.gen_btn.clicked.connect(self.generate)

    def generate(self):
        url = f'http://127.0.0.1:5000/api/{self.gen_type}'
        try:
            resp = requests.get(url)
            self.result.setText(str(resp.json()))
        except Exception as e:
            self.result.setText(f'Error: {e}')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Procedural Generator Suite')
        self.showMaximized()

        # Top menu bar
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')
        self.exit_action = QAction('Exit', self)
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)

        # Central widget with horizontal layout
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Left sidebar (main and submenus)
        self.left_sidebar = QFrame()
        self.left_sidebar.setFrameShape(QFrame.StyledPanel)
        self.left_sidebar.setFixedWidth(200)
        left_layout = QVBoxLayout(self.left_sidebar)
        left_layout.setContentsMargins(10, 10, 10, 10)

        # Main menu buttons with submenus
        self.city_menu_btn = QToolButton()
        self.city_menu_btn.setText('City')
        self.city_menu_btn.setPopupMode(QToolButton.MenuButtonPopup)
        city_menu = QMenu()
        city_gen_action = QAction('City Generator', self)
        city_menu.addAction(city_gen_action)
        self.city_menu_btn.setMenu(city_menu)

        self.dungeon_menu_btn = QToolButton()
        self.dungeon_menu_btn.setText('Dungeon')
        self.dungeon_menu_btn.setPopupMode(QToolButton.MenuButtonPopup)
        dungeon_menu = QMenu()
        dungeon_gen_action = QAction('Dungeon Generator', self)
        dungeon_menu.addAction(dungeon_gen_action)
        self.dungeon_menu_btn.setMenu(dungeon_menu)

        self.village_menu_btn = QToolButton()
        self.village_menu_btn.setText('Village')
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
        self.city_screen = GeneratorScreen('city')
        self.dungeon_screen = GeneratorScreen('dungeon')
        self.village_screen = GeneratorScreen('village')
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.city_screen)
        self.stack.addWidget(self.dungeon_screen)
        self.stack.addWidget(self.village_screen)

        # Add widgets to main layout
        main_layout.addWidget(self.left_sidebar)
        main_layout.addWidget(self.stack)
        main_layout.setStretch(1, 1)

        self.setCentralWidget(main_widget)
        self.show_main_menu()

        # Connect sidebar actions
        city_gen_action.triggered.connect(lambda: self.show_generator('city'))
        dungeon_gen_action.triggered.connect(lambda: self.show_generator('dungeon'))
        village_gen_action.triggered.connect(lambda: self.show_generator('village'))

    def show_main_menu(self):
        self.stack.setCurrentWidget(self.main_menu)

    def show_generator(self, gen_type):
        if gen_type == 'city':
            self.stack.setCurrentWidget(self.city_screen)
        elif gen_type == 'dungeon':
            self.stack.setCurrentWidget(self.dungeon_screen)
        elif gen_type == 'village':
            self.stack.setCurrentWidget(self.village_screen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
