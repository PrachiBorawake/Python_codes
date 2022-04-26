i=5
def fun():
    global i
    if (i > 0):
        print(i,end=" ")
        i = i - 1       # i++
        fun()       # Recursive call

def main():
    fun()

if __name__ == "__main__":
    main()