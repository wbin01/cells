from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QRadioButton, QButtonGroup, QLabel


class RadioButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Botões de Rádio")

        # Layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Label para exibir a opção selecionada
        self.label = QLabel("Nenhuma opção selecionada")
        layout.addWidget(self.label)

        # Grupo de botões de rádio
        self.button_group = QButtonGroup(self)
        self.button_group.buttonToggled.connect(self.on_button_toggled)

        # Cria os botões de rádio
        radio_button1 = QRadioButton("Opção 1")
        radio_button2 = QRadioButton("Opção 2")
        radio_button3 = QRadioButton("Opção 3")

        # Adiciona os botões ao grupo
        self.button_group.addButton(radio_button1)
        self.button_group.addButton(radio_button2)
        self.button_group.addButton(radio_button3)

        # Adiciona os botões ao layout
        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)
        layout.addWidget(radio_button3)

    def on_button_toggled(self, button, checked):
        if checked:
            self.label.setText(f"Selecionado: {button.text()}")


# Inicializa a aplicação
def main():
    app = QApplication([])
    window = RadioButtonExample()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
