def call(val):
    
    for i in range(0,val):
        n = 1
        for j in range (0,val):
            print(n,end=' ')
            n = n + 1
        print()
        
    
def main():
    print("Enter the num:")
    num = int(input())
    
    call(num)
if __name__=="__main__":
	main()