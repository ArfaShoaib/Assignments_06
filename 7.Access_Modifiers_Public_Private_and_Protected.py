class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private

    # Getter method for private __ssn
    def get_ssn(self):
        return self.__ssn

    # Setter method for private __ssn
    def set_ssn(self, ssn):
        self.__ssn = ssn

# Create an Employee object
emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing public variable
print("Name:", emp.name)

# Accessing protected variable
print("Salary (Protected):", emp._salary)

# Accessing private variable using getter method
print("SSN (Private) using getter:", emp.get_ssn())

# Modifying private variable using setter method
emp.set_ssn("987-65-4321")
print("Updated SSN using setter:", emp.get_ssn())
