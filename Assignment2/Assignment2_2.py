def call(num):
    i = 0
    for i in range(0,num):
        for j in range(0,num):
            print("*",end=' ')
        print()
            
def main():
    print("Enter the num:")
    num = int(input())
    call(num)
if __name__=="__main__":
    main()