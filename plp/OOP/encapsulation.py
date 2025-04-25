#private is shown using self.__name   double underscores
#public has no underscores self.name
#protected is shown with a single underscore self._name

class Company:
    def __init__(self, name, products, ship_to):
        self.__name = name    #private
        self._products = products   #protected
        self.ship_to = ship_to     #public

    def get_name(self):    #use a method to access a private member
        return self.__name
    
class branch1(Company):
    def __init__(self,name, products, ship_to ,location):
        super().__init__(name, products, ship_to)
        self.location = location
    def showDetails():
        return f'Company name: {self.get_name()}'  
company = Company("Kingen",["laptops","smartphones","batteries"],"Global")

#print(company.get_name())
print(company._products)