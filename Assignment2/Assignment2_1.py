import marvellous as M

    
def main():
    print("Enter first num:")
    no1 = int(input())

    print("Enter second num:")
    no2 = int(input())
    ret1 = M.Addition(no1,no2)
    ret2 = M.Subtraction(no1,no2)
    ret3 = M.Multiplication(no1,no2)
    ret4 = M.Division(no1,no2)
 if    

    print("Addition is :",ret1)
    print("Subtraction is :",ret2)
    print("Multiplication is :",ret3)
    print("division is :",ret4)
    
if __name__=="__main__":
    main()