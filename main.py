from task import Task
from taskmanager import TaskManager
import socket
from tabulate import tabulate
import sys
from PySide6.QtWidgets import *
from mainwindow import MainWindow

taskmanager = TaskManager()

def runGUI():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

def main() -> None:
    # main_menu()
    runGUI()
              
def check_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    if ip_address:
        print(f'Connected: {ip_address}')
        return ip_address
    else:
        print('Not Connected:')
        pass

def main_menu() -> None:
    while True:
        ip_address = check_ip_address()

        print('To Do List:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Delete Task')
        print('4. Save tasks to file')
        print('5. Exit')
        
        response = int(input('Select a number: '))
        
        if response == 1:
            title = input('Title: ')
            description = input('Description: ')
            font = 'Plain'
            font_style = fontStyles()
            font_size = int(input('Font size: '))
            
            task = Task(title, description, font, font_style, font_size, None)    
            
            taskmanager.addTask(task.__dict__, ip_address)        
            
            continue
        elif response == 2:
            tasks = taskmanager.showTasks(ip_address)
            
            print(f'Number of Tasks: {len(tasks)}')  
            print(tabulate(tasks, headers='keys', tablefmt="grid", showindex=True))
            
            continue
        elif response == 3:
            tasks = taskmanager.showTasks(ip_address)
            
            print(f'Number of Tasks: {len(tasks)}')  
            print(tabulate(tasks, headers='keys', tablefmt="grid", showindex=True))
            
            if len(tasks) > 0: 
                task_index = int(input(('Specify the task number: ')))
                
                taskmanager.deleteTask(ip_address, task_index)
            else:
                print('Nothing to delete')            
            
            continue
        elif response == 4:
            taskmanager.saveTasksToFile(ip_address)
            continue
        elif response == 5:
            quit()
            print('exitting...')
        else:
            print('Invalid response!')
            break

def fontStyles():
    print("Choose a font")
    table = {"Fonts" : ['Plain', 'Bold', 'Italic']}
    print(tabulate(table, headers='keys', tablefmt='grid'))
    font = input('Font: ')
    
    return font
    
if __name__ == '__main__':
    main()