def minor(n, matrix):
    l = len(matrix)
    matrix[n[0]] = [None for i in range(l)]
    nmatrix = []
    for i in range(l):
        m = []
        for j in range(l):
            if not j==n[1] and not matrix[i][j]==None:
                m.append(matrix[i][j])
        if len(m)!=0:
            nmatrix.append(m)
    print(nmatrix)
    return(nmatrix)

def determinant(matrix):
    if len(matrix)==1:
        return(matrix[0][0])
    elif len(matrix)==2:
        return(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    else:
        ret = 0
        c = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if c%2==0:
                    ret-=determinant(minor([i, j], matrix))
                else:
                    ret+=determinant(minor([i, j], matrix))
                c+=1
    return(ret)
        

m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

# print(minor([0, 1], m2))

print(determinant([[1]]), 1, "Determinant of a 1 x 1 matrix yields the value of the one element")
print(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
print(determinant(m2) == -20)