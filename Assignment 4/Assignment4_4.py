#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
#List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.

from functools import reduce
    
    
checkeven = lambda a : a%2==0

Increment = lambda a:a*a

sum = lambda a,b: a+b

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
    newdata = list(filter(checkeven,data))
    print("data after filter:",newdata)
    
    #map(function,list)
    incrementdata = list(map(Increment,newdata))
    print("data after map:",incrementdata)
    
    #reduce(function,list)
    ret =reduce(sum,incrementdata)
    print("data after reduce:",ret)

if __name__=="__main__":
    main()
    
    