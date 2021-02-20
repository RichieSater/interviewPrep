#[3,5,1,2] results in [10,6,30,15]
#[3,0,1,2] results in [0,6,0,0]
#[3,0,0,2] results in [0,0,0,0]

array1 = [3,5,1,2]
array2 = [3,0,1,2]
array3 = [3,0,0,2]


# 3 Cases:  Single Zero, Multi Zero, No Zero

def Solver(array):
    oneZero = False
    multiZero = False
    totalProduct = 1
    zeroIndex = -1 
    
    for i,x in enumerate(array):
        if array[i] == 0 and oneZero:
            multiZero = True
            break
        elif array[i] == 0 and not oneZero:
            oneZero = True
            zeroIndex = i
        else: 
            totalProduct = totalProduct * array[i]
        
    if multiZero:
        #array full of zero's
        length = len(array)
        answer = [0] * length
    elif oneZero:
        length = len(array)
        answer = [0] * length
        answer[zeroIndex] = totalProduct
    else:
        length = len(array)
        answer = [0] * length
        for i,x in enumerate(answer):
            answer[i] = totalProduct/array[i]     

    return(answer)

print(Solver(array1))
print(Solver(array2))
print(Solver(array3))