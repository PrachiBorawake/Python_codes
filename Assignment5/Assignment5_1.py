#1.Write a program which contains one class named as Demo.Demo class contains two instance variables as no1 ,no2.
#That class contains one class variable as Value.There are two instance methods of class as Fun and Gun which displays values of instance
#variables.Initialise instance variable in init method by accepting the values from user.After creating the class create the two objects of Demo class as
#Obj1 = Demo(11,21)
#Obj2 = Demo(51,101)
#Now call the instance methods as
#Obj1.Fun()
#Obj2.Fun()
#Obj1.Gun()
#Obj2.Gun()
class Demo:
    val = 20 
    def __init__(self,no1,no2):
        self.a=no1
        self.b=no2

    def fun_instance(self):
        print("Inside fun_instance")
        print(self.a)
        print(self.b)
        
    def gun_instance(self):
        print("Inside gun_instance")
        print(self.a)
        print(self.b)
        
def main():
    print("Enter the 1st num:")
    x = int(input())
    
    print("Enter the 2nd num:")
    y = int(input())
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)
    
    print("value of class variable",Demo.val)
    Obj1.fun_instance()
    Obj2.fun_instance()
    Obj1.gun_instance()
    Obj2.gun_instance()
    #obj.fun_instance()
    #obj.gun_instance()
    #print("value from instance variable:",obj.a ,obj.b)
  
    
    
if __name__=="__main__":
	main()