from PySide6.QtWidgets import *
from PySide6.QtGui import *
from tabulate import tabulate
import json
from taskmanager import TaskManager

class TaskView(QWidget):
    def __init__(self, task, index, taskmanager):
        super().__init__()
        self.task = task
        self.index = index
        self.taskmanager = taskmanager
        self.setFixedSize(350,420)
        self.components()
        
        
    def components(self):
        # Fonts
        self.fonts = QComboBox(self)
        self.fonts.setGeometry(230, 60, 100, 30)
        self.fonts.addItem('Segoe UI')
        self.fonts.addItem('Times')
        self.fonts.addItem('Verdana')
        self.fonts.addItem('Monospace')
        self.fonts.addItem('Arial')
        self.fonts.addItem('Lucida Console')
        self.fonts.addItem('Courier')
        self.fonts.addItem('Georgia')
        
        # Font Sizes
        self.font_sizes = QComboBox(self)
        self.font_sizes.setGeometry(230, 90, 100, 30)
        self.font_sizes.addItem('12')
        self.font_sizes.addItem('14')
        self.font_sizes.addItem('16')
        self.font_sizes.addItem('18')
        self.font_sizes.addItem('22')
        self.font_sizes.addItem('28')
        self.font_sizes.addItem('32')
        self.font_sizes.addItem('44')
        
        # Font Style
        self.font_styles = QComboBox(self)
        self.font_styles.setGeometry(230, 120, 100, 30)
        self.font_styles.addItem('normal')
        self.font_styles.addItem('bold')
        self.font_styles.addItem('italic')
        
        
        self.texts = QTextEdit(self)
        self.texts.setGeometry(20, 200, 310, 200)
        self.texts.setText('hello world')
        self.texts.setFont(QFont('Segoe UI'))
        
        self.label = QLabel('Customize Font', self)
        self.label.setGeometry(230, 35, 100, 30)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.button = QPushButton("Set Font", self)
        self.button.setGeometry(230, 160, 100, 30)
        self.button.clicked.connect(self.setFont)
        
        self.img = QLabel(self)
        self.img.setGeometry(40, 60, 130, 130)
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img.setStyleSheet(""" 
                               background-color: gray;
                               """)
        self.img.setScaledContents(True)
        self.img.mousePressEvent
        
        self.label = QLineEdit(self.task.title, self)
        self.label.setGeometry(40, 28, 130, 30)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        pass
        
    def setFont(self):
        self.task.title = self.label.text()
        font = self.fonts.currentText()
        size = self.font_sizes.currentText()
        style = self.font_styles.currentText()
        self.texts.setStyleSheet(f"""
                                  font: {style} {size}px "{font}";
                                 """)
        self.modifyTask()
        pass
    
    def loadTask(self):
        self.texts.setText(self.task.description)
        font = self.task.font
        font_size = self.task.font_size
        font_style = self.task.font_style
        img = str(self.task.img)
        
        self.fonts.setCurrentText(font)        
        self.font_sizes.setCurrentText(font_size)        
        self.font_styles.setCurrentText(font_style)        
        self.img.setPixmap(QPixmap(img))
        self.texts.setStyleSheet(f"""
                                  font: {font_style} {font_size}px "{font}";
                                 """)
        
    def modifyTask(self):
        self.task.title = self.label.text()
        self.task.description = self.texts.toPlainText()
        self.task.font = self.fonts.currentText()
        self.task.font_size = self.font_sizes.currentText()
        self.task.font_style = self.font_styles.currentText()
        self.taskmanager.editTask(self.index, self.task)
        pass
    
    def mousePressEvent(self, event):
        file_dialog = QFileDialog(self)
        file_name = file_dialog.getOpenFileName(self, '', '', 'Images (*.png *.xpm *.jpg)')[0]
        if len(file_name.strip()) != 0: 
            self.task.img = file_name
            self.img.setPixmap(QPixmap(self.task.img))
        return super().mousePressEvent(event)
    
    def showEvent(self, event):
        self.loadTask()
        return super().showEvent(event)
    
    def closeEvent(self, event):
        self.modifyTask()
        return super().closeEvent(event)