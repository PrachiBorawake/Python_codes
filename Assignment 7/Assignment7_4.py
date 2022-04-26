sum=0
def fun(num):
    global sum
    if(num>0):
        digit=num%10
        sum=sum+digit
        num=int(num/10)
        fun(num)
        
    print("sum of digits is:",sum)
    
    

def main():
    num=int(input(print("Enter the num:")))
    fun(num)
    
    

if __name__=="__main__":
	main()