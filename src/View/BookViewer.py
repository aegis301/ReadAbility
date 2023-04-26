import os
import fitz
import sys
import PyQt6
import PyQt6.QtCore as QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QDialog,
    QAbstractItemView,
    QListWidget,
)
from PyQt6.QtGui import QGuiApplication, QScreen, QPainter, QImage, QKeyEvent, QPixmap


class BookViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PDF Viewer")
        self.image_label = QLabel()
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        self.current_page = 0

    def set_image(self, image):
        self.image_label.setPixmap(image)

    def keyPressEvent(self, event: PyQt6.QtGui.QKeyEvent):
        print(event.key())
        if event.key() == QtCore.Qt.Key.Key_Left and self.current_page > 0:
            self.current_page -= 1
            self.update_image()
        elif (
            event.key() == QtCore.Qt.Key.Key_Right
            and self.current_page < self.doc.page_count - 1
        ):
            self.current_page += 1
            self.update_image()
        elif event.key() == QtCore.Qt.Key.Key_Space:
            self.show_dialog_box()
        elif event.key() == QtCore.Qt.Key.Key_Escape:
            self.close_dialog_box()

    def show_dialog_box(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Dialog Box")
        # show list of book paths
        self.list_widget = QListWidget(self.dialog)
        for path in self.book_paths:
            self.list_widget.addItem(path)
        self.list_widget.clicked.connect(self.clicked_list_item)
        self.list_widget.itemActivated.connect(self.activated_list_item)
        self.dialog_layout = QVBoxLayout(self.dialog)
        self.dialog_layout.addWidget(self.list_widget)
        self.dialog.exec()

    def clicked_list_item(self, item):
        path = self.book_paths[item.row()]
        self.load_pdf(path)
        self.close_dialog_box()

    def activated_list_item(self, item):
        path = item.text()
        self.load_pdf(path)
        self.close_dialog_box()

    def close_dialog_box(self):
        self.dialog.close()

    def load_pdf(self, path):
        self.doc = fitz.open(path)
        self.current_page = 0
        self.pages = [self.doc.load_page(i) for i in range(self.doc.page_count)]
        self.update_image()

    def update_image(self):
        page = self.pages[self.current_page]
        pix = page.get_pixmap()
        image_format = (
            QImage.Format.Format_RGB888
            if pix.alpha == 0
            else QImage.Format.Format_Grayscale16
        )
        image = QImage(pix.samples, pix.width, pix.height, pix.stride, image_format)
        pixmap = QPixmap.fromImage(image)
        self.set_image(pixmap)
