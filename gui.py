import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMenuBar, QAction, QStackedWidget
import requests

class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()
        self.city_btn = QPushButton('City Generator')
        self.dungeon_btn = QPushButton('Dungeon Generator')
        self.village_btn = QPushButton('Village Generator')
        layout.addWidget(self.city_btn)
        layout.addWidget(self.dungeon_btn)
        layout.addWidget(self.village_btn)
        self.setLayout(layout)
        self.city_btn.clicked.connect(lambda: parent.show_generator('city'))
        self.dungeon_btn.clicked.connect(lambda: parent.show_generator('dungeon'))
        self.village_btn.clicked.connect(lambda: parent.show_generator('village'))

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
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')
        self.exit_action = QAction('Exit', self)
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)
        self.stack = QStackedWidget()
        self.main_menu = MainMenu(self)
        self.city_screen = GeneratorScreen('city')
        self.dungeon_screen = GeneratorScreen('dungeon')
        self.village_screen = GeneratorScreen('village')
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.city_screen)
        self.stack.addWidget(self.dungeon_screen)
        self.stack.addWidget(self.village_screen)
        self.setCentralWidget(self.stack)
        self.show_main_menu()

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
