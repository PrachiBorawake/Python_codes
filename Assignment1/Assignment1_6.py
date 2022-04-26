def call(val):
    if(val > 0):
        print("The number is positive:",val)
    elif(val < 0): 
        print("The number is negative:",val)
    else:
        print("The number is zero",val)
            
def main():
    num = 0
    print("Enter the number:")
    num = int(input())
    call(num)
	
if __name__=="__main__":
	main()
