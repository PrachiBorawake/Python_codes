def ChkNum(val):

    if(val%2 == 0):
        print("The number is even:",val)
    else:
        print("The number is odd:",val)
    

def main():
    num  = 0
    print("Enter the number:")
    num = int(input())
    ChkNum(num)
if __name__=="__main__":
	main()