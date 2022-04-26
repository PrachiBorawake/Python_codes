#Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. 
#Reduce will return product of all that numbers.

from functools import reduce
    
    
check = lambda a : a>=70 and a<=90

Increment = lambda no:no+10

product = lambda a,b: a*b

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
    
    
    
    #filter(function,list)
    newdata = list(filter(check,data))
    print("data after filter:",newdata)
    
    #map(function,list)
    incrementdata = list(map(Increment,newdata))
    print("data after map:",incrementdata)
    
    #reduce(function,list)
    ret =reduce(product,incrementdata)
    print("data after reduce:",ret)

if __name__=="__main__":
    main()
    
    