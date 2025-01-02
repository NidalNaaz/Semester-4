def AddMatrices( Matrix1, Matrix2 ) :
    
    if len( Matrix1 ) != len( Matrix2 ) or len(Matrix1[0]) != len(Matrix2[0]):
        print("Unequal matrices.")
        return None
    
    Matrix3 = []

    for i in range ( 0, len( Matrix1 ) ) : 

        row = []
 
        for j in range ( 0, len( Matrix1[0] ) ) :
            row.append(Matrix1[i][j] + Matrix2[i][j])
                
        Matrix3.append(row)

    return Matrix3


rows1 = int ( input ( "Enter the number of rows in the matrix 1: " ) )
columns1 = int ( input ( "Enter the number of columns in the matrix 1: " ) )


print( "Enter the elements of the matrix 1 : " ) 

matrix1 = []

for i in range (0, rows1) :

    rows = []

    for j in range (0, columns1) :
        rows.append( int (input( )))
    
    matrix1.append(rows)



rows2 = int ( input ( "Enter the number of rows in the matrix 2: " ) )
columns2 = int ( input ( "Enter the number of columns in the matrix 2: " ) )

print( "Enter the elements of the matrix 2 : " ) 

matrix2 = []

for i in range (0, rows2) :

    rows = []

    for j in range (0, columns2) :
        rows.append( int (input( )))
    
    matrix2.append(rows)

result = AddMatrices( matrix1 , matrix2 )

if result is not None: 
    print("Result of addition of two matrices: ")

    for row in result:
        print(row)
