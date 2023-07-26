class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height
    
    def show(self):
        return f"{self.__title}: {self.width}, {self.height}"
    
    @staticmethod
    def check_value(value):
        return type(value) is int and value in range(0, 10001)
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if self.check_value(width):
            self.__width = width
            self.show()
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if self.check_value(height):
            self.__height = height
            self.show()



