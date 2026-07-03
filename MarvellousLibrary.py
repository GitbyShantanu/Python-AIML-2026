def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no) 
        if Ret == True:
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result

def reduceX(Task, Elements):
    Ans = 0
    for no in Elements:
        Ans = Task(Ans, no)
    
    return Ans