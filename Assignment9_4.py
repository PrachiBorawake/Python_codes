#Write a program which accept two file names from user and compare contents of both the
#files. If both the files contains same contents then display success otherwise display failure.
#Accept names of both the files from command line.
#Input : Demo.txt Hello.txt
#Compare contents of Demo.txt and Hello.txt
#cmp(file1, file2[, shallow])


from sys import *
import os
import filecmp

def main():
    print("number of arguments are:",len(argv))
    
    f1=argv[1]
    print(f1)
    f2=argv[2]
    
    if os.path.exists(f1):
        fd=open(f1,"r")
        data=fd.read()
        print(data)
        
    if os.path.exists(f2):
        fd=open(f2,"r")
        data=fd.read()
        print(data)
        
        
    result=filecmp.cmp(f1,f2, shallow = False)   
    
    print(result)
    

if __name__=="__main__":
    main()