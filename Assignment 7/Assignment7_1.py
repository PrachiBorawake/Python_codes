def display(i):
    if(i<5):
        print("*", end =" ")
        i = i+1
        display(i)
        
def main():
    display(0)


if __name__=="__main__":
	main()