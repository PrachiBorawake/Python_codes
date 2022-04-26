def call(num1):
    cnt = 0
    while(num1 > 0):
        num1 = num1//10
        cnt = cnt+1
        
    print("The digits in number:",cnt)
            
def main():
    print("Enter the num:")
    num = int(input())
    
    call(num)
if __name__=="__main__":
    main()