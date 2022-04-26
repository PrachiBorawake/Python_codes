import os

def main():
    print("Enter the name of file that want to be search:")
    name=input()
    
    if (os.path.exists(name)):
        fd=open(name,"r")
        
        data=fd.read()
        
        print("The data is :",data)
        fd.close()
    
    else:
        print("File is not exist")
        
if __name__=="__main__":
    main()
    
    