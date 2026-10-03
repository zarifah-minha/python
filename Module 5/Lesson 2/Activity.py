class IOString:
    def __init__(self):
     self.str1 = ""

    def get_input(self):
        self.str1 = input("Enter the string: ")

    def print_string(self):
       print("Result: ",self.str1.upper())

obj = IOString()
obj.get_input()
obj.print_string()