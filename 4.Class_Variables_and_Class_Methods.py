"""Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances."""



class Bank:
    bank_name = "Default Bank"  # Class variable
   

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change the class variable

    
    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")



# Create instances of the Bank class
bank1 = Bank("Alice")
bank2 = Bank("Bob")
bank3 = Bank("Charlie")


bank1.display_info()
bank2.display_info()
bank3.display_info()

# Change the bank name using the class method
Bank.change_bank_name("ABC Bank")

print("\nAfter changing the bank name:\n")

bank1.display_info()
bank2.display_info()
bank3.display_info()