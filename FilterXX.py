
CheckEven = lambda no: (no % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is: ",Data)

    fData = list(filter(CheckEven, Data))
    print("Data after filter: ",fData)


if __name__ == "__main__":
    main()