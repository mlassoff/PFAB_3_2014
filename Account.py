class BankAccount(object):
	aCount =0;

	def __init__(self, initial_balance=0):
		self.balance = initial_balance
		BankAccount.aCount += 1

	@classmethod
	def introduce(BankAccount):
		return BankAccount.aCount

	#instance method
	def deposit(self, amount):
		self.balance += amount
	#instance method
	def withdraw(self, amount):
		self.balance -= amount


class BankAccount2(object):
	def __init__(self, initial_balance=0):
		self._balance = initial_balance

	@property
	def balance(self):
		return self._balance
	@balance.setter
	def balance(self, balance):
		self._balance = balance

	def deposit(self, amount):
		self._balance += amount

	def withdraw(self, amount):
		self._balance -= amount

account = BankAccount2()
print "Balance before transaction: " , account._balance
account.deposit(175)
print "Balance after transaction: " , account._balance


print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
myAccount = BankAccount(100)
myAccount.withdraw(30)
print myAccount.balance
yourAccount = BankAccount(100)
yourAccount.deposit(50)
print yourAccount.balance
print "Number of accounts created: " , BankAccount.introduce()


