import addn1 as A
 
def call(num1):
    cnt = 0
    data =[]
    while(num1 > 0):
        num1 = num1//10
        cnt = cnt+1
        data.append(cnt)
    
    print("The digits: ",cnt)
    print(data)
    
    ret = A.addition(data)
    print("Addition is:",ret)
            
def main():
    print("Enter the num:")
    num = int(input())
    
    call(num)
if __name__=="__main__":
    main()
    
    