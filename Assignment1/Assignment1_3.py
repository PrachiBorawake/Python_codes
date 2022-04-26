def Add(val1,val2):
    ret = val1 +val2
    return ret
    

def main():
    print("Enter the 1st number:")
    num1 = int(input())
    print("Enter the 2nd number:")
    num2 = int(input())
    ret = Add(num1,num2)
    
    print("The addition is:",ret)

if __name__=="__main__":
	main()