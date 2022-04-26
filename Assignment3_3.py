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
    
   
    min1 = data[0]
    for i in range(1,len(data)):
        if ( data[i] < min1):
            min1 = data[i]
      
    print("Minimum number is:",min1)
             
   
def main():
    
    print("Enter the how many numbers you want:")
    n = int(input())
    call(n)
    
if __name__=="__main__":
	main()