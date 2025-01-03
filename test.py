# import random
# import pyautogui
# import cv2
# import numpy as np

# import pyscreenshot as ImageGrab
# from PIL import Image, ImageFilter, ImageEnhance

# from PySide6.QtWidgets import QApplication, QWidget
# from PySide6.QtGui import QPainter, QPixmap, QPaintEvent
# from PySide6 import QtWidgets, QtGui, QtCore

# class CustomWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(400, 300)
#         self.background_image = QPixmap("/home/user/fullscreen.png")
#         self.installEventFilter(self)

#     def paintEvent(self, event: QPaintEvent):
#         painter = QPainter(self)
#         painter.drawPixmap(self.rect(), self.background_image)
#         painter.end()

#     def eventFilter(
#             self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
#         if event.type() == QtCore.QEvent.MouseButtonPress:
#             def add_gaussian_noise(mean=0, var=0.01):
#                 image = ImageGrab.grab()
#                 image = np.array(image)
#                 sigma = var ** 0.5
#                 gaussian_noise = np.random.normal(mean, sigma, image.shape)
#                 noisy_image = np.clip(image + gaussian_noise, 0, 255)
#                 noisy_image.astype(np.uint8)
#                 cv2.imwrite("/home/user/fullscreen.jpg", noisy_image)

#             def add_gaussian_blur():
#                 screenshot = ImageGrab.grab()
#                 screenshot = np.array(screenshot)
#                 screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
#                 blurred_image = cv2.GaussianBlur(screenshot, (315, 315), 0)
#                 cv2.imwrite("/home/user/fullscreen.jpg", blurred_image)

#             def add_pillow_gaussian_blur():
#                 im = ImageGrab.grab()
#                 # im = im.filter(ImageFilter.GaussianBlur(radius=100))

#                 im = im.convert("RGB")
#                 imagem_borrada = im.filter(ImageFilter.GaussianBlur(radius=100))
#                 realce = Image.new("RGB", im.size, (32, 32, 32))
#                 realce = ImageEnhance.Brightness(realce).enhance(0.9)
#                 im = Image.blend(imagem_borrada, realce, alpha=0.1)
                
#                 # enhancer = ImageEnhance.Brightness(im)
#                 # im = enhancer.enhance(0.9)

#                 # im = im.convert("RGB")
#                 # pixels = im.load()
#                 # largura, altura = im.size
#                 # for _ in range(100000):
#                 #     x = random.randint(1, largura - 5)
#                 #     y = random.randint(1, altura - 5)
#                 #     r, g, b = pixels[x, y]
#                 #     ruido = lambda valor: max(0, min(255, valor + random.randint(-20, 20)))
#                 #     pixels[x, y] = (ruido(r), ruido(g), ruido(b))

#                 im.save("/home/user/fullscreen.png")
            
#             add_pillow_gaussian_blur()
#             # add_gaussian_blur()
#             self.background_image = QPixmap("/home/user/fullscreen.png")
#             self.update()
            
#         return QtWidgets.QMainWindow.eventFilter(self, watched, event)

# if __name__ == "__main__":
#     app = QApplication([])
#     widget = CustomWidget()
#     widget.resize(400, 300)
#     widget.show()
#     app.exec()
# # https://wayland.app/protocols/wlr-screencopy-unstable-v1
import time

from PySide6.QtCore import Slot, QThreadPool, QTimer
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QApplication,
)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(250, 100)
        self.setWindowTitle("Sheep Picker")

        self.sheep_number = 1
        self.timer = QTimer()
        self.picked_sheep_label = QLabel()
        self.counted_sheep_label = QLabel()

        self.layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.thread_manager = QThreadPool()
        self.pick_sheep_button = QPushButton("Pick a sheep!")

        self.layout.addWidget(self.counted_sheep_label)
        self.layout.addWidget(self.pick_sheep_button)
        self.layout.addWidget(self.picked_sheep_label)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.timer.timeout.connect(self.count_sheep)
        self.pick_sheep_button.pressed.connect(self.pick_sheep_safely)

        self.timer.start()

    @Slot()
    def count_sheep(self):
        self.sheep_number += 1
        self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")

    @Slot()
    def pick_sheep(self):
        self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
        time.sleep(5)  # This function doesn't affect GUI responsiveness anymore...

    @Slot()
    def pick_sheep_safely(self):
        self.thread_manager.start(self.pick_sheep)  # ...since .start() is used!


if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()