from PySide6.QtWidgets import *
from PySide6.QtGui import *
from taskmanager import TaskManager
from task import Task
from taskview import TaskView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.taskmanager = TaskManager()
        self.isItemSelected = False
        self.setFixedSize(500,500)
        self.components()
        self.initUI()
    
    def components(self):
        self.list = QListWidget(self)
        self.list.setGeometry(25,25, 450, 280)
        self.list.itemClicked.connect(self.selected)
        
        self.saveButton = QPushButton("SAVE INTO FILE", self)
        self.saveButton.setGeometry(50, 340, 140, 38)
        
        self.deleteButton = QPushButton("DELETE TASK", self)
        self.deleteButton.setGeometry(310, 340, 140, 38)

        self.addButton = QPushButton('ADD', self)
        self.addButton.setGeometry(365, 420, 110, 38)
        
        self.textfield = QLineEdit(self)
        self.textfield.setGeometry(25,420, 320, 38)
        pass
        
    def initUI(self):
        self.addButton.clicked.connect(self.addTask)
        self.deleteButton.clicked.connect(self.deleteTask)
        self.saveButton.clicked.connect(self.saveTasks)
        self.list.itemDoubleClicked.connect(self.viewTask)
        pass
    
    def addTask(self):
        title = self.textfield.text().strip()
        
        if title != "":
            task = Task(title, None, None, None, None, None)    
            self.taskmanager.addTask(task.__dict__)
            
            self.list.addItem(Item(task.title))
        pass
    
    def deleteTask(self):
        if self.list.selectionModel().hasSelection():
            selected_task = self.list.currentIndex().row()
            
            self.list.takeItem(selected_task)
            self.taskmanager.deleteTask(selected_task)
            self.list.selectionModel().clearSelection()
        pass
    
    def saveTasks(self):
        message = QMessageBox(self)
        message.setText("Save tasks into file?")
        message.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Save)
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle('Info')
        response = message.exec()
        
        if response == QMessageBox.Save:
            print('saving')
            self.taskmanager.saveTasksToFile()     
        
        pass
    
    def viewTask(self):
        task_selected = self.list.currentIndex().row()
        tasks = self.taskmanager.getTasks()
        
        if len(tasks) != 0:
            self.viewtask = TaskView(tasks[task_selected], task_selected, self.taskmanager)
            self.viewtask.setWindowModality(Qt.ApplicationModal)
            self.viewtask.show()
        pass
    
    def loadTasks(self):
        for task in self.taskmanager.getTasks():
            self.list.addItem(Item(task.title))
        
    def selected(self):
        if self.isItemSelected:
            self.list.selectionModel().clearSelection()
            self.isItemSelected = False
        else:
            self.isItemSelected = True
            
    def showEvent(self, event):
        self.loadTasks()
        return super().showEvent(event)
    
    def changeEvent(self, event):
        self.list.clear()
        self.loadTasks()
        return super().changeEvent(event)
    
    
class Item(QListWidgetItem):
    def __init__(self, label):
        super().__init__(f'-> {label}')
        self.setFont(QFont("Segoe UI", 18))
        self.setForeground(QColor('white'))
        self.setBackground(QColor('#525252'))