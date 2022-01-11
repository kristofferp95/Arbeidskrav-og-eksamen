class Acount:
    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self): 
        return self.__id

    def setId(self, id):
        self.__id = id
    
    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
       self.__balance = balance  

    def getAnnualint(self):
        return self.__annualInterestRate

    def Annualint(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self): 
        return self.__annualInterestRate / 12 

    def getMonthlyInterest(self): 
        k = self.__balance * self.getMonthlyInterestRate() / 100
        return k

    def Withdraw(self, withdraw): 
        self.__balance = self.__balance - withdraw

    def Deposit(self, deposit): 
        self.__balance = self.__balance + deposit


