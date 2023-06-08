import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QWidget,
    QProgressBar,
)
from PyQt6.QtCore import Qt, QTimer


class LoadingPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading Page")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.loading_label = QLabel("Initializing...")
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loading_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.central_widget.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

        self.loading_progress = 0

    def update_progress(self):
        self.loading_progress += 1
        self.progress_bar.setValue(self.loading_progress)

        if self.loading_progress >= 100:
            self.timer.stop()
            self.close()


def runLoad():
    app = QApplication(sys.argv)

    loading_page = LoadingPage()

    loading_page.show()

    sys.exit(app.exec())
