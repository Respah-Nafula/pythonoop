class Student:
     school = "Akirachix"
     def __init__(self,country,first_name,last_name,age):
        self.first_name = first_name
        self.country = country
        self.last_name = last_name
        self.age = age
     def full_name (self):

         return f"Hello {self.first_name} {self.last_name} How is {self.country}"
     def year_of_birth (self):  
         year=2022 - self.age
         return f"Hello {self.first_name} {self.last_name} How is {self.country} you are born in year {year}"
     def initials (self):
         return f"Hello {self.first_name} {self.last_name} How is {self.country} your initials are {self.first_name[0]} {self.last_name[0]}"

