# initialize a class
class employee:
    # special function or method/ magic method/ dunder method - constructor
    def __init__(self):
        print(id(self))
        #print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        #print("Data/attributes have been initiated")
    
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# creating an object or an instance of the class
sam = employee()
#sam.travel("Kolkata")
#print(id(sam))
sam.name = "Samar Kumar"
print(sam.name)

# encapsulation
