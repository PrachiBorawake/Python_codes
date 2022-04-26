import addn1 as A

def fact(val):
    i = 1
    data = []
    print("The factors are:")
    while(i<=val):
        if(val % i) == 0:
            #print(i)
            data.append(i)
        
        i=i+1
    print(data)
    
    ret = A.addition(data)
    print("Addition is:",ret)
    
def main():
    
    print("Enter the num:")
    num = int(input())
    fact(num)
    
    
    
    
if __name__=="__main__":
	main()