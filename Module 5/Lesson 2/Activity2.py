class Employee:
    def __init__ (self):
        print("EMPLOYEE CREATED")

    def __del__ (self):
        print("Destructor Called")

def create_obj(): 
    print("Maiking object......")
    obj = Employee()
    return obj 
obj = create_obj()
