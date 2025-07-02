
class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input(""" 
Hello, How would you like to proceed?
1. Enter 1 to create PIN
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check Balance
5. Enter 5 to exit
Your choice: """)

            if user_input == "1":
                print("Create Pin")
                self.create_pin()
            elif user_input == "2":
                print("Deposit")
                self.deposit()
            elif user_input == "3":
                print("Withdraw")
                self.withdraw()
            elif user_input == "4":
                print("Check Balance")
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.pin = input("Set your pin: ")
        print("Pin set successfully.")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance =self.balance - amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid Pin")


# Start the program
sbi = Atm()

