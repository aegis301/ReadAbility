import fitz
import os
import sys
import PyQt6
import json
import usbtmc
import logging
import itertools
import PyQt6.QtCore as QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication, QScreen, QPainter, QImage, QKeyEvent

logging.basicConfig(level=logging.CRITICAL)


class BookController:
    def __init__(self, viewer):
        self.viewer = viewer
        self.storage = self.get_storage()
        self.usb_devices = self.list_usb_devices()
        self.viewer.book_paths = [self.get_paths(device) for device in self.usb_devices]
        self.viewer.book_paths = list(itertools.chain(*self.viewer.book_paths))
        self.new_books = []
        for usb in self.usb_devices:
            new_books = self.get_books_from_usb(usb)
            # add new books to list of books
            self.new_books.extend(new_books)

    def open_book(self, path):
        """Opens a book at the given path"""
        # for book in self.storage:
        #     if os.path.join(book["filename"], book["type"]) == path:
        self.viewer.load_book(path)

    def list_usb_devices(self):
        """Returns a list of paths to all connected USB devices"""
        # devices = usbtmc.list_devices()
        # for now, just return every folder in the "../../books" folder, change this later
        path = os.path.join(os.path.dirname(__file__), "../../books")
        devices = [os.path.join(path, folder) for folder in os.listdir(path)]
        return devices
        # return devices

    def get_books_from_usb(self, usb_path):
        """Returns a list of all files on a USB device that are either .pdf or .epub files"""
        return [
            os.path.join(usb_path, file)
            for file in os.listdir(usb_path)
            if file.endswith(".pdf") or file.endswith(".epub")
        ]

    def get_paths(self, path):
        """Returns a list of all files in the given path that are either .pdf or .epub files"""
        return [
            os.path.join(path, file)
            for file in os.listdir(path)
            if file.endswith(".pdf") or file.endswith(".epub")
        ]

    def get_storage(self):
        """Returns the contents of the storage.json file"""
        path = os.path.join(os.path.dirname(__file__), "storage.json")
        storage = json.load(open(path, "r"))["books"]
        return storage
