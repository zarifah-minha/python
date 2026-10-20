class myClass:

    # private variable
    __privatevar = 27

    # Private method
    def __privatemeth(self):
        print(" I am a private method ")

    def show_output(self):
        print(myClass.__privatevar)


ob = myClass()
ob.show_output()
ob.__privatemeth()
