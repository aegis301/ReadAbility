import os
import fitz
import sys
import PyQt6
import PyQt6.QtCore as QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
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
        if event.key() == 16777234 and self.current_page > 0:
            self.current_page -= 1
            self.update_image()
        elif event.key() == 16777236 and self.current_page < self.doc.page_count - 1:
            self.current_page += 1
            self.update_image()

    def load_pdf(self, path):
        self.doc = fitz.open(path)
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
