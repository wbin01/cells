# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
# from PySide6.QtSvgWidgets import QSvgWidget
# from PySide6.QtCore import Qt


# class HoverSVGExample(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Alterar cor do SVG no hover")

#         # Widget central e layout
#         central_widget = QWidget()
#         layout = QVBoxLayout(central_widget)
#         self.setCentralWidget(central_widget)

#         # SVG Widget
#         self.svg_orig = QSvgWidget()
#         self.svg_orig.load("data/radio.svg")
#         self.svg_orig.setFixedSize(200, 200)

#         self.svg_hover = QSvgWidget()
#         self.svg_hover.load("data/radio.svg")
#         self.svg_hover.setFixedSize(200, 200)

#         self.svg_widget = self.svg_orig
#         layout.addWidget(self.svg_widget, alignment=Qt.AlignCenter)

#         # Adiciona eventos de mouse para hover
#         self.svg_widget.setAttribute(Qt.WA_Hover, True)
#         self.svg_widget.enterEvent = self.on_hover_enter
#         self.svg_widget.leaveEvent = self.on_hover_leave

#     def modify_svg(self, svg_content, stroke_color):
#         """Modifica a cor da borda do SVG."""
#         return svg_content.replace('stroke="black"', f'stroke="{stroke_color}"')

#     def on_hover_enter(self, event):
#         """Altera para o SVG modificado no estado hover."""
#         self.svg_widget.load(self.hover_svg)

#     def on_hover_leave(self, event):
#         """Restaura o SVG original."""
#         self.svg_widget.load("data/radio.svg")


# # Executa a aplicação
# def main():
#     app = QApplication([])
#     window = HoverSVGExample()
#     window.show()
#     app.exec()


# if __name__ == "__main__":
#     main()

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import QByteArray


class SvgFromMemoryExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSvgWidget com QByteArray")

        # Widget central e layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Conteúdo SVG como string
        svg_content = self.load_svg("data/radio.svg")
        print(svg_content)

        # Converte o conteúdo SVG para QByteArray
        svg_data = QByteArray(svg_content.encode('utf-8'))

        # Cria o QSvgWidget e carrega o SVG do QByteArray
        svg_widget = QSvgWidget()
        svg_widget.load(svg_data)
        svg_widget.setFixedSize(16, 16)

        # Adiciona o QSvgWidget ao layout
        layout.addWidget(svg_widget)

    def load_svg(self, path):
        """Carrega o conteúdo do arquivo SVG."""
        center = self.rgba_to_hex(45, 90, 165)
        border = self.rgba_to_hex(45, 90, 165)
        with open(path, "r") as f:
            cont = f.read()
        cont = cont.replace(
            'fill="#1a1a1a"', f'fill="{border}" fill-opacity=".9"').replace(
            'fill="#e5e5e5"', f'fill="{center}" fill-opacity=".5"')
            
        return cont

    def rgba_to_hex(self, r, g, b):
        """Converte valores RGBA para o formato hexadecimal."""
        return f"#{r:02X}{g:02X}{b:02X}".lower()


# Executa a aplicação
def main():
    app = QApplication([])
    window = SvgFromMemoryExample()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
