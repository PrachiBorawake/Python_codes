#Write a program which contains one lambda function which accepts two parameters and return its multiplication
#def mult(val1,val2):
    #ans=0
    #ans= val1 * val2
    #return ans
    
mult = lambda a,b : a*b

def main():
    print("Enetr 1st num:") 
    num1 = int(input())
    
    print("Enetr the 2nd num:")
    num2= int(input())
    
    ret = mult(num1,num2)
    print("the multiplication is:",ret)
if __name__=="__main__":
    main()