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

    def open_pdf(self, path):
        self.viewer.load_pdf(path)
