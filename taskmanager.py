import json
from task import Task
from tabulate import tabulate
import socket

class TaskManager:
    def __init__(self):
        self.ip = self.check_ip_address()
        pass
    
    def addTask(self, task):
        with open('tasks.json') as json_file:
            data = json.load(json_file)
            
            if self.ip not in data:
                data.update({self.ip : [task]})
            else:
                data[self.ip].append(task) 
            
        with open('tasks.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
    def editTask(self, task_index, task):
        with open('tasks.json', 'r') as json_file:
            data = json.load(json_file) 
        
        if task_index < len(data[self.ip]) and task_index >= 0:
            data[self.ip][task_index] = task.__dict__
            
            with open('tasks.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
        pass
            
    def deleteTask(self, task_index):
        with open('tasks.json', 'r') as json_file:
            data = json.load(json_file) 
        
        if task_index < len(data[self.ip]) and task_index >= 0:
            del data[self.ip][task_index]
            print('task deleted')
            
            with open('tasks.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
    
    def getTasks(self):
        with open('tasks.json', 'r') as json_file:
            data = json.load(json_file)    
            
            tasks = []
            
            if self.ip in data:
                for task_item in data[self.ip]:
                    task_obj = Task(**task_item)     
                    # tasks.append({'title' : task_obj.title, 'description' : task_obj.description})   
                    tasks.append(task_obj)     
                
            else:
                print('No tasks added \n')    
                
            return tasks
    
    def saveTasksToFile(self):
        with open('tasks.json', 'r') as json_file:
            data = json.load(json_file)  
            
        tasks = []
            
        if self.ip in data:
            for task_item in data[self.ip]:
                task_obj = Task(**task_item)     
                tasks.append({'title' : task_obj.title, 'description' : task_obj.description})        
                
            table = tabulate(tasks, headers='keys', tablefmt="grid", showindex=True)

            with open(f'{self.ip}-tasks.txt', 'w') as txt:
                    txt.write(f'IP: {self.ip} \n')
                    txt.write(table)
            print('saved into file')
        else:
            print('nothing to save')
            
    def check_ip_address(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        if ip_address:
            print(f'Connected: {ip_address}')
            return ip_address
        else:
            print('Not Connected:')
            pass
            