def binarySearch( array, key ) :
    
    LB = 0
    UB = len(array)

    for i in range ( 0 , len(array) ):
        
        mid = ( LB + UB )//2

        if array[mid] > key :
            UB = mid - 1

        elif array[mid] < key :
            LB = mid + 1

        else :
            return mid
    
    return -1
        

size = ( int ( input ( "Enter the size of Array: " ) ) )

array = [] 

print( "Enter the elements of Array: " )
for i in range (0, size) :
    element = ( int ( input ( ) ) )
    array.append(element)

key = ( int ( input ( "Enter the key to be found: " ) ) )

result = binarySearch( array, key )

if result == -1 :
    print("Key not found. ")

else :
    print("Key found at " , result + 1 , "th index. ")
