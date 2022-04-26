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
    
    max1 = 0
    for i in range(0,len(data)):
        if ( data[i] > max1):
            max1 = data[i]
    #return max1
    print("Maximum number is:",max1)
             
    
def main():
    
    print("Enter the how many numbers you want:")
    n = int(input())
    call(n)
    
if __name__=="__main__":
	main()