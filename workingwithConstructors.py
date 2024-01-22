class Student:
    
    def __init__(self, name, age, unit) -> None:
        self.name = name
        self.age = age
        self.unit = unit
        
        #return object properties as a string
    def __str__(self) -> str:
        return f"Name is : {self.name}, Age is {self.age}, UNit is : {self.unit}"
    
#Objects
stud = Student(name="jeff", age=15, unit=10)
print(stud)