import sys

from PyQt5.QtWidgets import (QApplication, QLineEdit, QPushButton, QTextEdit,
                             QVBoxLayout, QWidget)


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()  # Create the layout

        self.chatHistory = QTextEdit()
        self.chatHistory.setReadOnly(True)

        self.messageInput = QLineEdit()
        self.sendButton = QPushButton("Send")
        self.sendButton.clicked.connect(self.sendMessage)

        # Add widgets to the layout instead of setting it directly as an attribute
        layout.addWidget(self.chatHistory)
        layout.addWidget(self.messageInput)
        layout.addWidget(self.sendButton)

        self.setLayout(layout)  # Use setLayout to apply the layout to the widget
        self.setWindowTitle("Chat with Phi-2")

    def sendMessage(self):
        userMessage = self.messageInput.text()
        # Here, integrate with your model to process userMessage and generate a response
        botResponse = "This is where the bot's response would go."

        self.chatHistory.append(f"User: {userMessage}")
        self.chatHistory.append(f"Bot: {botResponse}")

        self.messageInput.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
