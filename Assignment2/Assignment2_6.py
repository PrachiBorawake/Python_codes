def call(val):
    for i in range(val,0,-1):
        for j in range (0,i):
            print("*",end=' ')
        print()
        
    
def main():
    print("Enter the num:")
    num = int(input())
    
    call(num)
if __name__=="__main__":
	main()