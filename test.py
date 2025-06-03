# from PySide6.QtWidgets import (
#     QApplication, QGraphicsView, QGraphicsScene,
#     QGraphicsProxyWidget, QPushButton
# )
# from PySide6.QtCore import Qt


# class MyGraphicsView(QGraphicsView):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         # Cena grande o suficiente para rolar
#         scene = QGraphicsScene(self)
#         scene.setSceneRect(0, 0, 800, 600)

#         # Criar botão normal
#         button = QPushButton("Clique aqui")
#         button.clicked.connect(lambda: print("Botão clicado!"))

#         # Colocar botão dentro da cena
#         proxy = QGraphicsProxyWidget()
#         proxy.setWidget(button)
#         proxy.setPos(100, 100)  # posição do botão
#         scene.addItem(proxy)

#         # Adicionar outros itens para demonstrar rolagem
#         for i in range(5):
#             another = QPushButton(f"Outro {i+1}")
#             another.setMinimumWidth(150)

#             proxy_other = QGraphicsProxyWidget()
#             proxy_other.setWidget(another)
#             proxy_other.setPos(100, 200 + i * 70)
#             scene.addItem(proxy_other)

#         # Configurar a view
#         self.setScene(scene)
#         # self.setRenderHint(self.RenderHint.Antialiasing)
#         self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
#         self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
#         self.setFocusPolicy(Qt.StrongFocus)


# if __name__ == "__main__":
#     app = QApplication([])

#     view = MyGraphicsView()
#     view.setWindowTitle("QGraphicsScene com QPushButton")
#     view.resize(400, 300)
#     view.show()

#     app.exec()


from PySide6.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene,
    QGraphicsProxyWidget, QPushButton, QLineEdit,
    QCheckBox, QComboBox, QSlider, QLabel
)
from PySide6.QtCore import Qt


class WidgetSceneDemo(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 800, 1000)  # Dimensões grandes para permitir rolagem

        y = 20  # posição inicial vertical

        # 1. QLabel
        label = QLabel("Digite algo:")
        self.add_widget(label, 50, y)
        y += 40

        # 2. QLineEdit
        line_edit = QLineEdit()
        self.add_widget(line_edit, 50, y)
        y += 60

        # 3. QCheckBox
        checkbox = QCheckBox("Ativar opção")
        self.add_widget(checkbox, 50, y)
        y += 60

        # 4. QComboBox
        combo = QComboBox()
        combo.addItems(["Opção 1", "Opção 2", "Opção 3"])
        self.add_widget(combo, 50, y)
        y += 60

        # 5. QSlider
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        self.add_widget(slider, 50, y)
        y += 60

        # 6. QPushButton
        button = QPushButton("Enviar")
        button.clicked.connect(lambda: print("Botão clicado!"))
        self.add_widget(button, 50, y)
        y += 60

        # 7. Vários outros para demonstrar rolagem
        for i in range(10):
            more_button = QPushButton(f"Extra {i+1}")
            self.add_widget(more_button, 50, y)
            y += 50

        # View settings
        self.setScene(self.scene)
        # self.setRenderHint(self.RenderHint.Antialiasing)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setFocusPolicy(Qt.StrongFocus)

    def add_widget(self, widget, x, y):
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(widget)
        proxy.setPos(x, y)
        self.scene.addItem(proxy)


if __name__ == "__main__":
    app = QApplication([])

    window = WidgetSceneDemo()
    window.setWindowTitle("QGraphicsScene com vários widgets")
    window.resize(400, 400)
    window.show()

    app.exec()
