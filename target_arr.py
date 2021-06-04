def targetArr( num, arr ):
    #print(num)
    #print(arr)

    for i in range(len(arr) - 1):
        #print("i=", i)
        for j in range(i + 1, len(arr)):
            #if (arr[i] + arr[j])
            #print("j=", j)

            if (arr[i] + arr[j] == num):
                #print("successful i=", i)
                #print("successful j=", j)
                return [arr[i], arr[j]]

arr = [2,7,11,15]
given_num = 9


#print(targetArr(9, arr))
