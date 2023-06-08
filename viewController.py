from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (
    QTimer,
    QThread,
    pyqtSignal,
)
from static import styles as st
from multiprocess import Process
import time


class ComputationThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, question):
        self.var = question
        super().__init__()

    def run(self):
        global bot_Obj
        result = bot_Obj.ask(self.var)

        # Emit signal with computed result
        self.finished.emit(result)


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Window.resize(934, 739)
        Window.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

        # central widget of window
        self.centralwidget = QtWidgets.QWidget(parent=Window)
        self.centralwidget.setStyleSheet("background-color:rgb(173, 216, 230);")
        self.centralwidget.setObjectName("centralwidget")

        # adding vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # scroll area
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet(st.scrollAreaStyle)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -575, 900, 1218))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # scroll Area Frame
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        # scroll area frame layout
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(parent=self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)

        # computer response/reply bubble
        self.reply_1 = QtWidgets.QLabel(parent=self.frame)
        self.reply_1.setMinimumSize(QtCore.QSize(600, 100))
        self.reply_1.setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reply_1.setFont(font)
        self.reply_1.setStyleSheet(st.replyStyle)
        self.reply_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.reply_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.reply_1.setLineWidth(3)
        self.reply_1.setMidLineWidth(3)
        self.reply_1.setObjectName("reply_1")
        self.gridLayout.addWidget(self.reply_1, 4, 0, 1, 1)

        # user querry bubble
        self.query_1 = QtWidgets.QLabel(parent=self.frame)
        self.query_1.setMinimumSize(QtCore.QSize(600, 100))
        self.query_1.setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.query_1.setFont(font)
        self.query_1.setStyleSheet(st.queryStyle)
        self.query_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.query_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.query_1.setLineWidth(3)
        self.query_1.setMidLineWidth(3)
        self.query_1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.query_1.setWordWrap(False)
        self.query_1.setObjectName("query_1")
        self.gridLayout.addWidget(self.query_1, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # bottom horizontal area
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setStyleSheet(st.hWidStyle)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)

        # label pointing to text field
        self.label = QtWidgets.QLabel(parent=self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:blue;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(parent=self.horizontalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        # text field/lineEdit at bottom which takes user query
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(st.lineEditStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.line_2 = QtWidgets.QFrame(parent=self.horizontalWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)

        # query send button
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.pushButton.setStyleSheet(st.btnStyle)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self._send_query)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.horizontalWidget)
        Window.setCentralWidget(self.centralwidget)
        self.actionRestart = QtGui.QAction(parent=Window)
        self.actionRestart.setObjectName("actionRestart")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        # list for queries
        self.query = [self.query_1]
        self.queryNumber = 0
        self.reply = [self.reply_1]
        self.replyNumber = 0
        self.gridCount = 4

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Bhagvad Gita ChatBot"))
        Window.setWindowIcon(QtGui.QIcon("./static/icon.jpg"))
        self.reply_1.setText(_translate("Window", "Hi!!! How can I help you?"))
        self.query_1.setText(_translate("Window", "Hi!!!"))
        self.label.setText(_translate("Window", "Ask Here"))
        self.lineEdit.setToolTip(
            _translate(
                "Window",
                '<html><head/><body><p><span style=" font-size:11pt; font-weight:700;">Enter Your Query...</span></p></body></html>',
            )
        )
        self.pushButton.setToolTip(
            _translate(
                "Window",
                '<html><head/><body><p align="center"><span style=" font-size:11pt; font-weight:700;">Ask the ChatBot</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Window", "SEND"))
        self.actionRestart.setText(_translate("Window", "Restart"))
        QTimer.singleShot(100, self._handle_scrlbar)

    # functions for managing functionality: ----->

    def _handle_scrlbar(self):
        x = self.scrollArea.verticalScrollBar().maximum()
        self.scrollArea.verticalScrollBar().setValue(x)

    def _send_query(self):
        queryStr = self.lineEdit.text().strip()
        if queryStr == "":
            return
        print(queryStr)
        self.queryFunc(queryStr)
        self._handle_scrlbar()
        self.pushButton.setEnabled(False)
        # threading:
        self.thread = ComputationThread(queryStr)
        self.thread.finished.connect(self.replyFunc)
        self.thread.start()
        self.thread.finished.connect(self.thread.deleteLater)

    def queryFunc(self, queryTxt):
        self.query.append(QtWidgets.QLabel(text=queryTxt, parent=self.frame))
        self.queryNumber += 1
        self.gridCount += 1

        self.query[self.queryNumber].setMinimumSize(QtCore.QSize(600, 100))
        self.query[self.queryNumber].setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.query[self.queryNumber].setFont(font)
        self.query[self.queryNumber].setStyleSheet(st.queryStyle)
        self.query[self.queryNumber].setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.query[self.queryNumber].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.query[self.queryNumber].setLineWidth(3)
        self.query[self.queryNumber].setMidLineWidth(3)
        self.query[self.queryNumber].setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.query[self.queryNumber].setWordWrap(False)
        self.query[self.queryNumber].setObjectName("query_" + str(self.queryNumber + 1))

    def replyFunc(self, answer, ans="Loading"):
        self.pushButton.setEnabled(True)
        self.reply.append(QtWidgets.QLabel(text=answer, parent=self.frame))
        self.replyNumber += 1
        self.gridCount += 1
        self.reply[self.replyNumber].setMinimumSize(QtCore.QSize(600, 100))
        self.reply[self.replyNumber].setMaximumSize(QtCore.QSize(1200, 1200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reply[self.replyNumber].setFont(font)
        self.reply[self.replyNumber].setStyleSheet(st.replyStyle)
        self.reply[self.replyNumber].setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.reply[self.replyNumber].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.reply[self.replyNumber].setLineWidth(3)
        self.reply[self.replyNumber].setMidLineWidth(3)
        self.reply[self.replyNumber].setObjectName("reply_" + str(self.queryNumber + 1))
        self.gridLayout.addWidget(self.reply[self.replyNumber], self.gridCount, 0, 1, 1)

    def rearrange(self):
        pass


def GUI(bot):
    import sys

    global bot_Obj
    global query_sol
    query_sol = ""
    bot_Obj = bot
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
