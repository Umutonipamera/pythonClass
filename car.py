class Car:
    name="Toyota" 
    def  __init__(self,model,colour,accelelation,registration):
        self.model=model
        self.colour=colour
        self.accelelation=accelelation
        self.registration=registration
    def hoot(self):
        return f"Hello your car name is{self.name} it's model is{self.model},it's colour is{self.colour}, it's accelelation is{self.accelelation} and it's registration is{self.registration}"  