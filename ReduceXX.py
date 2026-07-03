from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

Increament = lambda No: No+1

Addition = lambda No1, No2: No1 + No2

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is: ",Data)

    fData = list(filter(CheckEven, Data))
    print("Data after filter: ",fData)

    mData = list(map(Increament, fData))
    print("Data after map: ",mData)

    rData = reduce(Addition, mData)
    print("Data after reduce: ",rData)


if __name__ == "__main__":
    main()