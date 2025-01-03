# https://wayland.app/protocols/wlr-screencopy-unstable-v1
# from PySide6.QtCore import QPropertyAnimation, QEasingCurve
# from PySide6.QtGui import QColor
# from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
# from PySide6.QtWidgets import QGraphicsColorizeEffect

# class AnimatedColorButton(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         # Configuração do layout e botão
#         self.layout = QVBoxLayout(self)
#         self.button = QPushButton("Clique para animar", self)
#         self.layout.addWidget(self.button)
        
#         # Configurar o efeito de coloração
#         self.color_effect = QGraphicsColorizeEffect(self.button)
#         self.button.setGraphicsEffect(self.color_effect)
        
#         # Conectar o clique do botão
#         self.button.clicked.connect(self.animate_color)

#     def animate_color(self):
#         # Configuração inicial e final da cor
#         self.animation = QPropertyAnimation(self.color_effect, b"color")
#         self.animation.setDuration(1000)  # Duração em milissegundos
#         self.animation.setStartValue(QColor(0, 0, 255))  # Azul
#         self.animation.setEndValue(QColor(0, 255, 0))    # Verde
#         self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # Suavização
        
#         self.animation.start()

# if __name__ == "__main__":
#     app = QApplication([])
#     window = AnimatedColorButton()
#     window.resize(300, 200)
#     window.show()
#     app.exec()
from PySide6.QtCore import QPropertyAnimation, QObject, Property, Signal, QParallelAnimationGroup
# from PySide6.QtGui import 
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsOpacityEffect

class BackgroundAnimator(QObject):
    progress_changed = Signal(float)

    def __init__(self):
        super().__init__()
        self._progress = 0.0

    def get_progress(self):
        return self._progress

    def set_progress(self, progress):
        self._progress = progress
        self.progress_changed.emit(progress)

    # Registrar como uma propriedade do Qt
    progress = Property(float, get_progress, set_progress)

class AnimatedMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transição de Fundo")
        self.setGeometry(100, 100, 800, 600)

        # Configuração inicial do estilo
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('/home/user/imagem1.jpeg');
            }
        """)

        # Configurar o animador
        self.animator = BackgroundAnimator()
        self.animator.progress_changed.connect(self.update_background)

        # Clique para iniciar a animação
        self.mousePressEvent = self.animate_transition

    def update_background(self, progress):
        # Atualiza o estilo dinamicamente
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('/home/user/imagem2.jpg');
            }
        """)

    def animate_transition(self, event):
        # Configurar a animação
        self.animation = QPropertyAnimation(self.animator, b"progress")
        self.animation.setDuration(2000)  # Duração em milissegundos
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        # self.animation.start()

        effect = QGraphicsOpacityEffect(self)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setStartValue(0)
        self.anim_2.setEndValue(1)
        self.anim_2.setDuration(2500)

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()

if __name__ == "__main__":
    app = QApplication([])

    # Certifique-se de ter 'imagem1.jpg' e 'imagem2.jpg' no mesmo diretório
    window = AnimatedMainWindow()
    window.show()

    app.exec()
