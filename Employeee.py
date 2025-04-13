class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return (f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions =  ["Manager", "Cashier", "Cook","Janitor"]
        return position in valid_positions
    
employee1= Employee("Göktuğ", "Manager")
employee2= Employee("Tuğberk", "Cashier")
employee3= Employee("Alpierenyo", "Cook")
    
print(Employee.is_valid_position("Osman"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())