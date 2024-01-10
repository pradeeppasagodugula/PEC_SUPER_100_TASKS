class Bank_Account:
    def __init__(self,holder_name,account_number,balance):
        self.holder_name=holder_name
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f'{amount} has been credited in your account.')
    def withdraw(self,amount):
        if(amount>self.balance):
            print("!!!!Insufficient funds. please creadit money!!!!")
        else:
            self.balance-=amount
            print(f"{amount} has been debited from your account.")
    def get_balance(self):
        print(f"Current balance is {self.balance}")

    def get_customer_details(self):
        print(f"Account holder Name : {self.holder_name}")
        print(f"Account Number : {self.account_number}")        

customer_1 = Bank_Account("Pradeep",45456790,5000)
customer_2=Bank_Account("Swamy",12345678,3000)
customer_3=Bank_Account("Varma",24689135,2506)

print('-----Account Holder Details-----')
customer_1.get_customer_details()
customer_2.get_customer_details()
customer_3.get_customer_details()

print("---Deposit and Withdrawl---")
customer_2.deposit(15000)
customer_2.withdraw(5000)
customer_2.get_balance()
customer_3.withdraw(4000)
customer_3.deposit(3500)
customer_3.get_balance()
