class bankaccount:
    def __init__(self, name,balance,pin):
        self.name = name
        self._balance = balance
        self.__pin = pin
    def showbalance(self):
        print(f"account holder:{self.name}")
        print(f"balance is:{self._balance}")    #protected
        print(f"pin:{self.__pin}")              #private
acc = bankaccount("asha",1000, 1234)
print(acc.name)
print(acc._balance)
print(acc.__pin)