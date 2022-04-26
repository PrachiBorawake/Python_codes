import os
import threading


def even(No):
    i = 1
    
    while(i <= No):
        if(No%i==0):
            i=i+1
    
    print("Addition is:",i)


def main():
    print("PId of main:",os.getpid())
    print("Enter the numbers:")
    No = int(input())
    
    thread1=threading.Thread(target= even, args = (No,), name="Evenfactor")
    #thread2=threading.Thread(target=odd,args = (No,),name="Oddfactor")
    
    thread1.start()
    thread1.join()
    #thread2.start()

if __name__=="__main__":
	main()