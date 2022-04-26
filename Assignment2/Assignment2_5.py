def prime(val):
    for i in range (2,val):
        if(val % i) == 0:
            print("It is not prime number")
            break
    else:
            print("It is prime")
        
    
def main():
    print("Enter the number:")
    num = int(input())
    
    prime(num)
    
if __name__=="__main__":
    main()