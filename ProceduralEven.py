def chkEven(no):
    if (no % 2 == 0):
        print("Its Even number")
    else:
        print("Its Odd number")


def main():
    value = int(input("Enter number: "))
    
    chkEven(value)

if __name__ == "__main__":
    main()