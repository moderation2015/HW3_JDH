def factorial(x):
    if( x==0):
        return 1
    else:
        return x*factorial(x-1)

def main():
    for i in range(0,16 ,2):
        print(i,"factorial=", factorial(i))

if __name__ == "__main__":
    main()
    

