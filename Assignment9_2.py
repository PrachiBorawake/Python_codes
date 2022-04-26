#Write a program which accept file name from user and open that file and display the contents
#of that file on screen.
#Input : Demo.txt
#Display contents of Demo.txt on console.
import os

def main():

    print("Enter the name of file:")
    name=input()
    
    if os.path.exists(name):
        fd=open(name,"r")
    
        data=fd.read()
    
        print("The data is:",data)
        
        
    else:
        print("There is no such file")
        #fd=open(name,"x")
        
        #print("Enter the data to be inserted in file:")
        #data=input()
        
        #fd.write(data)
        #fd.close()

if __name__=="__main__":
    main()