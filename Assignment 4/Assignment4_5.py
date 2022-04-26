#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
#List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
#Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. 


from functools import reduce
    
    
checkprime = lambda a: all( a%i != 0 for i in range(2, int(a**.5)+1) )

Increment = lambda a:a*2

max1 = lambda a,b: a if (a>b) else b

def main():
    data =[]
    i=1
    print("Enter the how many numbers you want:")
    n = int(input())
    
    while(i<=n):
        print("Enter the number:")
        num = int(input())
        i = i+1
        data.append(num)
    print(data)
    
    
    #print("The list is:",data)
    
    #filter(function,list)
    newdata = list(filter(checkprime,data))
    print("data after filter:",newdata)
    
    #map(function,list)
    incrementdata = list(map(Increment,newdata))
    print("data after map:",incrementdata)
    
    #reduce(function,list)
    ret =reduce(max1,incrementdata)
    print("data after reduce:",ret)

if __name__=="__main__":
    main()
    
    