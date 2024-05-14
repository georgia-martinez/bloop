import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt


class SongEditor(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)

        # self.setHorizontalHeaderLabels([f"Column {i + 1}" for i in range(columns)])
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.set_column_widths()
        self.currentCellChanged.connect(self.handleCellChanged)

    def set_column_widths(self):
        column_width = 35

        for col in range(self.columnCount()):
            self.setColumnWidth(col, column_width)

    def handleCellChanged(self, current_row, current_column, previous_row, previous_column):
        pass