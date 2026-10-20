class Bangladesh:
    def capital(self):
        print("Dhaka is the capital city of Bangladesh.")
    def language(self):
        print("Bangla is the native language of Bangladesh.")
    def type(self):
        print("Bangladesh is a developing country.")


class USA:
    def capital(self):
        print("Wahington D.C is the capital city of  USA.")
    def language(self):
        print("English is the native language of USA.")
    def type(self):
        print("USA is a developed country.")


class India:
    def capital(self):
        print("New Delhi is the capital city of India.")
    def language(self):
        print("Hindi is the native language of India.")
    def type(self):
        print("India is a developing country.")

obj_bd = Bangladesh()
obj_ind = India()
obj_usa = USA()

for country in (obj_bd, obj_ind, obj_usa):
    country.capital()
    country.type()
    country.language()