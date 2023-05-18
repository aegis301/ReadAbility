import pytest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from src.View.BookViewer import BookViewer

app = QApplication([])


@pytest.fixture
def book_viewer():
    viewer = BookViewer()
    yield viewer
    viewer.close()


def test_initialization(book_viewer):
    assert book_viewer.windowTitle() == "PDF Viewer"
    assert isinstance(book_viewer.image_label, QLabel)
    assert book_viewer.current_page == 0


def test_set_image(book_viewer):
    pixmap = QPixmap(100, 100)
    book_viewer.set_image(pixmap)
    assert book_viewer.image_label.pixmap() == pixmap


def test_keyPressEvent_left(book_viewer):
    # Load a book with 3 pages
    book_viewer.load_book("path/to/book.pdf", page=1)
    assert book_viewer.current_page == 1

    # Simulate a Key_Left press
    QTest.keyPress(book_viewer, Qt.Key.Key_Left)

    # Verify that the current page is decremented
    assert book_viewer.current_page == 0


def test_keyPressEvent_right(book_viewer):
    # Load a book with 3 pages
    book_viewer.load_book("path/to/book.pdf", page=1)
    assert book_viewer.current_page == 1

    # Simulate a Key_Right press
    QTest.keyPress(book_viewer, Qt.Key.Key_Right)

    # Verify that the current page is incremented
    assert book_viewer.current_page == 2


def test_keyPressEvent_space(book_viewer):
    # Simulate a Key_Space press
    QTest.keyPress(book_viewer, Qt.Key.Key_Space)

    # Verify that the dialog box is shown
    assert book_viewer.dialog is not None


def test_keyPressEvent_escape(book_viewer):
    # Simulate a Key_Escape press
    QTest.keyPress(book_viewer, Qt.Key.Key_Escape)

    # Verify that the dialog box is closed
    assert book_viewer.dialog is None
