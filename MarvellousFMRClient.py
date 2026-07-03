from MarvellousLibrary import filterX, mapX, reduceX

CheckEven = lambda No: (No % 2 == 0)
Increament = lambda No: No+1
Addition = lambda No1, No2: No1 + No2

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is: ",Data)

    fData = list(filterX(CheckEven, Data))
    print("Data after filter: ",fData)

    mData = list(mapX(Increament, fData))
    print("Data after map: ",mData)

    rData = reduceX(Addition, mData)
    print("Data after reduce: ",rData)

if __name__ == "__main__":
    main()