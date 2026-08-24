class Account:
    def __init__(self, account_name: str, balance: int):
        self.account_name = account_name
        self.balance = balance
        pass
    
    def display_balance(self) -> None:
        print(f"Balance: ${self.balance}")
        pass


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
