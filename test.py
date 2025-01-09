# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QRadioButton, QButtonGroup, QLabel


# class RadioButtonExample(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Exemplo de Botões de Rádio")

#         # Layout principal
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout(central_widget)

#         # Label para exibir a opção selecionada
#         self.label = QLabel("Nenhuma opção selecionada")
#         layout.addWidget(self.label)

#         # Grupo de botões de rádio
#         self.button_group = QButtonGroup(self)
#         self.button_group.buttonToggled.connect(self.on_button_toggled)

#         # Cria os botões de rádio
#         radio_button1 = QRadioButton("Opção 1")
#         radio_button2 = QRadioButton("Opção 2")
#         radio_button3 = QRadioButton("Opção 3")

#         # Adiciona os botões ao grupo
#         self.button_group.addButton(radio_button1)
#         self.button_group.addButton(radio_button2)
#         self.button_group.addButton(radio_button3)

#         # Adiciona os botões ao layout
#         layout.addWidget(radio_button1)
#         layout.addWidget(radio_button2)
#         layout.addWidget(radio_button3)

#     def on_button_toggled(self, button, checked):
#         if checked:
#             self.label.setText(f"Selecionado: {button.text()}")


# # Inicializa a aplicação
# def main():
#     app = QApplication([])
#     window = RadioButtonExample()
#     window.show()
#     app.exec()


# if __name__ == "__main__":
#     main()

from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        slider = QSlider()

        slider.setMinimum(-10)
        slider.setMaximum(3)
        # Or: widget.setRange(-10,3)

        slider.setSingleStep(3)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(slider)

    def value_changed(self, value):
        print(value)

    def slider_position(self, position):
        print("position", position)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


# Inicializa a aplicação
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()