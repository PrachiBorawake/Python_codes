#Write a program which contains one class named as Arithmetic.
#Arithmetic class contains three instance variables as Value1 ,Value2.Inside init method initialise all instance variables to 0.
#There are three instance methods inside class as Accept(), Addition(), Subtraction(),Multiplication(), Division().
#Accept method will accept value of Value1 and Value2 from user.Addition() method will perform addition of Value1 ,Value2 and return result.
#Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
#Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
#Division() method will perform division of Value1 ,Value2 and return result.
#After designing the above class call all instance methods by creating multiple objects.
class Arithmetic:

    def __init__(self,value1,value2):
        self.a=value1
        self.b=value2

    def Accept(self):
        print("Enter the 1st num:")
        self.value1=int(input())
        
        print("Enter the 2nd num:")
        self.value2=int(input())
        
    def Addition(self):
        ans=self.value1+self.value2
        return ans
        
    def Subtraction(self):
        ans=self.value1-self.value2
        return ans
        
    def Multiplication(self):
        ans=self.value1*self.value2
        print("Multiplication is :",ans)
        
    def Division(self):
        ans=self.value1/self.value2
        print("Division is:",ans)
       

def main():
    obj=Arithmetic(0,0)
    obj.Accept()
    
    ret=obj.Addition()
    print("addition is :",ret)
    
    ret=obj.Subtraction()
    print("Subtraction is:",ret)
    
    obj.Multiplication()
    obj.Division()


if __name__=="__main__":
    main()