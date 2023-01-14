class Employee:
   #Employee class here
    def __init__(self, name , age ,salary , employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_annual_salary(self):
         return self.salary * 12


    def __str__(self) :
        # this func will take the argument from the user and save them to the class
        return f"{self.name} + {self.age} +{self.salary}+{self.employment_year} " 


class Manager(Employee):
    #Manager class here

    def __init__(self, name , age ,salary , employment_year,bonus_percentage):
        super().__init__(name,age,salary , employment_year )
        self.bonus_percentage = bonus_percentage


    def get_bonus(self): #becouse its a func inside the class so it will take self only 
        return self.bonus_percentage * self.salary 


    def __str__(self): #it will return and help us print the info iside the class 
        return f"Employee name is{self.name}, age is : {self.age}, and their salary is {self.salary} , the employment year : {self.employment_year} , {self.bonus_percentage}"





def main():
	# main code here

    employees =[ Employee ("manal" , 24 , 3000 , 2011),
    Employee("maryam" , 33 , 2300, 2022)  ,
    Employee("haya" ,33 , 430 , 2023) ,
    Employee("malak" , 45 , 3300 , 2010)
        ]
      
    managers =[
    Manager("sara" , 45 , 2300 , 2012 , 0.5),
    Manager("maram" , 44 , 430 , 2010 , 0.5),
    Manager("sara" , 45 , 500 , 2018 , 0.5),
    Manager("sara" , 45 , 670 , 2019 , 0.5)
    ]
   
    print ("welcom to HR pro")
    print("Options:")
    print("1: show Employees")
    print("2: show manager ")
    print("3: Add an Employee")
    print("4: Add A Manager")
    print("Exit")
    option = int(input("What would you like to do ? "))
    while option != 5:

        if option == 1:
            print (employees)
        elif option == 2:
            print(managers)
        elif option == 3:
            name = input("Enter name:")
            age = int(input("Enter Age: "))
            salary = int(input ("Enter Salary:"))
            employment_year = int(input("Enter employment year:"))
            employees.append(Employee(name, age, salary, employment_year))
        elif option == 4:
            name = input(" name:")
            age = int(input(" Age: "))
            salary = int(input (" Salary:"))
            employment_year = int(input("employment year:"))
            bonus_percentage = int(input("bonus percentage : "))
            managers.append(Manager(name, age,salary , employment_year,bonus_percentage))
        # else: 
        #     exit
    # for employe in employees:
    # if employe == 







    # for chose in choses :
    #     if 

    # em = Employee("ali", 999, 1000, 2020)
    # print(em)

if __name__ == '__main__':
	main()
# x = [1,2]

# c = Employee("a", 222, 9000, 2020)


