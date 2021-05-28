class Dog:
    name="Simba"
    def __init__( self,age,colour,name):
        self.age=age
        self.colour=colour
        self.name=name
    def biting(self):
        return f"Hello your dog age is{self.age} years old,colour is{self.colour},and it's name is{self.name}"
    