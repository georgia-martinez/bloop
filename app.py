import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QScreen

from song_editor import SongEditor
from playback import Playback


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bloop Tracker")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.resize(screen_geometry.width(), screen_geometry.height())

        self.playback = Playback()
        self.song_editor = SongEditor(20, 2)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.toggle_playback)

        layout = QVBoxLayout()
        layout.addWidget(self.play_button)
        layout.addWidget(self.song_editor)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def run(self):
        self.show()

    def toggle_playback(self):
        song_data = []
        
        for row in range(self.song_editor.rowCount()):
            row_data = []

            for col in range(self.song_editor.columnCount()):
                item = self.song_editor.item(row, col)

                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append(None)

            song_data.append(row_data)
        
        self.playback.play(song_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.run()
    sys.exit(app.exec_())
