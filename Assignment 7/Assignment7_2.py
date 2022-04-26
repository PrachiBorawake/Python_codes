i = 0
def display(no):
    global i
    if (i < no):
        print(i,end =" ")
        i=i+1
        display(i)
        
     
    
    
def main():
    x=int(input(print("Enter the number to display the series:")))
    display(x)
    
if __name__=="__main__":
	main()