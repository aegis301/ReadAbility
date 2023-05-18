import sys
import logging

from PyQt6.QtWidgets import QApplication
from View.BookViewer import BookViewer
from Controller.Controller import BookController


def main():
    logging.basicConfig(level=logging.CRITICAL)
    app = QApplication([])
    viewer = BookViewer()
    controller = BookController(viewer)
    controller.open_book(controller.viewer.book_paths[3])
    viewer.showFullScreen()
    app.exec()


if __name__ == "__main__":
    main()
