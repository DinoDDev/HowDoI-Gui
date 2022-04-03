from tkinter import font
from howdoi import howdoi 
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QLineEdit, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QDialog, QScrollArea, QComboBox

class ErrorWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!")
        self.setMinimumSize(200,100)
        error_msg = QLabel("Insert a question")

        close_button = QPushButton("Close")
        close_button.setCheckable(True)
        close_button.clicked.connect(self.close_window)

        error_layout = QVBoxLayout()
        error_layout.setAlignment(Qt.AlignCenter)
        error_layout.addWidget(error_msg)
        error_layout.addWidget(close_button)

        self.setLayout(error_layout)
        
        self.exec_()

    def close_window(self):
        self.close()

# how to remove bg python
class ScrollLabel(QScrollArea):
 
    def __init__(self):
        super().__init__()

        # set QScrollArea resizable
        self.setWidgetResizable(True)
 
        layout = QVBoxLayout()
 
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
 
        # add label to the layout
        layout.addWidget(self.label)
        
        # create widget and set layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)
 
    def setText(self, text):
        self.label.setText(text)

class HowDoIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("How Do I")
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        # create the scrollable label
        self.scroll_label = ScrollLabel()

        #create the input field
        self.input_line  = QLineEdit()

        #create the button search and set an event for click
        self.search_button = QPushButton("Search")
        self.search_button.setCheckable(True)
        self.search_button.clicked.connect(self.click_on_search_button)

        self.engine_list = QComboBox()
        self.engine_list.addItems(["Google", "Bing", "DuckDuckGo"])

        #create a lable and Font for the title
        title_label = QLabel("How do I..?")
        title_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        
        title_font = title_label.font()
        title_font.setPointSize(15)
        title_label.setFont(title_font)

        # add widgets to Horizontal Layout
        horizontal_layout.addWidget(self.input_line)
        horizontal_layout.addWidget(self.search_button)
        horizontal_layout.addWidget(self.engine_list)

        # add widgets and Horizontal Layout to Vertical Layout
        vertical_layout.addWidget(title_label)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.scroll_label)

        # set layout alignment to top
        vertical_layout.setAlignment(Qt.AlignTop)
        horizontal_layout.setAlignment(Qt.AlignTop)

        # create widget and set layout
        widget_container = QWidget()
        widget_container.setMinimumSize(500,350)
        widget_container.setLayout(vertical_layout)
        self.setCentralWidget(widget_container)

    def click_on_search_button(self):
        # remove the spacing from start and end of string
        text_insered = self.input_line.text().lstrip()
       
        chosed_engine = self.engine_list.currentText()
        if chosed_engine == "Google":
            engine="-e google "
        elif chosed_engine == "Bing":
            engine="-e bing "
        else:
            engine="-e duckduckgo "
            
        search_command = engine + text_insered

        # if string is empty show a window error
        if len(text_insered) <= 0:
           ErrorWindow()
        else:
            self.scroll_label.setText(howdoi.howdoi(search_command))

    def keyPressEvent(self, event):
        # if press Enter on keyboard i start the search
        if event.key() == Qt.Key_Return:
            self.click_on_search_button() 


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = HowDoIWindow()
    window.show()

    app.exec_()
