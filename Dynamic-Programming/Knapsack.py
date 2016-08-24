#0-1 Knapsack problem

def selectionSort(v,w):
    for i in range(len(w)-1):
        pos = i
        for j in range(i+1,len(w)):
            if w[j] < w[pos]:
                pos = j

        #both the arrays are now sorted simultaneously
        temp = w[i]
        w[i] = w[pos]
        w[pos] = temp
        temp = v[i]
        v[i] = v[pos]
        v[pos] = temp 


##w = [5,6,2,7,1,8,9]
##v = [1,3,2,1,2,2,1]
##print(w)
##print(v)
##selectionSort(v,w)

def Knapsack(valArr, wtArr, Wt):

    #The valArr and wtArr should be sorted according to the wtArr
    selectionSort(valArr, wtArr)
    
    #initialising the 2D memoization table
    row = len(valArr)
    col = Wt
    K = [[0 for x in range(col+1)] for y in range(row+1)]

    #Modifying the valArr and wtArr arrays by adding a 0's at their starts
    valArr = [0] + valArr
    wtArr = [0] + wtArr

    #Populating the memoization table
    for i in range(row+1):
        for j in range(col+1):
            
            if i==0 or j==0:#make a barrier row and column
                K[i][j] = 0
                continue

            if(j - wtArr[i] >= 0):#take the maximum of the previous value, or the present item
                K[i][j] = max(K[i-1][j], valArr[i]+K[i-1][j-wtArr[i]])

            else:#use the highest previous value
                 K[i][j] = K[i-1][j]

    #Print out the maximum value and the value matrix
    print("The maximum value is: "+str(K[row][col]))

    #Print the value matrix
    for x in K:
        print(x)

    #Finding the elements which contributed to the maximum value
    check(wtArr,K,row,col)

def check(w,K,row,col):
    
    if row==0 or col==0:#the process is finished
        return

    if K[row][col] == K[row-1][col]:#then the element in this row is not included in the final solution
        check(w,K,row-1,col)

    else:#select this element and then move onto the next element
        print("The element with weight "+str(w[row])+" is selected.")
        check(w,K,row-1,col-w[row])

#driver part
a1 = [1,4,5,7]
a2 = [1,3,4,5]
Knapsack(a1, a2, 7)
