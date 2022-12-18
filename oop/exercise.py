"""
Q1.
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.
"""


class Bankaccount:
    def __init__(self, account_number, name, balance):
        self.acountNumber = account_number
        self.name = name
        self.__balance = balance

    def deposite(self, dep_amount):
        self.balance = dep_amount + self.balance

    def withdrawl(self, wid_amount):
        self.balance = self.balance - wid_amount

    def bankfees(self):
        self.balance = self.balance - (self.balance * 5) / 100

    def display(self):
        return f"Name is {self.name} \n Account Number: {self.acountNumber} \n Balance: {self.balance}"


bc = Bankaccount(123, "Jeeban", 20000)
print(bc.name)

"""
Q2.
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.
"""
