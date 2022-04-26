#Write a program which accepts file name from user and check whether that file exists in
#current directory or not.Input : Demo.txt
#Check whether Demo.txt exists or not.

def main():

    try:
        print("Enter the name of file that you want to search:")
        fd=input()
        fd=open('study.txt')
        print(file)
        fd.close()
        
    except Exception:
        print("File not found")
    
    
if __name__=="__main__":
	main()