def LCS(str1, str2):
    #initialising the 2D memoization table
    row = len(str2)
    col = len(str1)
    K = [[0 for x in range(col+1)] for y in range(row+1)]

    #Modifying the strings by converting them into lists and adding a '0's at their starts
    s1 = ['0'] + list(str1)
    s2 = ['0'] + list(str2)

    #populating the memoization table
    for i in range(row+1):
        for j in range(col+1):

            if s2[i]=='0' or s1[j]=='0':#make a barrier row and column
                K[i][j]=0
                continue

            if s2[i]==s1[j]:#the characters match and hence the length of substring increases by 1
                K[i][j] = K[i-1][j-1]+1

            else:#take the value from previously computed values
                K[i][j] = max(K[i-1][j], K[i][j-1])

    #printing the length of the longest common subsequence
    print(K[row][col])
    for x in K:
        print(x)
        
    #printing the longest common subsequence
    s=""
    check(s,K,row,col,s2)

def check(s,K,row,col,s2):

    if row==0 or col==0:#process is finished
        print(s)
        return
    if K[row][col] == K[row-1][col]:#this row did not contribute a character
        check(s,K,row-1,col,s2)

    elif K[row][col] == K[row][col-1]:
        check(s,K,row,col-1,s2)
        
    else:#this row contributed the character
        s = s2[row] + s
        print(s)
        print(str(row)+","+str(col))
        check(s,K,row-1,col-1,s2)

#driver program  
LCS("abcdaf","acbcf")
