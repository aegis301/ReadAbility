import pytest
from PyQt6.QtGui import QKeyEvent, QGuiApplication, QPixmap
from PyQt6.QtCore import Qt
from src.View.BookViewer import BookViewer


class TestBookViewer:
    @pytest.fixture
    def viewer(self):
        app = QGuiApplication([])
        return BookViewer()

    # @pytest.mark.parametrize(
    #     "initial_page, key, expected_page",
    #     [
    #         (1, Qt.Key.Key_Left, 0),
    #         (1, Qt.Key.Key_Right, 2),
    #         (1, Qt.Key.Key_Space, None),
    #     ],
    # )
    # def test_keyPressEvent(self, viewer, initial_page, key, expected_page):
    #     viewer.doc = None
    #     viewer.current_page = initial_page
    #     viewer.pages = [None, None, None]
    #     viewer.update_image()
    #     event = QKeyEvent(QKeyEvent.KeyPress, key, Qt.KeyboardModifiers(), "")
    #     viewer.keyPressEvent(event)
    #     assert viewer.current_page == expected_page

    def test_load_pdf(self, viewer):
        viewer.load_pdf("sample3.pdf")
        assert viewer.doc is not None
        assert len(viewer.pages) == viewer.doc.page_count

    # def test_set_image(self, viewer):
    #     pixmap = QPixmap("test.png")
    #     viewer.set_image(pixmap)
    #     assert viewer.image_label.pixmap() == pixmap
