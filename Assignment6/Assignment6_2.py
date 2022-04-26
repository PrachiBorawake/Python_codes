#Write a program which contains one class named as BankAccount.BankAccount class contains two instance variables as Name & Amount.
#That class contains one class variable as ROI which is initialise to 10.5.Inside init method initialise all name and amount variables by accepting the values from user.
#There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
#CalculateIntrest().Deposit() method will accept the amount from user and add that value in class instance variable
#Amount.Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
#CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
#And Display() method will display value of all the instance variables as Name and Amount.
#After designing the above class call all instance methods by creating multiple objects.
class BankAccount:

    def __init__(self,Name,Amount):
        print("Inside constructor") 
        self.Name=Name
        self.Amount=Amount
        self.ROI=10.5
        print("Enter the Name:")
        self.Name=input()
        print("Enter the amount:")
        self.Amount=int(input())
        
        
    def Deposit(self):
        print("Enter the Amount to be deposited:")
        self.deposite=int(input())
        self.Amount=self.Amount+self.deposite
            
    def Withdraw(self):
        print("Enter the amount to be withdraw:")
        self.withdrawn=int(input())
        self.withdrawn=self.Amount-self.withdrawn
    
    def CalculateIntrest(self):
        self.Interest=self.Amount*self.ROI
    
    def Display(self):
        print("Name:",self.Name)
        print("Deposited Amount:",self.Amount)
        print("Balance:",self.withdrawn)
        print("ROI",self.Interest)

def main():
        obj=BankAccount(0,0)
        obj.Deposit()
        obj.Withdraw()
        obj.CalculateIntrest()
        obj.Display()
        
if __name__=="__main__":
    main()
