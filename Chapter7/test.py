import types
import inspect

class Bank_account(object):
    '''Simulate the bank accounts in the real world.'''
    name = 'Mike'
    def __init__(self, balance):
        #self.balance = balance
        self.name = 'Micheal'

    def change(self):
        self.__init__(500)

    def with_draw(self, amount):
        #self.balance -= amount
        pass

    def deposit(self, amount):
        #self.balance += amount
        pass

    def get_balance(self):
        #return self.balance
        pass

    def get_name(self):
        return Bank_account.name

    def add_job(self):
        #self.job = 'engineer'
        #self.name = 'Lily'
        pass

    def change_name(self, string):
        self.name = string
        Bank_account.name = 'Globala'
        print self.name

    def first(self):
        self.a = 'a'

    def second(self):
        return self.a
        
class Check_account(Bank_account):
    '''Simulate the checking account.'''
    #def get_name(self, string):
        #print 'abc'
    pass

account = Bank_account(0)
print account.__dict__
print account
account.add_job()
print account.get_name()
print account
account.change()
print account.get_balance()
print account
checking = Check_account(0)
#checking.get_name('a')
print type(account)
print type(Bank_account)
print isinstance(account, Bank_account)
print issubclass(Check_account, Bank_account)
print types.IntType
print inspect.getmembers(Bank_account)
help(Bank_account)
print account.get_name()
print checking.get_name()
account.change_name('Lin')
print account.name
print checking.name
print account.get_name()
print checking.get_name()
account.first()
account.second()
