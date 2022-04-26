import os
import threading

def display():
    print("Thread name : ",threading.current_thread().name)
    sequnce =[]
    for i in range(1,51):
        sequnce.append(i)
    print(sequnce)

def reverse():
    print("Thread name : ",threading.current_thread().name)
    reverse = []
    for i in range(50,0,-1):
        reverse.append(i)
    print(reverse)
    


def main():
    print("PID of main:",os.getpid())
    
    thread1=threading.Thread(target=display,name="Sequence num")
    thread2=threading.Thread(target=reverse,name="Reverse num")
    
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()
    


if __name__=="__main__":
	main()