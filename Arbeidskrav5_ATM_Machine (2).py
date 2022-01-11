from Arbeidskrav5_AcountClass import Acount

class ATMMachine():
    def __init__(self, bankList = []):
        self.bankList = bankList
        self.acountid = 0

    def checkID(self):
        print("Enter an acount ID: ", end = '')
        id = int(input())
        for i in range(0, len(self.bankList)):
           # if id == int(Acount.getId(self.bankList[i])):
            if id == self.bankList[i].getId():
                self.acountid = i
            
        if self.acountid >= 1:
            self.getAChoice()
        else: 
            print(f'No match')
        
    def runAtm(self, choice):    
        if choice == 1: 
            print(f'The balance is {Acount.getBalance(self.bankList[self.acountid])}') #Endre lik linje 12
            self.getAChoice()
        elif choice == 2:
            number = float(input('Enter an amount to withdraw: '))
            self.bankList[self.acountid].setWithdraw(number) #fjerne "set"
            self.getAChoice()
        elif choice == 3: 
            number = float(input("Enter an amount to deposit: "))
            self.bankList[self.acountid].setDeposit(number) #fjerne "set"
            self.getAChoice()
        else: 
            self.checkID()

    def getAChoice(self):
        while True:
            print("\nMain menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            print("Enter a choice: ", end = '')
            choice = int(input())
            if choice < 1 or choice > 4:
                print("Wrong choice, try again: ", end = "")
            else:
                self.runAtm(choice)

def main():
    if __name__ == "__main__":
        banklist2 = []
        for i in range(0, 10):
            banklist2.append(Acount(i))
    
        atm = ATMMachine(banklist2)
        atm.checkID()

main()


