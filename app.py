import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QScreen

from song_editor_widget import SongEditorWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chiptune Tracker")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.resize(screen_geometry.width(), screen_geometry.height())

        self.song_editor = SongEditorWidget(100, 3)

        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.song_editor)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def run(self):
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.run()
    sys.exit(app.exec_())
