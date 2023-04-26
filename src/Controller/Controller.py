import fitz
import os
import sys
import PyQt6
import PyQt6.QtCore as QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication, QScreen, QPainter, QImage, QKeyEvent


class BookController:
    def __init__(self, viewer):
        self.viewer = viewer
        self.viewer.book_paths = self.get_paths("books")

    def open_pdf(self, path):
        self.viewer.load_pdf(path)

    def list_usb_devices(self):
        """Returns a list of paths to all connected USB devices"""
        return [
            os.path.join("/media", user, device)
            for user in os.listdir("/media")
            for device in os.listdir(os.path.join("/media", user))
        ]

    def get_paths(self, path):
        return [
            os.path.join(path, file)
            for file in os.listdir(path)
            if file.endswith(".pdf") or file.endswith(".epub")
        ]
