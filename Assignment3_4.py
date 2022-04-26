import addn1 as A
def call(n1):
    i=1
    data = []
    
    while(i<=n1):
        print("Enter the number:")
        num = int(input())
        i = i+1
        data.append(num)
    print(data)
   
    print("Number is to be search:")
    num1 = int(input())
    
    cnt = 0
    for i in data:
        if( i == num1):
            cnt = cnt + 1
    print("The occurence of number is:",cnt)        
    
             
    
def main():
    
    print("Enter the how many numbers you want:")
    n = int(input())
    call(n)
    
if __name__=="__main__":
	main()