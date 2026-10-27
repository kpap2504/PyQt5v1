import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 App")
        self.resize(300, 200)

        # Layout and widgets
        layout = QVBoxLayout()
        self.label = QLabel("Hello, PyQt5!")
        button = QPushButton("Click Me")
        
        button.clicked.connect(self.on_click)

        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)

    def on_click(self):
        self.label.setText("You clicked me!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
