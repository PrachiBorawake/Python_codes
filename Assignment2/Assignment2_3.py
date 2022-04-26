def call(num):
    i = 1
    fact = 1
    while(i<=num):
        
        fact = fact * i
        i = i + 1
    print("Factorial of the number is:",fact)

        

def main():
    print("Enter the number:")
    num = int(input())
    call(num)
    
if __name__=="__main__":
    main()