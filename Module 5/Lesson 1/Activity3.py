class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age 

blu= parrot("blu",10)
woo = parrot("woo",15)

print(f"The name of the first parrot is {blu.name}. he is {blu.age} years old. he is a {blu.species}")

print(f"The name of the first parrot is {woo.name}. he is {woo.age} years old. he is a {woo.species}")