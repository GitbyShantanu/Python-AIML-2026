def chkEven(no):
    return no % 2 == 0

def main():
    value = int(input("Enter number: "))
    
    Ret = chkEven(value)
    
    if (Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd Number")    

if __name__ == "__main__":
    main()