import os
import fitz
import sys
import PyQt6
import PyQt6.QtCore as QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication, QScreen, QImage, QPainter


class PDFReader(QWidget):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.current_page = 0
        self.doc = fitz.open(self.path)

        self.setWindowTitle("PDF and EPUB Reader")
        self.screen_size = QGuiApplication.primaryScreen().size()
        self.setGeometry(0, 0, self.screen_size.width(), self.screen_size.height())

        self.showFullScreen()

    def open_page(self, page_number):
        self.current_page = page_number
        page = self.doc.load_page(page_number)
        pix = page.get_pixmap()
        output = "output.png"
        print(pix.alpha)
        image_format = (
            QImage.Format.Format_RGB888
            if pix.alpha == 0
            else QImage.Format.Format_Grayscale16
        )
        image = QImage(pix.samples, pix.width, pix.height, pix.stride, image_format)
        return image

    def paintEvent(self, event: PyQt6.QtGui.QPaintEvent):
        image = self.open_page(self.current_page)
        image = image.scaled(
            self.screen_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio
        )
        painter = QPainter(self)
        painter.drawImage(0, 0, image)

    def keyPressEvent(self, event: PyQt6.QtGui.QKeyEvent):
        if event.key() == 16777234 and self.current_page > 0:
            self.current_page -= 1
            self.update()
        elif event.key() == 16777236 and self.current_page < self.doc.page_count - 1:
            self.current_page += 1
            self.update()


def main():
    app = QApplication([])
    reader = PDFReader("books/famouspaintings.epub")
    reader.showFullScreen()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
