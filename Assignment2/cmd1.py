from sys import *

def main():
    print("number of cmd line arguments are:",len(argv))
    print("Name of application is :",argv[0])
    
    for data in argv:
        print(data)
        
if __name__=="__main__":
    main()