#Program #4: Employee Class
#Clara Riley
#Luke Snell
#11/08/24

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print("-" * 30)


# Creating Employee objects
employee1 = Employee("Bob Cratchit", 35785, "Accounting", "Vice President")
employee2 = Employee("Cave Johnson", 45786, "IT", "Programmer")
employee3 = Employee("Montgomery Scott", 26543, "Manufacturing", "Engineer")

# Displaying Employee information
employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()
