import os
import fitz
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication, QScreen, QImage, QPainter


def open_pdf_for_pyqt(path="books/sample2.pdf"):
    """Open a pdf file and return a QImage object"""
    doc = fitz.open(path)
    page = doc.load_page(0)
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


def main():
    image = open_pdf_for_pyqt()

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("PDF and EPUB Reader")
    screen_size = app.primaryScreen().size()
    window.setGeometry(0, 0, screen_size.width(), screen_size.height())
    window.showFullScreen()

    image = image.scaled(screen_size, Qt.AspectRatioMode.KeepAspectRatio)
    window.paintEvent = lambda event: QPainter(window).drawImage(0, 0, image)
    window.showFullScreen()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
