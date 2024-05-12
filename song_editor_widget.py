import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import Qt


class SongEditorWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        self.setHorizontalHeaderLabels([f"Column {i + 1}" for i in range(columns)])
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            current_row = self.currentRow()
            next_row = current_row + 1 if current_row < self.rowCount() - 1 else 0  # Wrap around to the first row
            self.selectRow(next_row)
            self.setCurrentCell(next_row, 0)
            
        else:
            super().keyPressEvent(event)
