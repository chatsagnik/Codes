def subsetSum(arr,val):

    #initialising the 2D memoization table
    row = len(arr)
    col = val+1
    K = [[0 for x in range(col)] for y in range(row)]

    #initializing the table
    for i in range(row):
        K[i][0] = 1
        
    #populating the memoization table
    for i in range(row):
        for j in range(col):

            if arr[i] == j:#If the value is equal to sum, set value as true
                K[i][j] = 1
                continue

            if arr[i] > j:#copy the value from above
                K[i][j] = K[i-1][j]
                continue

            #Either take the value from above or include the present element to check if sum possible
            K[i][j] = max(K[i-1][j - arr[i]], K[i-1][j])

    #printing the length of the longest common subsequence
    print(str(row)+","+str(col))

    if K[row-1][col] == 1:
        print("Sum possible from given subset.")

    else:
        print("Sum not possible from given subset.")

    for x in K:
        print(x)

##    #print the elements included in the sum
##    check(K,row,col)

#driver program
arr = [2,3,7,8,10]
val = 11
subsetSum(arr,val)
