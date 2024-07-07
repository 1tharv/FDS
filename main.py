def data_input(Row ,Column):
    matrix=[]
    for i in range(Row):    
        a = []
        for j in range(Column):   
            a.append(int(input()))
        matrix.append(a)
    return matrix
    
def display(Row,Column,matrix):
    for i in range(Row):
        for j in range(Column):
            print(matrix[i][j], end=" ")
        print()
        
def sub(row,column,matrixA,matrixB):
    ans=[]
    
    for x in range(row):    
        a = []
        for y in range(column):   
            a.append(int(0))
        ans.append(a)
        
    for i in range(row):
        for j in range(column):
            ans[i][j]=matrixA[i][j]-matrixB[i][j]
    return ans

def main():
    matrixA=[]
    matrixB=[]
    answer=[]
    
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))
    print("\nData for Matrix A")
    matrixA=data_input(Row,Column)
    print("\nMatrix A is")
    display(Row,Column,matrixA)
    print("\nData for Matrix B")
    matrixB=data_input(Row,Column)
    print("\nMatrix B is")
    display(Row,Column,matrixB)
    print("\nMatrix A-B is")
    answer=sub(Row,Column,matrixA,matrixB)
    display(Row,Column,answer)
    
main()