#parent class
class Mother:

    #Constructor
    def __init__(self,eye_color,height):
        self.eye_color = eye_color
        self.height = height

    def show_details(self):
        print("Eye color: ", self.eye_color)
        print("Height:", self.height)

# Child class
class Daughter(Mother):

    def __init__(self,name,age,eye_color, height):
        self.name = name
        self.age = age
        super().__init__(eye_color, height)

    def show_details(self):
        print ("Nme:",self.name)
        print("Age:",self.age)    
        super().show_details()

    def favourite_hobby(self,hobby):
        print(f"{self.name} loves {hobby}")


obj = Daughter("Zarifah", 13, "brown", "134cm")
obj.show_details()
obj.favourite_hobby("reading")