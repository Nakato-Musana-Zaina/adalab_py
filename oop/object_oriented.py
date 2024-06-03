class Student:
    school = "Akirachix"
    
    def __init__(self, first_name,last_name,age,country,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code= code

    def greet_student(self):
        greeting = f"Hello {self.first_name}, welcome to {self.school}. YOur code is {self.code}"
        return greeting
    
    def year_of_birth(self):
        return f"{self.first_name}, you were born in {2024-self.age}"
    
    def full_name(self):
        fullname = self.first_name + self.last_name
        return fullname
    
    def intials(self):
        intial=self.first_name[0] + self.last_name[0]
        return intial
    
    def check_minor(self):
        if self.age <= 18:
            return f"your are a minor"
        else:
            return f"your are an adult"
        
    
    def enrollment(self):
        

        


# agnes = Student(first_name ="agnes", last_name = "Wangesha", age =21, country="Kenya", code = 79)
# faith = Student(first_name ="Faith", last_name = "Mutava", age =21, country="Kenya", code = 27)
# glory = Student(first_name ="Glory", last_name = "Wachira", age =21, country="Kenya", code = 2),
        



    