#Write a program which contains one lambda function which accepts one parameter and return  power of two.

#def mult(val1,val2):
    #ans=0
    #ans= val1 * val2
    #return ans
    
power = lambda a : a**2

def main():
    print("Enetr 1st num:") 
    num1 = int(input())
    
    ret = power(num1)
    print("the power o number is:",ret)
if __name__=="__main__":
    main()