#import primm as P
def call(n1):
    i=1
    data = []
    
    while(i<=n1):
        print("Enter the number:")
        num = int(input())
        i = i+1
        data.append(num)
    print(data)
    return data

def chkprime(data1):
    if data == 1:
        print("not prime")
    for i in data:
        if(data % i ==0):
            print("not prime",data[i],)
        else:
            print("prime",data[i])        

    #ret = P.chkprime(data)
    
def main():
    
    print("Enter the how many numbers you want:")
    n = int(input())
    data=call(n)
    chkprime(data)
    
if __name__=="__main__":
	main()