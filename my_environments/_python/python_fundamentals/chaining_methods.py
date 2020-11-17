
#creating a file with User Class including the __inti__ and make_deposit methods
class User:
    def __init__(self, user_name, user_email):
        self.name = user_name
        self.email = user_email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount

    #Create three instances of user class
user = User("Sonu", "sonuisgrea@gmail.com")
user_one = User("Kenya", "kenyakitty@gmail.com")
user_two = User("Rowley", "rowleycat@gmail.com")
user_two = User("Chester", "stunningboy@gmail.com")

user.make_deposit(123)
print(f"Before my balance was {user.account_balance}")
user.make_deposit(12345)
print(f"After, my balance was {user.account_balance}")

#make_deposit method
    def make_deposit(self, amount):	
        self.account_balance += amount

# make_withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount

#add a display_user_balance method to User class
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")



#Have the first user make 3 deposits, 1 withdrawal and display balance
user_one.make_deposit(123)
print(f"Before my balance was {user.account_balance}")
user_one.make_deposit(12345)
print(f"After, my balance was {user.account_balance}")
user_one.make_withdrawal(100)
print(f"your account has been reduced by {user.account_balance}")

kenya.make_deposit(100,000).make_deposit(100,000).make_deposit(100,000).make_withdrawal(50,000).display_user_balance()
print(f"User: {self.name}, Balance: ${self.account_balance}", "Now you are rich.  Go party like a rock star.  Actually don't.  They all end up in rehab.  Instead invest wisely, so that you can retire young and help disadvantaged kids go to college.")

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
rowley.make_deposit(100.00).make_deposit(100.00).make_withdrawl(100.00).make_withdrawal(50.00).display_user_balance()
print(f"User: {self.name}, Balance: ${self.account_balance}", "Good kitty")

# Have the third user make 1 deposits and 3 withdrawals and then display their balance   
Chester.make_deposit(10.00).make_deposit(5.00).make_withdrawl(1.00).make_withdrawal(1.00).display_user_balance()
print(f"User: {self.name}, Balance: ${self.account_balance}", "You're poor.  You should probably apply for some scholarships and grants, go back to school, and make something of yourself because this ballance is just sad.")



