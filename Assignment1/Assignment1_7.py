def div(val):
    if (val % 5)==0:
        print("The number is divisible by 5:")
    else:
        print("The number is not divisible by 5:") 
        

def main():
    print("Enter the number:")
    num = int(input())
    div(num)
if __name__=="__main__":
	main()