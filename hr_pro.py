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
    # def get_bonus(self):
    # #   return self.bonus_percentage * self.salary 
    def __str__(self):
        return f"Employee name is{self.name}, age is : {self.age}, and their salary is {self.salary} , the employment year : {self.employment_year} , {self.bonus_percentage}"

employees =[ Employee ("manal" , 24 , 3000 , 2011),
 Employee("maryam" , 33 , 2300, 2022)  ,
 Employee("haya" ,33 , 430 , 2023) ,
 Employee("malak" , 45 , 3300 , 2010),]
# print(employe1),
# print(employe2)
# print(employe3)
# print(employe4)
manager1 = Manager("sara" , 45 , 2300 , 2012 , 0.5)
manager2 = Manager("maram" , 44 , 430 , 2010 , 0.5)
manager3 = Manager("sara" , 45 , 500 , 2018 , 0.5)
manager4 = Manager("sara" , 45 , 670 , 2019 , 0.5)

print(manager1)
print(manager2)
print(manager3)
print(manager4)
# def main():
	# main code here
   







    # for chose in choses :
    #     if 

    # em = Employee("ali", 999, 1000, 2020)
    # print(em)

# if __name__ == '__main__':
# 	main()
# x = [1,2]

# c = Employee("a", 222, 9000, 2020)


