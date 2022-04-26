#Write a program which accept file name from user and create new file named as Demo.txt and
#copy all contents from existing file into new file. Accept file name through command line
#arguments.
#Input : ABC.txt
#Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
from sys import *
import os 
import shutil


def main():
    print("number of cmd line arguments are:",len(argv))
    print("File name is :",argv[0])
    
    
    #name=argv[1]
    
    if os.path.exists(argv[0]):
        fd=open(argv[0],"a")
        
    shutil.copyfile("study.txt","demo.txt")
        
           
        
if __name__=="__main__":
    main()