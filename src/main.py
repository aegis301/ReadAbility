import sys

from PyQt6.QtWidgets import QApplication
from View.BookViewer import BookViewer
from Controller.Controller import BookController


def main():
    app = QApplication([])
    viewer = BookViewer()
    controller = BookController(viewer)
    controller.open_pdf("books/sample3.pdf")
    viewer.showFullScreen()
    app.exec()


if __name__ == "__main__":
    main()
