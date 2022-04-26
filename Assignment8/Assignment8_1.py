import os
import threading



        
def even():
    #print("PID of even is:",os.getpid())
    #print("PPID of even is :",os.getppid())
    print("Thread Name:",threading.current_thread().name)
    elist = []
    for i in range(0,20,2):
        elist.append(i)
    print(elist)
    
    
def odd():
    #print("PPID of odd is :",os.getppid())
    print("Thread Name:",threading.current_thread().name)
    olist = []
    for i in range(1,20,2):
        olist.append(i)
    print(olist)
    
def main():
    print("PID of main :",os.getpid())
    
    
    thread1=threading.Thread(target = even,name="even")
    thread2=threading.Thread(target = odd,name="odd")
    
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()
    

if __name__=="__main__":
	main()