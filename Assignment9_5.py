#Accept file name and one string from user and return the frequency of that string from file.
#Input : Demo.txt Marvellous
#Search “Marvellous” in Demo.txt

import os
from sys import *


def main():
    print("Number of arguments",len(argv))
    
    if os.path.exists(argv[1]):
        fd=open(argv[1],"r")
        data=fd.read()
        print(data)
        
        fd.close()

if __name__=="__main__":
    main()