import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QTimer, QEvent
from PyQt5.QtGui import QPalette
from hs3_main import get_answer

print("Initializing GUI...")

class HAISGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.isRequestERROR = False
        self.initUI()
        self.input_text.installEventFilter(self)

    def initUI(self):
        print("Initializing Display...")
        self.setWindowTitle("HAIS - AI Chatbot")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(500, 400)

        # Set the main window background color
        self.setStyleSheet("background-color: rgb(227, 227, 227);")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Header
        print("Initializing Text...")
        header = QLabel("HAIS")
        header.setFont(QFont("Georgia", 20))
        header.setStyleSheet("background-color: rgb(63, 120, 134); color: rgb(252, 211, 192); padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Display Text
        self.display_text = QTextEdit()
        self.display_text.setFont(QFont("Georgia", 18))
        self.display_text.setStyleSheet("background-color: rgb(195, 206, 212); color: rgb(43, 46, 97); border: none;")
        self.display_text.setReadOnly(True)
        layout.addWidget(self.display_text)

        # Input Text
        self.input_text = QTextEdit()
        self.input_text.setFont(QFont("Georgia", 18))
        self.input_text.setStyleSheet("background-color: rgb(252, 211, 192); color: rgb(43, 46, 97); border: none;")
        self.input_text.setFixedHeight(100)
        layout.addWidget(self.input_text)

        # Buttons
        print("Initializing Buttons...")
        button_layout = QHBoxLayout()
        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(QFont("Georgia", 16))
        self.exit_button.setStyleSheet("background-color: rgb(250, 160, 129); color: rgb(251, 212, 141);")
        self.exit_button.clicked.connect(self.hs3_exit)
        button_layout.addWidget(self.exit_button)

        self.send_button = QPushButton("Send")
        self.send_button.setFont(QFont("Georgia", 16))
        self.send_button.setStyleSheet("background-color: rgb(99, 155, 169); color: rgb(251, 212, 141);")
        self.send_button.clicked.connect(self.hs3_sendText)
        button_layout.addWidget(self.send_button)
        layout.addLayout(button_layout)
        print("HAIS Staus: Online")
    
    def error_handler(self, response):
        if "HAIS-ERROR:" in response:
            self.isRequestERROR = True
            print("Error Occurred; Send Button is Disabled")
            self.send_button.setEnabled(False)
            self.display_text.append("\n*** ALERT ***\nAn error has occurred, please try to resolve mentioned errors.\nSession has been terminated.\nClick Exit\n********************************\n")
            self.display_text.setTextColor(QColor(209, 99, 127))  # Use a warm red color for error messages
    
    def hs3_exit(self):
        self.display_text.append("\nIt was fun talking to you! \nHave a nice day! \nGoodbye!")
        self.exit_button.setFont(QFont("Georgia", 16))
        self.display_text.setTextColor(QColor("Black"))
        self.send_button.setEnabled(False)
        self.exit_button.setEnabled(False)
        QTimer.singleShot(3000, self.close)

    def hs3_sendText(self):
        user_input = self.input_text.toPlainText().strip()
        if user_input:
            self.display_text.append(f"You: {user_input}")
            get_hs3_response = get_answer(user_input)
            self.display_text.append(f"HAIS: {get_hs3_response}")
            self.display_text.setTextColor(QColor("darkblue"))
            self.display_text.moveCursor(self.display_text.textCursor().End)
            self.input_text.clear()
            self.error_handler(get_hs3_response)

        else:
            print("Input cannot be empty!")
            self.display_text.append(f"Hais: Input is empty!")
            return False
    #Event handler
    def eventFilter(self, source, event):
        if (source == self.input_text and 
            event.type() == QEvent.KeyPress and 
            event.key() == Qt.Key_Return and 
            not event.modifiers() & Qt.ShiftModifier):
            self.hs3_sendText()
            return True
        return super().eventFilter(source, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HAISGui()
    ex.show()
    sys.exit(app.exec_())

print("HAIS GUI closed.")


        


