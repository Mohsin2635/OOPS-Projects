class Bank:
    Bank_name = "MCB Bank"
    
    def __init__(self,customer_name):
        self.customer = customer_name
    @classmethod
    def change_bank_name(cls,new_name):
        cls.Bank_name = new_name
Bank.change_bank_name("Meezan ")
customer1 = Bank("Hammad")
customer2 = Bank("Mohsin")
print(f"Our first customer is {customer1.customer}")
print(f"Our second customer is {customer2.customer}")
print(f"They all get these bank: {Bank.Bank_name}")
