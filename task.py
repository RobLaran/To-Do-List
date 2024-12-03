class Task:
    def __init__(self, title, description, font, font_style, font_size, img):
        self.title = title
        self.description = description
        self.font = font
        self.font_style = font_style
        self.font_size = font_size
        self.img = img
        
    def __str__(self) -> str:
        return self.title

    def defaultStyles(self):
        self.font = 'Segoe UI'
        self.font_style = 'normal'
        self.font_size = '12'
    
    def print_task(self) -> None:
        print(f'Title: {self.title}')
        print(f'Description: {self.description}')
        
    def info(self):
        return [{'title' : self.title, 'description' : self.description, 'font': self.font, 'font_style' : self.font_style, 'font_size' : self.font_size}]