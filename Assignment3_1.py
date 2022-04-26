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
        
    ret = A.addition(data)
    print("The addition is:",ret)
    
def main():
    
    print("Enter the how many numbers you want:")
    n = int(input())
    call(n)
    
if __name__=="__main__":
	main()