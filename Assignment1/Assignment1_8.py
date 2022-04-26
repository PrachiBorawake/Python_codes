def call(val):
    for i in range (0,val):
        print("*",end =' ')
def main():
    print("Enter the value of num:")
    num = int(input())
    call(num)
if __name__=="__main__":
    main()