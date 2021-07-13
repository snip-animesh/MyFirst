from numpy import *
row_1=int(input("Enter the row number of 1st Matrix :"))
col_1=int(input("Enter the col number of 1st Matrix :"))
row_2=int(input("Enter the row number of 2nd Matrix :"))
col_2=int(input("Enter the col number of 2nd Matrix :"))
mat1=[]
mat2=[]
if col_1==row_2:
    for i in range(row_1):
        temp=[]
        print("Enter the Element of 1st Matrix's row {}\n".format(i+1))
        for j in range(col_1):
            temp.append(int(input()))
        mat1.append(temp)
    for i in range(row_2):
        temp=[]
        print("Enter the Element of 2nd Matrix's row {}\n".format(i + 1))
        for j in range(col_2):
            temp.append(int(input()))
        mat2.append(temp)


    result=[]

    for r_1 in range(row_1):
        sum=[]

        for c_2 in range(col_2):
            s = 0
            for r_2 in range(row_2):
                s=mat1[r_1][r_2]*mat2[r_2][c_2]+s
            sum.append(s)
        result.append(sum)
    result=matrix(result)
    print(result)

else:
    print("Column Number of Matrix 1 must be Equal to row number of Matrix 2 for Multiplication.\n")
