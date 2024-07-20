"""
Author:  Brian Wiatrek
Date written: 07/13/24
Assignment:   Module 7 Programming Assignment Part 1
Short Desc:   This python program will demonstrate the usage of a sub class.  The parent class
              is the Person class with three variables and two methods.  The subclass has two
              additional variables and also two methods.
"""
class Person(object):
    """
    The person class has three variables:
    name: name of person
    address: address of person
    telephoneNbr: telephone number of person
    """
    def __init__(self, name, address, telephoneNbr):
        self.name = name
        self.address = address
        self.telephoneNbr = telephoneNbr

    def __str__(self):
        return "Name: " + self.name + "\nAddress: " + self.address + "\nTelephone Number: " + self.telephoneNbr


class Customer(Person):
    """
    The Customer class is a subclass of person and has two variables:
    customerNbr: unique identification of the customer
    mailingListFlag: a boolean representing whether the customer is on the mailing list
    """
    def __init__(self, name, address, telephoneNbr, customerNbr, mailingListFlag):
        Person.__init__(self, name, address, telephoneNbr)
        self.customerNbr = customerNbr
        self.mailingListFlag = mailingListFlag

    def __str__(self):
        return Person.__str__(self) + "\nCustomer Number: " + self.customerNbr + "\nMailing List: " + str(self.mailingListFlag)


def main():
    myCustomer = Customer("Brian Wiatrek", "109 Spring Fawn", "210-555-8765", "112233", False)
    print(myCustomer)

if __name__ == "__main__":
    main()

