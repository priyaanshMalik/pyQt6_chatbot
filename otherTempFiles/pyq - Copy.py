import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFrame,
    QLabel,
    QSpacerItem,
)
from PyQt6.QtCore import Qt


WINDOW_LENGTH = 1200
WINDOW_WIDTH = 900
DISPLAY_HEIGHT = int(900 * 0.8)
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 40


class main_window(QMainWindow):
    """main window GUI"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bhagvad Gita Chatbot")
        self.setGeometry(100, 100, WINDOW_LENGTH, WINDOW_WIDTH)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createInputArea()
        # A single leading underscore in front of a variable,
        # a function, or a method name means that these objects
        # are used internally.

    def _createDisplay(self):
        self.display = QFrame()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setLineWidth(2)
        self.display.setStyleSheet(
            "background-color: #808080;\
                                   border: 5px solid #000000;"
        )
        self.generalLayout.addWidget(self.display)
        self.msgLayout = QVBoxLayout()
        self.display.setLayout(self.msgLayout)

    def _createInputArea(self):
        inputLayout = QGridLayout()
        self.btn = QPushButton("SEND")
        self.btn.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.inputBox = QLineEdit()
        inputLayout.addWidget(self.inputBox, 0, 0, 0, 5)
        inputLayout.addWidget(self.btn, 0, 6)

        self.generalLayout.addLayout(inputLayout)

    def setInputText(self, text):
        """Set the display's text."""
        self.inputBox.setText(text)
        self.inputBox.setFocus()

    def getInputText(self):
        """Get the display's text."""
        return self.inputBox.text()

    def clearInput(self):
        """Clear the display."""
        self.setInputText("")

    def addMsg(self, msg):
        message = MessageBubble(msg)
        self.msgLayout.addWidget(message)


class MessageBubble(QWidget):
    def __init__(self, message, is_sent_by_user=False):
        super().__init__()
        self.initUI(message, is_sent_by_user)

    def initUI(self, message, is_sent_by_user):
        layout = QGridLayout()
        # layout.addStretch()
        self.setLayout(layout)

        message_label = QLabel(message)
        message_label.setWordWrap(True)
        # message_label.setFixedHeight(30)
        layout.addWidget(message_label, 1, 1, 1, 6)
        frame_style = "background-color: #DCF8C6; border-radius: 10px; padding: 8px;"
        if is_sent_by_user:
            frame_style += "background-color: #1DA1F2;"

        frame = QFrame()
        frame.setStyleSheet(frame_style)
        # frame.setFixedHeight(30)
        layout.addWidget(frame, 2, 3, 2, 8)
        # space = QSpacerItem(50, 50)
        # space.setFixedHeight(50)
        # layout.addWidget(space, 4,0, 7,0)

        # Code to add reply here


def main():
    """Main function for chatbot"""
    app = QApplication(sys.argv)
    window = main_window()
    window.addMsg("Hi there. How can i help you?")
    window.addMsg("What is this?")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
