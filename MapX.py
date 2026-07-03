def CheckEven(No):
    return (No % 2 == 0)

def Increament(No):
    return No+1

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is: ",Data)

    fData = list(filter(CheckEven, Data))
    print("Data after filter: ",fData)

    mData = list(map(Increament, fData))
    print("Data after map: ",mData)

if __name__ == "__main__":
    main()