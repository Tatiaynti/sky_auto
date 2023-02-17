class User:
    def __init__(self, _firstname, _lastname):
        self.first_name = _firstname
        self.last_name = _lastname
    
    def printFirstname(self):
        print(self.first_name)

    def printLastname(self):
        print(self.last_name)

    def printFirstnameAndLastname(self):
        print(self.first_name + ' ' + self.last_name)